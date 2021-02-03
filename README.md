
# Cisco DNA Center Device Configuration Collection

This application will collect the configurations for all the devices managed by Cisco DNA Center.
The configuration for each device will be saved in a file.

It will create a report with the hostname and platform id for these devices

**Cisco Products & Services:**

- Cisco DNA Center
- Cisco network devices managed by Cisco DNA Center

**Tools & Frameworks:**

- Python environment to run the application
- Cisco DNA Center Python SDK - https://github.com/cisco-en-programmability/dnacentersdk

**Usage**

This application will:
- create an inventory of all devices managed by Cisco DNA Center
- verify if folder exists, or create the folder to save the device configuration files to
- collect the running configuration for each device
- save each configuration to a file using the name {device_hostname}, in the folder {FOLDER_NAME}

Sample Output:

```

"device_config_collection.py" App Run Start,  2021-02-02 17:07:50

The number of devices managed by Cisco DNA Center is: 11
Saved configuration file with the name:  device_configs/C9800-CL
Saved configuration file with the name:  device_configs/NYC-ACCESS
Saved configuration file with the name:  device_configs/NYC-RO
Saved configuration file with the name:  device_configs/PDX-ACCESS
Saved configuration file with the name:  device_configs/PDX-CORE1
Saved configuration file with the name:  device_configs/PDX-CORE2
Saved configuration file with the name:  device_configs/PDX-M
Saved configuration file with the name:  device_configs/PDX-RN
Saved configuration file with the name:  device_configs/PDX-RO
Saved configuration file with the name:  device_configs/SP

"device_config_collection.py" App Run End,  2021-02-02 17:07:53

Process finished with exit code 0

```
 
This sample code is for proof of concepts and labs

**License**

This project is licensed to you under the terms of the [Cisco Sample Code License](./LICENSE).


