# CrypTaco, v. 1.0.0
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
    key_file = default_key
    mask = default_mask
except:
    print("Fatal error! Unable to import configuration file cryptaco_conf.py\nExiting.")
    sys.exit()

# default variables
capture_host = "-h"
capture_port = "-p"
capture_key = "-k"
capture_mask = "-m"

# attempt to capture connection parameters from terminal
try:
    if (len(sys.argv) > 1):
        if capture_host in sys.argv:
            host = sys.argv[sys.argv.index(capture_host) + 1]
        if capture_port in sys.argv:
            port = sys.argv[sys.argv.index(capture_port) + 1]
        if capture_key in sys.argv:
            key_file = sys.argv[sys.argv.index(capture_key) + 1]
        if capture_mask in sys.argv:
            mask = sys.argv[sys.argv.index(capture_mask) + 1]
           
except:
    print("Could not stat connection or public key parameters.\nExiting.")
    sys.exit()

# welcome users to CrypTaco
print("Welcome to CrypTaco!")
print("Copyright (c) 2018-2019, chum8.")
print("Clone https://github.com/chum8/cryptaco for the most up to date version.")
print("\nYou can launch CrypTaco with custom parameters from command line:")
print("python3 cryptaco.py -h <host> -p <port> -k <public key file>\n")
print("Add the following option if you don't want to display encryption results in your terminal window")
print("-m mask")

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
print("Attempting to connect to " + host + " on port " + port)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
except:
    print("\nFatal error! Unable to connect to " + host + " on port " + port)
    print("Make sure your host machine is listening.")
    print("\tnc -nvlp " + port)
    print("\t\tor")
    print("\tpy cryptacolisten.py")
    print("You may also need to supply the correct IP address in cryptaco_conf.py.")
    print("Exiting.")
    sys.exit()

print("Success. Connected to " + host + " on port " + port)
print("CTRL-C or '" + default_exit + "' to exit.")


# capture user input, encrypt, and pipe across tunnel
content = ''
while content != default_exit:
    content = str(input())

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

# exit system
s.close()
sys.exit()
