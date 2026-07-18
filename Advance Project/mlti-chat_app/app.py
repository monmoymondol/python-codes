from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, leave_room, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def chat():
    return render_template("chat.html")

@socketio.on("join")
def handle_join(data):
    username = data["username"]
    room = data["room"]
    join_room(room)
    send(f"👋 {username} has joined {room}", to=room)

@socketio.on("leave")
def handle_leave(data):
    username = data["username"]
    room = data["room"]
    leave_room(room)
    send(f"👋 {username} has left {room}", to=room)

@socketio.on("message")
def handle_message(data):
    room = data["room"]
    msg = f"{data['username']}: {data['msg']}"
    send(msg, to=room)

if __name__ == "__main__":
    socketio.run(app, debug=True)
