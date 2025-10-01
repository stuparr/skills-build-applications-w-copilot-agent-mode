#!/bin/bash
# Quick API test script

echo "Testing OctoFit Tracker API..."
echo ""

# Start Django server in background
cd octofit-tracker/backend
source venv/bin/activate
python manage.py runserver 8000 > /tmp/django.log 2>&1 &
DJANGO_PID=$!
cd ../..

echo "Waiting for server to start..."
sleep 5

# Test API endpoints
echo "Testing API endpoints..."
echo ""

echo "1. Testing API Root (/):"
curl -s http://localhost:8000/ | python3 -m json.tool
echo ""

echo "2. Testing Users endpoint:"
curl -s http://localhost:8000/api/users/ | python3 -c "import sys, json; data = json.load(sys.stdin); print(f'Found {len(data)} users')"
echo ""

echo "3. Testing Teams endpoint:"
curl -s http://localhost:8000/api/teams/ | python3 -c "import sys, json; data = json.load(sys.stdin); print(f'Found {len(data)} teams')"
echo ""

echo "4. Testing Activities endpoint:"
curl -s http://localhost:8000/api/activities/ | python3 -c "import sys, json; data = json.load(sys.stdin); print(f'Found {len(data)} activities')"
echo ""

echo "5. Testing Leaderboard endpoint:"
curl -s http://localhost:8000/api/leaderboard/ | python3 -c "import sys, json; data = json.load(sys.stdin); print(f'Found {len(data)} entries')"
echo ""

echo "6. Testing Workouts endpoint:"
curl -s http://localhost:8000/api/workouts/ | python3 -c "import sys, json; data = json.load(sys.stdin); print(f'Found {len(data)} workouts')"
echo ""

# Stop Django server
kill $DJANGO_PID 2>/dev/null

echo "✅ API test complete!"
