# Script Name		: daily_checks.py
# Author				: Levis Jani

# Description			: This script loads everything I need to carry out the daily checks for our systems.

import platform					# Load the Library Module
import os							# Load the Library Module
import subprocess				# Load the Library Module 
import sys							# Load the Library Module

from time import strftime		# Load just the strftime Module from Time

def clear_screen():								# Function to clear the screen
	if os.name == "posix":					# Unix/Linux/MacOS/BSD/etc
		os.system('clear')						# Clear the Screen
	elif os.name in ("nt", "dos", "ce"):	# DOS/Windows
		os.system('CLS')						# Clear the Screen
  
def putty_sessions():										# Function to load the putty sessions I need
  for server in open(conffilename):					# Open the file server_list.txt, loop through reading each line - 1.1 -Changed - 1.3 Changed name to use variable conffilename
    subprocess.Popen(('putty -load '+server))		# Open the PuTTY sessions - 1.1
	  
def rdp_sessions():
  print "Loading RDP Sessions:"
  subprocess.Popen("mstsc eclr.rdp")				# Open up a terminal session connection and load the euroclear session

# End of the functions			

# Start of the Main Program

filename=sys.argv[0]									# Create the variable filename
confdir = os.getenv("my_config")					# Set the variable confdir from the OS environment variable - 1.3
conffile = ('daily_checks_servers.conf')			# Set the variable conffile - 1.3
conffilename=os.path.join(confdir, conffile)	# Set the variable conffilename by joining confdir and conffile together - 1.3
clear_screen()											# Call the clear screen function
# The command below prints a little welcome message, as well as the script name, the date and time and where it was run from.
print "Good Morning " + os.getenv('USERNAME') + ", " + filename, "ran at", strftime("%Y-%m-%d %H:%M:%S"), "on",platform.node(), "run from",os.getcwd()
putty_sessions()										# Call the putty_session function
rdp_sessions()											# Call the rdp_sessions function
