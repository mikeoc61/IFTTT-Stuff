#!/usr/bin/env python

#####
#
# Python2 program to call IFTTT to trigger an Applet
# Uses the same event dictionary format sent by an AWS IoT Button
#
# Use this code to directly invoke IFTTT Applets and simulate Button Presses
#
# Requires that environment variables MAKER_KEY BUTTON_SN be defined and set
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

# Define event dictionary to simulate AWS IoT Button
#   batteryVoltage is unused
#   serialNumber corresponds to a specific IoT Device (and Webhooks applet name)
#   clickType corresponds to type of button press (and Webhooks applet name)

event = {
    "batteryVoltage": "1707mV",
    "serialNumber": "<UNIQUE SN of AWS Iot Button>",
    "clickType": "<SINGLE, DOUBLE or LONG>"
}

# Specify IFTTT event name as defined by environment variable BUTTON_SN
# This will be used to identify the IFTTT Webhooks Applet to run

try:
    event['serialNumber'] = os.environ["BUTTON_SN"]
except KeyError:
   print "Please set the environment variable BUTTON_SN to specify IFTTT Applet"
   sys.exit(1)

print ('BUTTON_SN is set to: ' + event['serialNumber'])

# Function to emulate AWS IFTTT Lambda function invoked when IoT button is pressed
# Function forms the required URL based on button S/N and clickType
# and calls IFTTT with the requried URL to invoke the maker applet
# Note webhooks (maker) applet needs to have name = <serialNumber>-<clickType>

def ifttt_handler (event):
  maker_event = '%s-%s' % (event['serialNumber'], event['clickType'])
  url = 'https://maker.ifttt.com/trigger/%s/with/key/%s' % (maker_event, maker_key)
  f = urllib2.urlopen(url)
  response = f.read()
  f.close()
  return response

# Prompt for user input, process and loop as long as input is valid

def main():

  prompt = 'Please specify: SINGLE, DOUBLE, LONG: (or quit)'

  press = raw_input(prompt)		# Prompt for user input

  while press == 'SINGLE' or press == 'DOUBLE' or press == 'LONG':
    print ('Processing event: ' + press)	# Provide user status
    event['clickType'] = press			# Update event dictionary
    print ('Response: ' + ifttt_handler(event))	# call handler and provide status update
    time.sleep(10)				# wait 10 seconds
    press = raw_input(prompt)			# Prompt for next input

# Standard boilerplate to call the main() function.

if __name__ == '__main__':
  main()
