
# (c) Aleksander Alekseev 2016, http://eax.me/

import socket, ssl, time

def irc_send(conf, msg_list):
    if msg_list == []:
        return
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = ssl.wrap_socket(tcp_sock)
    ssl_sock.connect( (conf['host'], int(conf['port'])) )

    def ssl_send(cmd):
        ssl_sock.write(cmd.encode() + b'\r\n')

    ssl_send('USER {0} localhost localhost {0}'.format(conf['nick']))
    ssl_send('NICK {}'.format(conf['nick']))
    ssl_send('PASS {}'.format(conf['password']))
    ssl_send('JOIN #{}'.format(conf['channel']))
    for msg in msg_list:
        ssl_send('PRIVMSG #{} :{}'.format(conf['channel'], msg))
        # time.sleep(1.1)
    ssl_send('QUIT')

    while True:
        data = ssl_sock.read()
        if data == b'': # enf of file
            break

    ssl_sock.close()

irc_config = {
    'host': 'irc.gitter.im',
    'port': '6667',
    'nick': 'devzen_ru_twitter',
    'password': 'SECRET',
    'channel': 'DevZenRu/live'
}

irc_send(irc_config, ['Message 1', 'Message 2'])