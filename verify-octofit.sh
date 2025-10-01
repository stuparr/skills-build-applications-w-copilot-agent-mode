#!/bin/bash
# Quick verification script for OctoFit Tracker

set -e

echo "🏋️ OctoFit Tracker Verification Script"
echo "======================================"
echo ""

# Check if we're in the right directory
if [ ! -d "octofit-tracker" ]; then
    echo "❌ Error: octofit-tracker directory not found"
    echo "Please run this script from the repository root"
    exit 1
fi

echo "✅ Found octofit-tracker directory"
echo ""

# Check backend files
echo "📋 Checking backend files..."
BACKEND_FILES=(
    "octofit-tracker/backend/requirements.txt"
    "octofit-tracker/backend/manage.py"
    "octofit-tracker/backend/octofit_tracker/models.py"
    "octofit-tracker/backend/octofit_tracker/serializers.py"
    "octofit-tracker/backend/octofit_tracker/views.py"
    "octofit-tracker/backend/octofit_tracker/urls.py"
    "octofit-tracker/backend/octofit_tracker/admin.py"
    "octofit-tracker/backend/octofit_tracker/management/commands/populate_db.py"
)

for file in "${BACKEND_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✅ $file"
    else
        echo "  ❌ Missing: $file"
        exit 1
    fi
done

echo ""
echo "📋 Checking frontend files..."
FRONTEND_FILES=(
    "octofit-tracker/frontend/package.json"
    "octofit-tracker/frontend/src/App.js"
    "octofit-tracker/frontend/src/components/Home.js"
    "octofit-tracker/frontend/src/components/Users.js"
    "octofit-tracker/frontend/src/components/Teams.js"
    "octofit-tracker/frontend/src/components/Activities.js"
    "octofit-tracker/frontend/src/components/Leaderboard.js"
    "octofit-tracker/frontend/src/components/Workouts.js"
)

for file in "${FRONTEND_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✅ $file"
    else
        echo "  ❌ Missing: $file"
        exit 1
    fi
done

echo ""
echo "📋 Checking documentation..."
if [ -f "octofit-tracker/README.md" ]; then
    echo "  ✅ README.md found"
else
    echo "  ❌ Missing: README.md"
    exit 1
fi

echo ""
echo "🎉 All verification checks passed!"
echo ""
echo "To run the application:"
echo ""
echo "Backend:"
echo "  cd octofit-tracker/backend"
echo "  source venv/bin/activate"
echo "  python manage.py runserver 8000"
echo ""
echo "Frontend (in a new terminal):"
echo "  cd octofit-tracker/frontend"
echo "  npm start"
echo ""
