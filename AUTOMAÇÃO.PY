#Importando as bibliotecas
import pyautogui
from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep
# Abrindo a pagina do sistama SAS do Sebrae
#pyautogui.alert("o codigo vai comer.Aperte enter para continuar")
pyautogui.PAUSE = 1.5
pyautogui.press('winleft')
pyautogui.write('firefox')
pyautogui.press('enter')
pyautogui.write('https://sas.sebrae.com.br/')
pyautogui.PAUSE = 1.5
pyautogui.press('enter')
#time.sleep(1)
#navegador = webdriver.Firefox()
pyautogui.write('https://sas.sebrae.com.br/')
pyautogui.PAUSE = 2.5
pyautogui.press('enter')
#navegador.get("https://sas.sebrae.com.br/")
#navegador.find_element_by_xpath('//*[@id="entrar"]').click()
#pyautogui.PAUSE = 1.5



