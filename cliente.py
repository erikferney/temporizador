from temporizador import *
from time import sleep

hora = 0
minuto = 1
segundo = 0

tempo = Temporizador()
tempo.iniciar([hora, minuto, segundo])

for ln in range(60*minuto):
	tempo.retroceder()
	#sleep(0.5)