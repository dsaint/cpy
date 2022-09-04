#!/usr/bin/env python3
import datetime

with open("sensor.log", 'r', encoding='utf-8') as f:
    print("time,temp,humidty")
    for line in f:
        cols = line.rstrip().split(" ")
        print(f"{datetime.datetime.fromtimestamp(float(cols[0]))},{cols[1]},{cols[2]}")
