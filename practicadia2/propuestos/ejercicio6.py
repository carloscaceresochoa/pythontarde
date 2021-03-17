segundos=int(input("digite numero de segundos\n"))
hora,minuto=segundos//3600,(segundos%3600)//60
print(hora,"hora",minuto,"minutos")