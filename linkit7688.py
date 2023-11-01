import serial
import requests

port = serial.Serial('/dev/ttyS0', baudrate=9600, timeout=1)
while True:
    data = port.readline().decode().strip()
    if data:
        parts = data.split(',')
        temperature = parts[0]
        humidity = parts[1]
        url = 'http://localhost:8000/temperature/?id=linkit1&temp=' + temperature + '&humi=' + humidity
        response = requests.get(url, verify=False)
