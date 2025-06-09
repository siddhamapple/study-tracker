from fastapi import WebSocket
import asyncio
import json
from datetime import datetime
from typing import Dict, Optional

class TimerManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}
        self.active_timers: Dict[str, dict] = {}
        self.timer_tasks: Dict[str, asyncio.Task] = {}
    
    async def connect(self, websocket: WebSocket, user_id: str):
        await websocket.accept()
        self.active_connections[user_id] = websocket
        
        # Send current timer state if exists
        if user_id in self.active_timers:
            await self.send_timer_update(user_id, self.active_timers[user_id])
    
    def disconnect(self, user_id: str):
        if user_id in self.active_connections:
            del self.active_connections[user_id]
        
        # Stop timer task if running
        if user_id in self.timer_tasks:
            self.timer_tasks[user_id].cancel()
            del self.timer_tasks[user_id]
    
    async def handle_message(self, user_id: str, message: dict):
        action = message.get("action")
        
        if action == "start_timer":
            await self.start_timer(user_id, message.get("subject_id"), message.get("mode", "study"))
        elif action == "pause_timer":
            await self.pause_timer(user_id)
        elif action == "stop_timer":
            await self.stop_timer(user_id)
        elif action == "minimize_timer":
            await self.minimize_timer(user_id, message.get("minimized", True))
    
    async def start_timer(self, user_id: str, subject_id: str, mode: str):
        # Initialize timer state
        self.active_timers[user_id] = {
            "subject_id": subject_id,
            "mode": mode,  # "study", "short_break", "long_break"
            "start_time": datetime.now().isoformat(),
            "elapsed_time": 0,
            "is_running": True,
            "is_minimized": False,
            "total_duration": 25 * 60 if mode == "study" else 5 * 60  # Default durations
        }
        
        # Start timer task
        self.timer_tasks[user_id] = asyncio.create_task(self.timer_loop(user_id))
        
        await self.send_timer_update(user_id, self.active_timers[user_id])
    
    async def pause_timer(self, user_id: str):
        if user_id in self.active_timers:
            self.active_timers[user_id]["is_running"] = False
            
            # Cancel timer task
            if user_id in self.timer_tasks:
                self.timer_tasks[user_id].cancel()
                del self.timer_tasks[user_id]
            
            await self.send_timer_update(user_id, self.active_timers[user_id])
    
    async def stop_timer(self, user_id: str):
        if user_id in self.active_timers:
            timer_data = self.active_timers[user_id]
            
            # Save session to database here
            await self.save_session(user_id, timer_data)
            
            # Clean up
            del self.active_timers[user_id]
            if user_id in self.timer_tasks:
                self.timer_tasks[user_id].cancel()
                del self.timer_tasks[user_id]
            
            await self.send_message(user_id, {"action": "timer_stopped"})
    
    async def minimize_timer(self, user_id: str, minimized: bool):
        if user_id in self.active_timers:
            self.active_timers[user_id]["is_minimized"] = minimized
            await self.send_timer_update(user_id, self.active_timers[user_id])
    
    async def timer_loop(self, user_id: str):
        try:
            while user_id in self.active_timers and self.active_timers[user_id]["is_running"]:
                await asyncio.sleep(1)
                
                if user_id in self.active_timers:
                    self.active_timers[user_id]["elapsed_time"] += 1
                    
                    # Check if timer completed
                    if self.active_timers[user_id]["elapsed_time"] >= self.active_timers[user_id]["total_duration"]:
                        await self.timer_completed(user_id)
                        break
                    
                    await self.send_timer_update(user_id, self.active_timers[user_id])
        except asyncio.CancelledError:
            pass
    
    async def timer_completed(self, user_id: str):
        if user_id in self.active_timers:
            timer_data = self.active_timers[user_id]
            timer_data["is_running"] = False
            timer_data["completed"] = True
            
            await self.send_timer_update(user_id, timer_data)
            await self.save_session(user_id, timer_data)
    
    async def save_session(self, user_id: str, timer_data: dict):
        # Save to Firebase/database
        session_data = {
            "user_id": user_id,
            "subject_id": timer_data["subject_id"],
            "duration": timer_data["elapsed_time"] // 60,  # Convert to minutes
            "session_type": timer_data["mode"],
            "start_time": timer_data["start_time"],
            "end_time": datetime.now().isoformat()
        }
        # TODO: Implement database save
        print(f"Saving session: {session_data}")
    
    async def send_timer_update(self, user_id: str, timer_data: dict):
        await self.send_message(user_id, {
            "action": "timer_update",
            "data": timer_data
        })
    
    async def send_message(self, user_id: str, message: dict):
        if user_id in self.active_connections:
            try:
                await self.active_connections[user_id].send_text(json.dumps(message))
            except:
                # Connection closed
                self.disconnect(user_id)
