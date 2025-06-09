import React, { useState, useEffect } from 'react';
import './MinimizableTimer.css';

const MinimizableTimer = ({ userId }) => {
  const [timerState, setTimerState] = useState({
    isRunning: false,
    isMinimized: false,
    elapsed_time: 0,
    total_duration: 1500, // 25 minutes
    mode: 'study',
    subject_id: null
  });
  const [websocket, setWebsocket] = useState(null);

  useEffect(() => {
    // Connect to WebSocket
    const ws = new WebSocket(`ws://localhost:8000/ws/timer/${userId}`);
    
    ws.onmessage = (event) => {
      const message = JSON.parse(event.data);
      
      if (message.action === 'timer_update') {
        setTimerState(prev => ({ ...prev, ...message.data }));
      }
    };
    
    setWebsocket(ws);
    
    return () => {
      ws.close();
    };
  }, [userId]);

  const sendMessage = (message) => {
    if (websocket && websocket.readyState === WebSocket.OPEN) {
      websocket.send(JSON.stringify(message));
    }
  };

  const startTimer = (subjectId) => {
    sendMessage({
      action: 'start_timer',
      subject_id: subjectId,
      mode: 'study'
    });
  };

  const pauseTimer = () => {
    sendMessage({ action: 'pause_timer' });
  };

  const stopTimer = () => {
    sendMessage({ action: 'stop_timer' });
  };

  const toggleMinimize = () => {
    const newMinimized = !timerState.isMinimized;
    setTimerState(prev => ({ ...prev, isMinimized: newMinimized }));
    sendMessage({
      action: 'minimize_timer',
      minimized: newMinimized
    });
  };

  const formatTime = (seconds) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  const remainingTime = timerState.total_duration - timerState.elapsed_time;

  return (
    <div className={`timer-widget ${timerState.isMinimized ? 'minimized' : 'expanded'}`}>
      {timerState.isMinimized ? (
        // Minimized view - floating widget
        <div className="timer-minimized" onClick={toggleMinimize}>
          <div className="timer-mini-display">
            <span className="timer-mini-time">{formatTime(remainingTime)}</span>
            <div className={`timer-mini-status ${timerState.isRunning ? 'running' : 'paused'}`}>
              {timerState.isRunning ? '▶️' : '⏸️'}
            </div>
          </div>
        </div>
      ) : (
        // Expanded view - full timer interface
        <div className="timer-expanded">
          <div className="timer-header">
            <h3>Study Timer</h3>
            <div className="timer-controls-header">
              <button onClick={toggleMinimize} className="minimize-btn">
                ➖
              </button>
            </div>
          </div>
          
          <div className="timer-display">
            <div className="timer-circle">
              <svg width="200" height="200" className="timer-svg">
                <circle
                  cx="100"
                  cy="100"
                  r="90"
                  fill="none"
                  stroke="#e0e0e0"
                  strokeWidth="10"
                />
                <circle
                  cx="100"
                  cy="100"
                  r="90"
                  fill="none"
                  stroke="#4CAF50"
                  strokeWidth="10"
                  strokeDasharray={`${2 * Math.PI * 90}`}
                  strokeDashoffset={`${2 * Math.PI * 90 * (1 - timerState.elapsed_time / timerState.total_duration)}`}
                  transform="rotate(-90 100 100)"
                />
              </svg>
              <div className="timer-text">
                <div className="timer-time">{formatTime(remainingTime)}</div>
                <div className="timer-mode">{timerState.mode}</div>
              </div>
            </div>
          </div>
          
          <div className="timer-controls">
            {!timerState.isRunning ? (
              <button onClick={() => startTimer('default')} className="start-btn">
                Start
              </button>
            ) : (
              <button onClick={pauseTimer} className="pause-btn">
                Pause
              </button>
            )}
            <button onClick={stopTimer} className="stop-btn">
              Stop
            </button>
          </div>
          
          <div className="timer-info">
            <div>Mode: {timerState.mode}</div>
            <div>Elapsed: {formatTime(timerState.elapsed_time)}</div>
          </div>
        </div>
      )}
    </div>
  );
};

export default MinimizableTimer;
