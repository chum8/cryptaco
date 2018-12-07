# cryptaco
Send encrypted message across a network tunnel
CrypTaco
# IMPORTANT NOTE
On my machine, I have aliased the command
```bash
	python3
```
to
```
	py
```
You may have to replace 'py' with 'python3' in the below examples to get the code to work.

# What CrypTaco does

Send coded messages (“talk”) across a socket connection!  Plaintext entered on the client machine is received as encoded text on the host terminal.  If using the Cryptaco Listener Helper, host terminal also decodes text.

# Install
You will need a host and client machine, or host and client tabs in a single Linux terminal.  Clone into the repository.
```bash
	git clone https://github.com/chum8/cryptaco.git
```
(If using separate machines, do this step on both machines.)

# Configure
Edit the cryptaco_conf.py configuration file to set defaults.
```bash
	vi cryptaco_conf.py
```
Make sure the port and host IP settings are correct for your machine.
```bash
	default_host = <IP address of your host machine>
	default_port = <some port>
```
Leave the key pair settings as they are to use the key pair included in the distribution, or modify them if using your own key pair.

# Run

Fire up a host and client machine and open terminal windows on those machine, or open two tabs in a Linux terminal.

# 1) On host machine

If you want to receive messages in encrypted form, simply begin listening on some port
```bash
	nc -nvlp 8080
```
If you want the Cryptaco Listener Helper to decrypt the messages, issue the following command
```bash
	py cryptacolisten.py
```

# 2) On client machine
To run cryptaco with the default settings, issue
```bash
	py cryptaco.py
```
You can change the defaults using this format
```bash	
	py cryptaco.py -h <host> -p <port> -k <keyfile>
		e.g.
	py cryptaco.py -h 10.0.0.5 -p 8989 -k mykey.pub
```
You can also add the following option to prevent cryptaco from displaying the message in encrypted form on the client terminal.
```bash	
	-m mask
```  
After cryptaco loads, type messages and strike ENTER.  
Messages are encrypted before being sent across to the host machine.
You will see the encrypted message on the host machine.  If you are using cryptacolisten.py, you will also see the decrypted message.
