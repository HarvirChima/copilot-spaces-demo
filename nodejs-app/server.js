const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const PORT = 3000;

app.use(bodyParser.json());

// In-memory task storage
let tasks = [
    { id: 1, title: 'Complete project proposal', completed: false, priority: 'high', created_at: '2024-01-10' },
    { id: 2, title: 'Review pull requests', completed: true, priority: 'medium', created_at: '2024-01-12' },
    { id: 3, title: 'Update documentation', completed: false, priority: 'low', created_at: '2024-01-15' },
    { id: 4, title: 'Fix bug in authentication', completed: false, priority: 'high', created_at: '2024-01-18' }
];

// Middleware for logging
app.use((req, res, next) => {
    console.log(`${new Date().toISOString()} - ${req.method} ${req.path}`);
    next();
});

// Home route
app.get('/', (req, res) => {
    res.json({
        message: 'Task Manager API',
        version: '1.0.0',
        endpoints: {
            tasks: '/api/tasks',
            task_by_id: '/api/tasks/:id'
        }
    });
});

// Get all tasks
app.get('/api/tasks', (req, res) => {
    const { completed, priority } = req.query;
    
    let filteredTasks = tasks;
    
    if (completed !== undefined) {
        const isCompleted = completed === 'true';
        filteredTasks = filteredTasks.filter(task => task.completed === isCompleted);
    }
    
    if (priority) {
        filteredTasks = filteredTasks.filter(task => task.priority === priority);
    }
    
    res.json(filteredTasks);
});

// Get task by ID
app.get('/api/tasks/:id', (req, res) => {
    const taskId = parseInt(req.params.id);
    const task = tasks.find(t => t.id === taskId);
    
    if (!task) {
        return res.status(404).json({ error: 'Task not found' });
    }
    
    res.json(task);
});

// Create new task
app.post('/api/tasks', (req, res) => {
    const { title, priority } = req.body;
    
    if (!title) {
        return res.status(400).json({ error: 'Title is required' });
    }
    
    const newTask = {
        id: tasks.length > 0 ? Math.max(...tasks.map(t => t.id)) + 1 : 1,
        title,
        completed: false,
        priority: priority || 'medium',
        created_at: new Date().toISOString().split('T')[0]
    };
    
    tasks.push(newTask);
    res.status(201).json(newTask);
});

// Update task
app.put('/api/tasks/:id', (req, res) => {
    const taskId = parseInt(req.params.id);
    const task = tasks.find(t => t.id === taskId);
    
    if (!task) {
        return res.status(404).json({ error: 'Task not found' });
    }
    
    const { title, completed, priority } = req.body;
    
    if (title !== undefined) task.title = title;
    if (completed !== undefined) task.completed = completed;
    if (priority !== undefined) task.priority = priority;
    
    res.json(task);
});

// Delete task
app.delete('/api/tasks/:id', (req, res) => {
    const taskId = parseInt(req.params.id);
    const taskIndex = tasks.findIndex(t => t.id === taskId);
    
    if (taskIndex === -1) {
        return res.status(404).json({ error: 'Task not found' });
    }
    
    tasks.splice(taskIndex, 1);
    res.json({ message: 'Task deleted successfully' });
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(PORT, () => {
    console.log(`Task Manager API is running on http://localhost:${PORT}`);
});

module.exports = app;
