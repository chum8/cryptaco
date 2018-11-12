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
    with open(key_file, 'rb') as f1:
        key = RSA.importKey(f1.read())
        # print(key) # debug line

    cipher_rsa = PKCS1_OAEP.new(key)

except:
    print("Fatal error! Could not load key from file " + key_file)
    print("Make sure the file is accessible. You may need to generate a new RSA key.")
    print("Exiting.")
    sys.exit()

# attempt to create a socket connection
try:
    print("Listening on " + host + ":" + port + " ...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,int(port)))
    s.listen(1)
    conn, addr = s.accept()
except:
    print("Fatal error! Unable to bind server socket on port " + port)
    print("Exiting.")
    sys.exit()
    
print("Connected by",addr)

data = ''
# capture encrypted messages piped across tunnel
with conn:
    while str(data) != default_exit:
        data = conn.recv(4096)
        if len(data) > 0:
            print(data)

            # attempt to decrypt the content using the key given
            try:
                data = cipher_rsa.decrypt(data).decode()
                print('\n%s\n'%data)
            except:
                print("Unable to decrypt message using key " + key_file + ". Make sure you are using the right public/private combination to encrypt and decrypt.")

# exit system
s.close()
print("Connection closed.")
sys.exit()
