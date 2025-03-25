#!/usr/bin/env python

#####
#
# Python2 program to call IFTTT to trigger an Applet
#
# Use this code to directly invoke IFTTT Applets and control LIFX lighting
#
# Requires that environment variables MAKER_KEY and LIFX_APPLET be set
#
#####

__author__      = "Michael E. O'Connor"
__copyright__   = "Copyright 2018"

import os
import sys
import time
import urllib2

# Specify IFTTT supplied key from Webhooks defined as environment variable MAKER_KEY
# Obtain key from: https://ifttt.com/services/maker_webhooks/settings

try:  
    maker_key = os.environ["MAKER_KEY"]
except KeyError: 
   print "Please set the environment variable MAKER_KEY"
   sys.exit(1)

print ('MAKER_KEY is set to: ' + maker_key)

# Specify IFTTT event name as defined by environment variable LIFX_APPLET
# This will be used to identify the IFTTT Webhooks Applet to run

try:
    maker_name = os.environ["LIFX_APPLET"]
except KeyError:
   print "Please set the environment variable LIFX_APPLET to specify IFTTT Prefix"
   sys.exit(1)

print ('LIFX_APPLET is set to: ' + maker_name)

# Function calls IFTTT with the requried URL to invoke the maker applet
# Note webhooks (maker) applet needs to have name = maker_name+maker_action

def ifttt_handler (action):
  maker_event = '%s-%s' % (maker_name, action)
  url = 'https://maker.ifttt.com/trigger/%s/with/key/%s' % (maker_event, maker_key)
  f = urllib2.urlopen(url)
  response = f.read()
  f.close()
  return response

# Prompt for user input, process and loop as long as input is valid

def main():

  prompt = 'Please specify LIFX Action: (or quit)'

  maker_action = raw_input(prompt)		# Prompt for user input

  while maker_action != 'quit':
    print ('Processing event: ' + maker_action)	# Provide user status
    print ('Response: ' + ifttt_handler(maker_action))	# call handler and provide status update
    time.sleep(10)				# wait 10 seconds
    maker_action = raw_input(prompt)			# Prompt for next input

# Standard boilerplate to call the main() function.

if __name__ == '__main__':
  main()
