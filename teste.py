
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

def document_initialised(driver):
    return driver.execute_script("return initialised")

driver = webdriver.Chrome()
aposta = ['09', '18', '21', '27','33', '56']
url = 'https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx'

driver.get(url)
tabela = driver.find_element(By.CLASS_NAME, "resultado-loteria")
sleep(10)
numero = tabela.find_element(By.TAG_NAME, 'ul').text
driver.close()
resultado = [numero[:2], numero[2:4], numero[4:6], numero[6:8], numero[8:10], numero[10:]]

acertos = 0

for  dezena in aposta:
    if dezena in resultado:
        print("{}: acertou ".format(dezena))
        acertos += 1
    else:
        print("{}: errou".format(dezena))

if acertos < 4:
    print("Perdeu, Playboy!")
elif acertos == 4:
    print('Acertou a quadra, mas não vai ganhar muito dinheiro')
elif acertos == 5:
    print('Acertou a quina, sortudo!')
else:
    print('Voce acertou todos os numeros, me empreta uma grana??')

print(resultado)
