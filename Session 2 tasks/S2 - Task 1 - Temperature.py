Temp = int(input("Please enter today's temperature in Celsius: "))

if Temp >= 30:
    print("It's a hot day. Stay hydrated!")
elif Temp >= 20 and Temp <= 29:
    print("It's a warm day. Enjoy the weather!")
elif Temp >= 10 and Temp <=19:
    print("It's a cool day. Wear a jacket!")
elif Temp < 10:
    print("It's a cold day. Stay warm!")
