import json
import requests

url = 'https://covid19.th-stat.com/api/open/today'

r = requests.get(url)
data = r.json()

print("\n")
print("-" *50)

print("{:^50}".format("| รายงายสถานการณ์ Covid-19 |"))

print("\n")

print("ผู้ติดเชื้อรายใหม่ : {:10}".format(data['NewConfirmed']))
print("ผู้ติดเชื้อสะสม : {:12}".format(data['Confirmed']))
print("หายป่วยแล้ว : {:13}".format(data['Recovered']))
print("เสียชีวิตสะสม : {:12}".format(data['Deaths']))
print("ผู้ป่วยรักษาอยู่ : {:12}".format(data['Hospitalized']))
print("อัพเดทล่าสุด : {:10}".format(data["UpdateDate"]))

print("-" *50)
print("\n")
