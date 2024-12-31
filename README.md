# Chat Box
Chat Box is a real-time web chat application built with Flask and Socket.IO, featuring a modern UI, dynamic user management, and real-time messaging capabilities. The application supports instant messaging, user presence tracking, and message management.

![Screenshot of app](/images/chatbox_sample.png)

## Technical Stack
- Backend: Python (Flask + Flask-SocketIO)
- Frontend: HTML, CSS, JavaScript
- Real-time Communication: Socket.IO
- Avatar Service: Liara Avatar API

  
## Technical Implementation Details

| Feature | Description |
|---------|-------------|
| Real-time Communication | Implements Socket.IO for bidirectional real-time communication between clients and server. Uses event-based architecture to handle messages, user status updates, and system notifications across all connected clients. |
| Message Handling | Messages are stored server-side with unique UUIDs. Includes sender information, message content, and metadata. Supports real-time message broadcasting to all connected clients while maintaining message ownership for deletion capabilities. |
| Message Deletion | Allows users to delete their own messages using a client-side delete button that appears on hover. Implements server-side validation to ensure only message owners can delete their messages. Deletions are synchronized across all connected clients. |
| System Notifications | Automatically generates and broadcasts system messages for user events: join notifications, leave notifications, and username changes. |
| Responsive UI | Features a modern chat interface with distinct message styling for sent vs received messages. Implements message bubbles, user avatars, and system messages with different visual treatments. Messages are automatically scrolled into view. |
| Connection Management | Handles user disconnections gracefully by removing user data from active sessions and notifying other users. Maintains consistent state across the application when users join or leave. |
| Code Organization | Separates concerns between frontend and backend logic. Frontend handles UI updates and event triggering, while backend manages state and broadcasts. Uses clear naming conventions and modular event handlers. |
