

import zmq

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.connect("tcp://79.98.115.10:1024")  # Replace <receiver_ip> with the receiver's public IP address

message = "Hello from sender!"
socket.send_string(message)
print("Sent message:", message)
