# -*- coding:utf-8 -*-

while True:
    try:
        weight = float(input("体重(kg)は？"))
        height = float(input("身長(cm)は？"))
        height = height / 100 # cm to m
        bmi = weight / (height ** 2)
        break
    except:
        print("入力ミスがあります。再度入力して下さい。")

result = ""
if bmi < 18.5:
    result = "痩せ型"
elif bmi < 25:
    result = "標準体型"
elif bmi < 30:
    result = "肥満(軽)"
else:
    result = "肥満(重)"

print("BMI: ", bmi)
print("判定", result)
