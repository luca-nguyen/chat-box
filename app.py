from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import random
import uuid

#### Backend ####

app = Flask(__name__)
socketio = SocketIO(app)

# key: socket id
# value: username and avatarUrl 
users = {}
messages = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on("connect")
def handle_connect():
    # Generate default username 
    username = f"User_{random.randint(1000,9999)}"
    gender = random.choice(["girl","boy"])
    avatar_url = f" https://avatar.iran.liara.run/public/{gender}?username={username}"

    users[request.sid] = { "username":username, "avatar":avatar_url }
    emit("user_joined", {"username":username,"avatar":avatar_url}, broadcast=True)
    emit("set_username", {"username":username})

@socketio.on("disconnect")
def handle_disconnect():
    # Remove user from dictionary
    user = users.pop(request.sid, None)
    if user:
      emit("user_left", {"username":user["username"]}, broadcast=True)


@socketio.on("send_message")
def handle_message(data):
    # Retrieve information of user in current session 
    user = users.get(request.sid)   
    message_id = str(uuid.uuid4())

    # Storing message with unique id
    messages[message_id] = {
            "username":user["username"],
            "avatar":user["avatar"],
            "message":data["message"],
            "sender_id":request.sid,
    }

    if user:
        emit("new_message", {
            "username":user["username"],
            "avatar":user["avatar"],
            "message":data["message"],
            "messageId": message_id,
        }, broadcast=True)

@socketio.on("delete_message")
def handle_delete_message(data):
    message_id = data["messageId"]
    message = messages.get(message_id)
    
    # Validate that message exists and sender is the current sender
    if message and message["sender_id"] == request.sid:  
        messages.pop(message_id)
        emit("message_deleted", {"messageId": message_id}, broadcast=True)

@socketio.on("update_username")
def handle_update_username(data):
    old_username = users[request.sid]["username"]
    new_username = data["username"]
    users[request.sid]["username"] = new_username

    emit("username_updated", {
        "old_username":old_username,
        "new_username":new_username
    }, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, port=5001) 