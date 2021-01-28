#!/usr/bin/env python3
import base64
import paho.mqtt.client as mqtt


topic_num = {}

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe([("topic/seal", 0), ("topic/sa", 2)])

def _on_message(client, userdata, msg):
  if msg.payload.decode() == "Hello world!":
    print("Yes!")
    client.disconnect()

def on_message(client, obj, msg):
 # with open('/home/yicheng/python/test/new', 'wb') as fd:
    #fd.write(msg.payload)
    print(msg)
    imgdata = base64.b64decode(msg.payload)

    top = msg.topic.split('/')[-1]
    if top in topic_num:
      topic_num[top] += 1
    else:
      topic_num[top] = 0

    filename = top + str(topic_num[top]) +  '.jpg'
    with open(filename, 'wb') as f:
       f.write(imgdata)
    client.disconnect()

while(True):

  client = mqtt.Client()
  client.connect("10.121.190.108",1883,60)
  client.on_connect = on_connect
  #///////////////////////////////////////////////////
  client.on_message = on_message
  client.loop_forever()
