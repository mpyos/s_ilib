#%fetchfile --load secrets.py

# This file is where you keep secret settings, passwords, and tokens!
# If you put them in the code you risk committing that info or sharing it

secrets = {
    'hostname' : 'LOLIN S3 with ESP32S3',
    'ssid' : 'mySSID',
    'password' : 'myWIFI_Password',
    'aio_username' : 'my_adafruit_io_username',
    'aio_key' : 'my_adafruit_io_key',
    'timezone' : "Europe/Berlin", # http://worldtimeapi.org/timezone,
    'utc_diff' : 2,
    'ntp_server' : 'de.pool.ntp.org',
    'ap_ssid' : 'my_AP_SSID',
    'auth' : 'None',
    'channel' : 1
    }