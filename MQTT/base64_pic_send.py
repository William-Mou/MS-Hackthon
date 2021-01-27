#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import base64

with open("test.jpg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())


# This is the Publisher
client = mqtt.Client()
client.connect("10.121.190.108",1883,60)
#client.publish("topic/test", "Hello world!");
#f=open("/home/yicheng/python/test/test.txt")
byteArray = bytes(my_string)
client.publish("topic/test", byteArray ,0)
print(byteArray)
client.disconnect()




