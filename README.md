# cryptaco
Send encrypted message across a network tunnel
CrypTaco

Send coded messages (“talk”) across a socket connection!  Plaintext entered on the client machine is received as encoded text on the host terminal.

Future improvements to be made: the encoded text is received as gibberish rather than human-readable bytes. 

Instructions

Fire up a host and client machine

On the client machine, clone into 	https://github.com/chum8/cryptaco

On the host machine, begin listening on port 8080 (or some other port)

	nc -nvlp 8080

Performing the remaining steps on the client machine.

By default, cryptaco will attempt to resolve the host at address 192.168.135.1 on port 8080, encrypting with a key from the file cryptaco.pub.  To run cryptaco with default settings, issue the command
	
	python3 cryptaco.py

You can change the defaults using this format
	
	python3 cryptaco.py -h <host> -p <port> -k <keyfile>
		e.g.
	python3 cryptaco.py -h 10.0.0.5 -p 8989 -k mykey.pub

You can also add the following option to prevent cryptaco from displaying the message in encrypted form on the client terminal.
	
	-m mask
  
  After cryptaco loads, type messages and strike ENTER.  
  Messages are encrypted before being sent across to the host machine.
  You will see the encrypted message on the host machine.
