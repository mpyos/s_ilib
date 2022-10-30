# version 0.3
# last update 7/17/22
def wifi(_debug=False):
    '''
    WIFI main modul
    need a secrets file is where you keep secret settings, passwords, and tokens!
    '''
    from secrets import secrets
    import network
    import time
    import ubinascii
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    # Access Point
    #ap_if.active(True)
    #ap_if.active(False)
    if ap_if.active():
        print('AP connected: {}'.format(ap_if.isconnected()))
        print('AP:',(ubinascii.hexlify(ap_if.config('mac'),':').decode()))
        print('Network configuration AP: ', ap_if.ifconfig())
    # client
    sta_if.active(True)
    # Client
    i=0
    while (False == sta_if.isconnected()):
        try:
            #sta_if = network.WLAN(network.STA_IF)        
            print(sta_if.isconnected())
            sta_if.connect(secrets["ssid"],secrets['password'])
            if _debug:
                 print('WIFI try counter: {}'.format(i))
            i=i+1
            if i == 2:
                #print('sta reset')
                #sta_if.active(False)
                print('WIFI disconnect')
                sta_if.disconnect()
                time.sleep_ms(1000)
                #sta_if.active(True)
                sta_if.connect(secrets["ssid"],secrets['password'])
                print('Try WIFI connect')
                time.sleep_ms(1000)
                i=0
        except:
            pass
        time.sleep_ms(500)
        
            
            
            
    print('CL:',(ubinascii.hexlify(sta_if.config('mac'),':').decode()))    
    print('Network configuration CL:', sta_if.ifconfig())
    #sta_if.active(False)

    
    #return sta_if.isconnected()
    return sta_if.ifconfig()
