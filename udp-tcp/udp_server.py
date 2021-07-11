# Задание 2
# Создайте UDP сервер, который ожидает сообщения о новых устройствах в сети.
# Он принимает сообщения определенного формата, в котором будет идентификатор устройства и печатает новые подключения в консоль.
# Создайте UDP клиента, который будет отправлять уникальный идентификатор устройства на сервер, уведомляя о своем присутствии.

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 8888))
while True:
    try:
        rezult = sock.recv(1024)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print('New connection to the device', rezult.decode('utf-8'))
