temperature = float(input("Enter Farenheit:"))
print("The Farenheit is: " + str(temperature))
c = (temperature - 32) * 5/9
print("The Celsius is: ", end=" ")
print(c)



temp = input("Enter Celsius:")
print("The Celsius is: " + temp)
temp = float(temp)
f = (temp * 9/5) + 32
print("The Farenheit is: ", end=" ")
print(f)
