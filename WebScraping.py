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
pyautogui.PAUSE = 1.5
navegador.find_element('xpath','//*[@id="entrar"]').click()
pyautogui.PAUSE = 1.5
navegador.find_element('xpath','/html/body/header/div[2]/div/div[1]/button/span').click()

pyautogui.PAUSE = 1.5
navegador.find_element('xpath','//*[@id="btn10"]').click()
sleep(1)
pyautogui.press('tab')

pyautogui.press('tab')

pyautogui.press('tab')

pyautogui.press('tab')
sleep(1)
pyautogui.press('enter')

pyautogui.PAUSE = 1.5
navegador.find_element('/html/body/div[15]/div[1]/section/div[1]/div/div/div[2]/div/div/div[2]/div/button').click()




            