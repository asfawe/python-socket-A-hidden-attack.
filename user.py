from pythonping import ping
from time import sleep

with open("./jeju.png", "rb") as f:
    while True:
        byte = f.read(1024)
        if byte == b"":
            ping("127.0.0.1", verbose=True, count=1, payload=b"EOF")
            break
        ping("127.0.0.1", verbose=True, count=1, payload=byte)
        sleep(0.5)
