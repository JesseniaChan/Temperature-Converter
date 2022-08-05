temperature = input("celsius or farenheiht?")
degree = eval(input("how many degrees?"))
if temperature == "celsius":
  print("farenheit is: ", (degree * 1.8)+ 32)
elif temperature == "farenheit":
  print("celsius is: ", (degree - 32 ) / 1.8)
