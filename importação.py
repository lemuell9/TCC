# Importando biblioteca
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep
#abrindo o navegador
navegador = webdriver.Firefox()

navegador.get("https://sas.sebrae.com.br/")
navegador.find_element_by_xpath('//*[@id="entrar"]').click()
time.sleep(1)

