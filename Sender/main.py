from machine import Pin  # import for light
from time import sleep  # import for timer
import network  # import for connect to router
import urequests  # import for form a request

led = Pin(2, Pin.OUT)  #  assign variable led light bulb

def do_connect():
    led.on()  # power on pin. VALUE OFF = ON
    sta_if = network.WLAN(network.STA_IF)  # assign variable interface station, when esp work with router // be 2
    # mode interface
    if not sta_if.isconnected(): # that is if sta_if == False
        print("connecting to network...")
        sta_if.active(True)  # power off mode interfaces for connect
        sta_if.connect("Aspirant", "#aspirant_love_all_esp")  # connect to router
        while not sta_if.isconnected(): # if not connect, function be restart. If indicate light will be shine,
            # means problem with connect to router
            pass
    print("network config:", sta_if.ifconfig())  # print ip address
    led.off()  # power off light bulb


do_connect()  # start function



while True:
    try:  # if be problem, will print error in usb. And begin complete cycle// if not try, on error cycle will be break
        sleep(2)  # timer on 5 second
        led.on()  # power off pin(light bulb)
        print("Sending data")
        response = urequests.get(  # form a request
            'http://192.168.1.8/index.py?local="Success_from_esp"'
        )
        response.close()  # close response
        led.off()  # off light bulb
    except OSError as e:  # elif will be error. Cycle not will be break, cycle print error. And be complete next
        for x in range 4:
            led.off()
            led.on()
            sleep(1)