import pyautogui as cursor
from selenium import webdriver
from time import sleep

#Através das coordenadas do mouse, move o mouse para o campo de pesquisa
cursor.moveTo(x=270, y=755, duration=0.1)
cursor.click()
sleep(4)

#Abre o Spotify
cursor.write("Spotify")
cursor.press("enter")
sleep(3)

#Vai até o local de pesquisa do app e busca por Iron Maiden
cursor.moveTo(x=72, y=107, duration=0.1)
cursor.click()
cursor.write("Iron Maiden")
sleep(2)

#Entra no perfil do artista
cursor.moveTo(x=349, y=194, duration=0.1)
cursor.click()
sleep(2)

#Move o mouse até a barra de rolagem
cursor.moveTo(x=1087, y=86, duration=0.1)
sleep(2)

#Desce a barra até entrar nas discografias do artista
cursor.dragTo(1087, 200, 2, button='left')
cursor.moveTo(x=982, y=383, duration=0.1)
cursor.click()

#busca pelo album 'Peace of Mine' e entra
cursor.moveTo(x=1087, y=99, duration=0.1)
sleep(2)
cursor.dragTo(1085, 525, 2, button='left')
sleep(2)
cursor.moveTo(x=668, y=409, duration=0.1)
cursor.click()

#Faz a rolagem do mouse até a música desejada e dá play
cursor.moveTo(x=1089, y=145, duration=0.1)
sleep(2)
cursor.dragTo(1089, 395, 2, button='left')
sleep(2)
cursor.moveTo(x=293, y=340, duration=0.1)
cursor.click()

#Print da tela
sleep(3)
cursor.press("PrtSc")

#Abre o Paint e cola o print
cursor.moveTo(x=166, y=745, duration=0.1)
cursor.click()
cursor.write("Paint")
sleep(1)
cursor.press("enter")
sleep(3)
cursor.moveTo(x=33, y=75, duration=0.1)
cursor.click()
sleep(5)

#Fecha Paint
cursor.moveTo(x=1350, y=20, duration=0.1)
cursor.click()