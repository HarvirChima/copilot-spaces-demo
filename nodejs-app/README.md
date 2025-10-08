# Task Manager API

A simple Node.js/Express REST API for managing tasks.

## Setup

```bash
npm install
```

## Run the Application

```bash
npm start
```

For development with auto-reload:
```bash
npm run dev
```

The API will be available at `http://localhost:3000`

## API Endpoints

### GET /
API information and available endpoints

### GET /api/tasks
Get all tasks
- Query parameters:
  - `completed` (true/false) - filter by completion status
  - `priority` (high/medium/low) - filter by priority

### GET /api/tasks/:id
Get a specific task by ID

### POST /api/tasks
Create a new task
- Body: `{ "title": "Task name", "priority": "high" }`

### PUT /api/tasks/:id
Update a task
- Body: `{ "title": "New title", "completed": true, "priority": "low" }`

### DELETE /api/tasks/:id
Delete a task

## Example Usage

```bash
# Get all tasks
curl http://localhost:3000/api/tasks

# Get completed tasks
curl http://localhost:3000/api/tasks?completed=true

# Create a task
curl -X POST http://localhost:3000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "New task", "priority": "high"}'

# Update a task
curl -X PUT http://localhost:3000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'

# Delete a task
curl -X DELETE http://localhost:3000/api/tasks/1
```

## Demo Ideas for Copilot Spaces

1. **Add User Authentication**: "Implement user authentication with JWT tokens"
2. **Add Task Categories**: "Add support for categorizing tasks"
3. **Add Due Dates**: "Add due date functionality and overdue task detection"
4. **Add Sorting**: "Implement sorting by different fields"
5. **Write Tests**: "Create unit tests using Jest and Supertest"
6. **Add Input Validation**: "Add comprehensive input validation using express-validator"
