# CrypTaco, v. 1.0.0
# CrypTaco Listener
# contributors: chum8
# https://github.com/chum8
# Copyright (c) 2018-2019

# import libraries
import sys, socket
from Crypto.PublicKey import RSA
#from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP #,AES

# import configuration
try:
    from cryptaco_conf import *
    host = default_host
    port = default_port
    key_file = default_key_server
except:
    print("Fatal error! Unable to import configuration file cryptaco_conf.py\nExiting.")
    sys.exit()

# default variables
capture_host = "-h"
capture_port = "-p"
capture_key = "-k"

# attempt to capture connection parameters from terminal
try:
    if (len(sys.argv) > 1):
        if capture_host in sys.argv:
            host = sys.argv[sys.argv.index(capture_host) + 1]
        if capture_port in sys.argv:
            port = sys.argv[sys.argv.index(capture_port) + 1]
        if capture_key in sys.argv:
            key_file = sys.argv[sys.argv.index(capture_key) + 1]
           
except:
    print("Could not stat connection or public key parameters.\nExiting.")
    sys.exit()

# attempt to load key
try:
    with open(key_file, 'r') as f1:
        key = RSA.importKey(f1.read())
        # print(key) # debug line

    cipher_rsa = PKCS1_OAEP.new(key)

except:
    print("Fatal error! Could not load key from file " + key_file)
    print("Make sure the file is accessible. You may need to generate a new RSA key.")
    print("Exiting.")
    sys.exit()

# attempt to create a socket connection
#try:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',int(port)))
    #s.connect((host, int(port)))
"""
except:
    print("Fatal error! Unable to bind server socket on port " + port)
    print("Exiting.")
    sys.exit()
"""
#print("Listening on " + socket.get_hostname() + " on port " + port)


# capture encrypted messages piped across tunnel
content = ''
while content != default_exit:
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by',addr)
        while True:
            data = conn.recv()
            if not data:
                break
            print(data)
    #content = s.recv()
    #print(content)
"""
    if content != default_exit:

        # attempt to encrypt the content using the key given
        try:
            data = cipher_rsa.encrypt(content.encode())
            if mask.lower() != 'mask':
                print(data)
        except:
            print("Unable to encrypt message. Try a different message or '" + default_exit + "' to exit.")

        # attempt to send string across tunnel
        try:
            s.sendall(data)
        except:
            print("There was a connection problem sending message to host at 's.sendall(data)'.  Try a different message or '" + default_exit + "' to exit.")
"""
# exit system
sys.exit()
