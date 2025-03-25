########
#
# Python code to connect Lambda with IFTTT Maker channel. The event is
# sent in this format: <serialNumber>-<clickType>.
#
# The following JSON template shows what is sent as the payload:
# {
#     "serialNumber": "GXXXXXXXXXXXXXXXXX",
#     "batteryVoltage": "xxmV",
#     "clickType": "SINGLE" | "DOUBLE" | "LONG"
# }
#
# A "LONG" clickType is sent if the first press lasts longer than 1.5 seconds.
# "SINGLE" and "DOUBLE" clickType payloads are sent for short clicks.
#
# For more documentation, follow the link below.
# http://docs.aws.amazon.com/iot/latest/developerguide/iot-lambda-rule.html
#
# Author: Michael O'Connor - 8/15/17
#
#########

from __future__ import print_function

import boto3
import json
import logging
import urllib2

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Specify IFTTT supplied key from IFTTT Webhooks
# Obtain unique key from: https://ifttt.com/services/maker_webhooks/settings

maker_key = 'XXXXXXXXXXXXXXXXXX'

def lambda_handler(event, context):
    logger.info('Received event: ' + json.dumps(event))
    maker_event = '%s-%s' % (event['serialNumber'], event['clickType'])
    logger.info('Maker event: ' + maker_event)
    url = 'https://maker.ifttt.com/trigger/%s/with/key/%s' % (maker_event, maker_key)
    logger.info('URL: ' + url)
    f = urllib2.urlopen(url)
    response = f.read()
    f.close()
    logger.info('Event has been sent to IFTTT Maker channel')
    return response
