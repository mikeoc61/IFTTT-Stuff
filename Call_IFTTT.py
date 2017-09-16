#####
#
# Python2 program to call IFTTT dirctly and activate Applets
#
# Prompts user to specific BLINK, ALERT or CYCLE which would then
# correspond to Applets named: CHIP-ALERT, CHIP-BLINK or CHIP-CYCLE
#
# Author: Michael O'Connor
#
# Last Change: 9/14/17
#
######

import time
import urllib2

# Specify IFTTT supplied key from Webhooks
# Obtain key from: https://ifttt.com/services/maker_webhooks/settings

maker_key = 'XXXXXXXXXXXXXXXXXX'

# Function forms the required URL based on <EVENT-TYPE> corresponding to Applet Name

def ifttt_handler (event, type):
  maker_event = '%s-%s' % (event, type)
  url = 'https://maker.ifttt.com/trigger/%s/with/key/%s' % (maker_event, maker_key)
  f = urllib2.urlopen(url)
  response = f.read()
  f.close()
  return response

# Prompt for user input, process and loop as long as input is valid

def main():

  prompt = 'Please specify IFTTT event: BLINK, ALERT, CYCLE: (or quit)'

  press = raw_input(prompt)		# Prompt for user input

  while press == 'BLINK' or press == 'ALERT' or press == 'CYCLE':
    print ('Processing event: ' + press)	# Provide user status
    event = 'CHIP'			# Update event dictionary
    type = press
    print ('Response: ' + ifttt_handler(event, type))	# call handler and provide status update
    time.sleep(10)				# wait 10 seconds
    press = raw_input(prompt)			# Prompt for next input

# Standard boilerplate to call the main() function.

if __name__ == '__main__':
  main()
