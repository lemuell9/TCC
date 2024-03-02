# Importando as bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep
import pyautogui
Options = Options()
Options.headless = False

navegador = webdriver.Firefox(options=Options)
link = "https://sas.sebrae.com.br/"
navegador.get(url=link)
sleep(1)
navegador.get("https://sas.sebrae.com.br/")

navegador.find_element('xpath','//*[@id="Usuario"]').send_keys("pa-sebrae\se.lemuelcarvalho")

navegador.find_element('xpath','//*[@id="Senha"]').send_keys("@Ifpa1997")
pyautogui.PAUSE = 0.5
navegador.find_element('xpath','//*[@id="entrar"]').click()
pyautogui.PAUSE = 0.5
navegador.find_element('xpath','/html/body/header/div[2]/div/div[1]/button/span').click()

pyautogui.PAUSE = 0.5
#Fazendo o click no botao de interação.
botaointeração = navegador.find_element('xpath','//*[@id="btn10"]').click()
sleep(1)
#Fazedo o click no bota pesquisa
botaopesquisa = navegador.find_element('xpath','/html/body/div[5]/div/div/div[2]/nav/ul/li[3]/ul/li[1]/a').click()
# Escolhendo o perido da pesquisa no sistema SAS.

sleep(1)
pyautogui.press('enter')
sleep(1)
navegador.find_element('xpath','//*[@id="txtPeriodoInicio"]').click()
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
navegador.find_element('xpath','//*[@id="txtPeriodoInicio"]').send_keys("01/01/2023")
sleep(1)
navegador.find_element('xpath','//*[@id="txtPeriodoFim"]').click()
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
sleep(1)

navegador.find_element('xpath','//*[@id="txtPeriodoFim"]').send_keys("31/12/2023")
sleep(1)
navegador.find_element('xpath','/html/body/div[2]/div[2]/a[1]').click()
sleep(1)

navegador.find_element('xpath','/html/body/div[15]/div[1]/section/div[1]/div/div/div[2]/div/div/div[2]/div/button').click()
