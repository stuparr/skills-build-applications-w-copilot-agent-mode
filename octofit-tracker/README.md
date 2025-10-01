# OctoFit Tracker

A fitness tracking application built with Django REST Framework and React, designed to help users track their fitness activities, compete with teams, and get personalized workout suggestions.

![OctoFit Home](https://github.com/user-attachments/assets/088ac8ce-819d-4466-b3d9-865a35cbd9fd)

## Features

- **User Profiles**: Track user information and team membership
- **Activity Logging**: Record workout activities with duration tracking
- **Team Management**: Create and manage fitness teams
- **Competitive Leaderboard**: See how you rank against other users
- **Workout Suggestions**: Get personalized workout recommendations

## Technology Stack

### Backend
- Python 3.12
- Django 4.1.7
- Django REST Framework 3.14.0
- SQLite database

### Frontend
- React 18
- React Router DOM
- Bootstrap 5
- JavaScript (ES6+)

## Getting Started

### Prerequisites
- Python 3.12 or higher
- Node.js 20.x or higher
- npm 10.x or higher

### Backend Setup

1. Navigate to the backend directory:
```bash
cd octofit-tracker/backend
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Populate the database with test data:
```bash
python manage.py populate_db
```

6. Start the Django development server:
```bash
python manage.py runserver 8000
```

The backend API will be available at `http://localhost:8000/`

### Frontend Setup

1. Open a new terminal and navigate to the frontend directory:
```bash
cd octofit-tracker/frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the React development server:
```bash
npm start
```

The frontend will be available at `http://localhost:3000/`

## API Endpoints

- `GET /` - API root with endpoint links
- `GET /api/users/` - List all users
- `GET /api/teams/` - List all teams
- `GET /api/activities/` - List all activities
- `GET /api/leaderboard/` - View leaderboard rankings
- `GET /api/workouts/` - Get workout suggestions

All endpoints support standard REST operations (GET, POST, PUT, PATCH, DELETE).

## Project Structure

```
octofit-tracker/
├── backend/
│   ├── octofit_tracker/
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── populate_db.py
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── manage.py
│   └── requirements.txt
└── frontend/
    ├── public/
    │   └── octofitapp-small.png
    └── src/
        ├── components/
        │   ├── Activities.js
        │   ├── Home.js
        │   ├── Leaderboard.js
        │   ├── Teams.js
        │   ├── Users.js
        │   └── Workouts.js
        ├── App.js
        └── index.js
```

## GitHub Codespaces Support

This application is configured to work seamlessly with GitHub Codespaces:

- Backend automatically detects the `CODESPACE_NAME` environment variable
- Frontend uses `REACT_APP_CODESPACE_NAME` for API endpoint configuration
- Ports 8000 (backend) and 3000 (frontend) are configured for public access

## Sample Data

The application comes with sample data including:

- 5 users across 3 teams
- 8 recorded activities
- Competitive leaderboard with rankings
- 4 suggested workouts

## Contributing

This project was built as part of the GitHub Copilot Agent Mode skills exercise.

## License

MIT License - See LICENSE file for details
