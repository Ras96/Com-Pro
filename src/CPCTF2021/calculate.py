import socket
import sys

def linesplit(sock):
    buf_size = 4096
    buf = sock.recv(buf_size).decode('utf-8')
    while True:
        if '\n' in buf:
            (line, buf) = buf.split('\n', 1)
            yield line
        else:
            buf += sock.recv(buf_size).decode('utf-8')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    server_address = ('024076610607', 10013)
    sock.connect(server_address)

    lines = linesplit(sock)
    for _ in range(8):
        print(next(lines))

    sock.send(b'y\n')

    for i in range(20):
        print(next(lines))
        print(next(lines))

        question = next(lines)
        print(question)

        lhs, op, rhs, _, _ = question.split()
        if op == '+':
            ans = int(lhs) + int(rhs)
        else:
            ans = int(lhs) * int(rhs)

        buf = bytearray()
        buf.extend(map(ord, str(ans) + '\n'))

        sock.send(buf)

        print(next(lines))

    print(next(lines))
    print(next(lines))