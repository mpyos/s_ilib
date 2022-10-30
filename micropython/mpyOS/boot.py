# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
def boot():
    '''Webrepl active'''
    import webrepl
    webrepl.start()
boot()
