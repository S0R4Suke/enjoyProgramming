# -*- coding: utf-8 -*-
import requests

image = open('shibadog.jpg', 'rb')
files = {'image':('shibadog.jpg', image, 'image/jpeg')}
data = {'another_key': 'another_value'}
r = requests.post(url = "http://localhost:3000/upload",files=files,data=data)
print(r.text)
