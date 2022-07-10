#this is a work in progress, A list of things that you can do are on the other page.
from playsound import playsound
import random
import datetime
z = datetime.datetime.now()
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
from time import sleep
import datetime
import webbrowser
jokes = 10
 #stardust = 10
question = input("Contraseña:  ")
#Welcome = 10
if question == "11052009Th":
#Welcome -= 1
    print ('Bienvenido Señor')
else:
    print ("Contraseña Incorrecta")
    raise SystemExit
sleep(0.5)
print ("Conectando a la base de datos Stark Industries")
print("-------------------------------------------")
sleep(2)
print ("Conexion segura establesida")
sleep(1)
def question():
  x = input("Como lo puedo ayudar señor?:  ")
  #Task = 10
  if x == "abre spotify":
    #Task -= 1
    print("-------------------------------------------")
    print("ok")
    webbrowser.open_new_tab('https://open.spotify.com/')
    sleep(1)
    print("Abierto")
    print("-------------------------------------------")
  if x == "clima":
    print("-------------------------------------------")
    print("Deja que te muestre")
    webbrowser.open_new_tab('https://www.bbc.co.uk/weather')
    print("-------------------------------------------")
  if x =="tiempo":
   print("-------------------------------------------")
   print("Tiempo =", current_time)
   print("-------------------------------------------")
  if x =="fecha":
    print("-------------------------------------------")
    print ("Fecha actual")
    print (now.strftime("%d-%m-%y"))
    print("-------------------------------------------")
  if x =="que significa jarvis":
    print("-------------------------------------------")
    print("Jarvis significa simplemente un sistema bastante inteligente")
    print("-------------------------------------------")
  if x =="tengo hambre":
    print("-------------------------------------------")
    print("ok")
    webbrowser.open_new_tab('https://www.pedidosya.com.ar')
    print("-------------------------------------------")
  if x =="abre gmail":
    print("-------------------------------------------")
    e=input("¿Qué correo electrónico? ¿Gmail o Outlook?   ")
    if e =="gmail":
      print("Ok, abriendo Gmail")
      webbrowser.open_new_tab('https://mail.google.com/mail/u/0/')
      print("-------------------------------------------")
    else:
      print("Ok, abriendo Outlook")
      webbrowser.open_new_tab('https://outlook.live.com/owa/')
      print("-------------------------------------------")
  if x=="abre google":
    webbrowser.open_new_tab
    ('https://www.google.com/')
  if x=="musica":
    print("el comando no funciona")
    playsound('Summer Nights - LiQWYD (Music promoted by Audio Library).mp3')
    
    

for i in range (1,999):
 question()
