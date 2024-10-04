const http = require('http');
const express = require('express');
const path = require('path');
const { Server } = require('socket.io'); // Corrected import

const app = express();
const server = http.createServer(app);
const io = new Server(server);

// Handle socket connection
io.on('connection', (socket) => {
    console.log('a user connected');
    socket.on('disconnect', () => {
        console.log('user disconnected');
    });
});

// Serve static files
app.use(express.static(path.join(__dirname, 'public')));

// Serve the main page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Start the server
server.listen(3000, () => {
    console.log('Server running on port 3000');
});
