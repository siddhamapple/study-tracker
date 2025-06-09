import React, { useState } from 'react';
import MinimizableTimer from './components/Timer/MinimizableTimer';
import './App.css';

function App() {
  const [userId] = useState('user123'); // In real app, get from auth

  return (
    <div className="App">
      <header className="app-header">
        <h1>📚 Study Tracker</h1>
      </header>
      
      <main className="app-main">
        <div className="dashboard">
          <div className="dashboard-section">
            <h2>Today's Progress</h2>
            <p>Start studying to see your progress!</p>
          </div>
          
          <div className="dashboard-section">
            <h2>Subjects</h2>
            <p>Manage your subjects here</p>
          </div>
          
          <div className="dashboard-section">
            <h2>Analytics</h2>
            <p>View your study analytics</p>
          </div>
        </div>
      </main>
      
      {/* Minimizable Timer - Always available */}
      <MinimizableTimer userId={userId} />
    </div>
  );
}

export default App;
