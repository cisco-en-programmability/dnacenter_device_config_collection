#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Copyright (c) 2021 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Gabriel Zapodeanu TME, ENB"
__email__ = "gzapodea@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2021 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


import urllib3
import datetime
import json
import time
import logging
import dnacentersdk
import os

from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings
from requests.auth import HTTPBasicAuth  # for Basic Auth

from config import DNAC_URL, DNAC_PASS, DNAC_USER
from dnacentersdk import DNACenterAPI
from config import FOLDER_NAME

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings

DNAC_AUTH = HTTPBasicAuth(DNAC_USER, DNAC_PASS)


def main():
    """
    This application will:
     - create an inventory of all devices managed by Cisco DNA Center
     - collect the running configuration for each device
     - save each configuration in a file using the name {device_hostname + time when config saved}
    """

    # logging, debug level, to file {application_run.log}
    logging.basicConfig(
        filename='application_run.log',
        level=logging.DEBUG,
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

    current_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print('\n"device_config_collection.py" App Run Start, ', current_time)

    # Create a DNACenterAPI "Connection Object"
    dnac_api = DNACenterAPI(username=DNAC_USER, password=DNAC_PASS, base_url=DNAC_URL, version='2.1.2', verify=False)

    # find the Cisco DNA Center device count
    devices_count = dnac_api.devices.get_device_count()['response']
    print('\nThe number of devices managed by Cisco DNA Center is:', devices_count)

    # collect the device info for all devices managed by Cisco DNA Center
    devices_list = []
    remaining_device_count = devices_count
    device_offset = 1
    device_limit = 500
    while remaining_device_count > 0:
        device_info = dnac_api.devices.get_device_list(offset=device_offset,limit=device_limit)
        devices_list.extend(device_info['response'])
        device_offset += device_limit
        remaining_device_count -= device_limit

    # create a folder to save the reports to
    if not os.path.exists(FOLDER_NAME):
        os.makedirs(FOLDER_NAME)

    # collect device config and save to file
    for device in devices_list:
        device_hostname = device['hostname']
        device_id = device['id']

        filename = FOLDER_NAME + '/' + device_hostname
        try:
            config_str = dnac_api.devices.get_device_config_by_id(device_id)['response']
            with open(filename, 'w') as filehandle:
                filehandle.write('%s\n' % config_str)
        except:
            pass

    current_time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print('\n"device_config_collection.py" App Run End, ', current_time)


if __name__ == '__main__':
    main()
