import socket


class BotDetector:

    bots = [
        'googlebot.com',
        'search.msn.com',
        'yandex.com',
        'yasni.de',
    ]
    

    def __init__(self, port=80, timeout=0.1):

        self.port = port

        # Set socket timeout
        if hasattr(socket, 'setdefaulttimeout'):
            socket.setdefaulttimeout(timeout)

    def verified_reverse(self, ip):

        # Convert mapped IPv4 
        if ip[:7] == '::ffff:' and '.' in ip:
            ip = ip[7:]
        
        try:
            reverse = socket.getnameinfo((ip, self.port), 0)[0]
        except:
            return None

        try:
            ai = socket.getaddrinfo(reverse, self.port)
        except:
            return None

        for addr in ai:
            forward = addr[4][0]

            if ip == forward:
                return reverse

        return None

    def bot(self, ip):

        reverse = self.verified_reverse(ip)
        if reverse is None:
            return None

        reverse = reverse.rstrip('.')

        for bot in self.bots:
            if reverse.endswith(bot):
                return bot

        return None
