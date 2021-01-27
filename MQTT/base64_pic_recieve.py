#!/usr/bin/env python3
import base64
import paho.mqtt.client as mqtt

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/image")

def _on_message(client, userdata, msg):
  if msg.payload.decode() == "Hello world!":
    print("Yes!")
    client.disconnect()

def on_message(client, obj, msg):
 # with open('/home/yicheng/python/test/new', 'wb') as fd:
    #fd.write(msg.payload)
    imgdata = base64.b64decode(msg.payload)
    filename = 'some_image.jpg'
    with open(filename, 'wb') as f:
       f.write(imgdata)
    client.disconnect()


client = mqtt.Client()
client.connect("10.121.190.108",1883,60)
client.on_connect = on_connect
#///////////////////////////////////////////////////
client.on_message = on_message
client.loop_forever()
