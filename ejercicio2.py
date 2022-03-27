import pyfirmata

puerto = "\\.\COM4"
led = (13)
led2 = (11)
boton = (2)

tarjeta = pyfirmata.Arduino(puerto)
       
letra = input("Ingrese una letra:")
if(letra == "A"):
    tarjeta.digital[led].write(1)
    tarjeta.digital[led2].write(1)
elif(letra == "Y"):
    tarjeta.digital[led].write(1)
    tarjeta.digital[led2].write(1)
else:
    print("Letra incorrecta")