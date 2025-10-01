import React from 'react';

const Home = () => {
  return (
    <div className="text-center">
      <h1 className="display-4">Welcome to OctoFit Tracker</h1>
      <p className="lead">Track your fitness goals and compete with your team!</p>
      <img 
        src="/octofitapp-small.png" 
        alt="OctoFit Logo" 
        className="img-fluid my-4"
        style={{ maxWidth: '300px' }}
      />
      <div className="mt-4">
        <h3>Features:</h3>
        <ul className="list-unstyled">
          <li>📊 Track your activities</li>
          <li>👥 Join a team</li>
          <li>🏆 Compete on the leaderboard</li>
          <li>💪 Get personalized workout suggestions</li>
        </ul>
      </div>
    </div>
  );
};

export default Home;
