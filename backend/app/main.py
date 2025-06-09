from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.routers import subjects, sessions, analytics
from app.services.timer_service import TimerManager
import json

app = FastAPI(title="Study Tracker API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Timer manager for real-time updates
timer_manager = TimerManager()

# Include routers
app.include_router(subjects.router, prefix="/api/subjects", tags=["subjects"])
app.include_router(sessions.router, prefix="/api/sessions", tags=["sessions"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["analytics"])

# WebSocket for real-time timer updates
@app.websocket("/ws/timer/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await timer_manager.connect(websocket, user_id)
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            await timer_manager.handle_message(user_id, message)
    except WebSocketDisconnect:
        timer_manager.disconnect(user_id)
