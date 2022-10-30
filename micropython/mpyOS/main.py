#%fetchfile --load main.py
#import machine
#machine.freq(240000000)

def sysinfo():
    
    import sys
    try:
        exec(open('/ilib/systeminfo.py').read(),globals())
    except Exception as e:
        print(e)
    return

def ipinfo():
    try:
        #exec(open('ipconfig.py').read(),globals())
        exec(open('/ilib/ipconfig-micropython.py').read(),globals())
    except Exception as e:
        print(e)
    return

def mreset():
    '''machine reset'''
    import machine
    machine.reset()
    return

def gc_clear():
    '''Run a garbage collection'''
    import gc
    gc.collect()
    return

def wifi_start():
    '''Start WIFI Client Network'''
    import wifi
    wifi.wifi()
    return

def wifi_stop():
    '''Stop WIFI Client Network'''
    import network
    try:
        sta_if = network.WLAN(network.STA_IF)
        sta_if.disconnect()
    except Exception as e:
        print(e)
    return

def wifi_active():
    '''Enable WIFI Network'''
    import network
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    return

def wifi_inactive():
    '''Disable WIFI Network'''
    import network
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(False)
    return

def wifi_ap_active():
    '''Enable WIFI Accesspoint'''
    import network
    ap = network.WLAN(network.AP_IF)
    ap.active(True) 
    return

def wifi_ap_inactive():
    '''Disable WIFI Access Point'''
    import network
    ap = network.WLAN(network.AP_IF)
    ap.active(False) 
    return

def wifi_ap_start():
    '''Start WIFI Access Point'''
    import network
    ap = network.WLAN(network.AP_IF)
    ap.active(True)         
    
    return

def wifi_ap_stop():
    '''Stop WIFI Access Point'''
    import network
    try:
        ap = network.WLAN(network.AP_IF)
        ap.disconnect()
    except Exception as e:
        print(e)
    return




#sysinfo()
### WIFI ###
#wifi_inactive()
#wifi_stop()
wifi_active()
wifi_start()

### WIFI AP ###
wifi_ap_inactive()
#wifi_ap_active()
#wifi_ap_stop()
#wifi_ap_start()
# test
ipinfo()
import go2m_os_hw
root=go2m_os_hw.whatisroot()
if root == '':
    print('root is empty')
else:
    print('root is {}'.format(root))

print('main finsh')
#import ccp
#import sccp