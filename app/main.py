import requests
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os

# Setup Gecko/Firefox WebDriver
def webdriver_options_setup():
    option = Options()
    option.headless = True
    option.accept_insecure_certs

    return option

def webdriver_exec_setup(webdriver_name, option):

    local_path = os.getcwd()
    geckodriver_location = os.path.join(local_path, webdriver_name)

    driver = webdriver.Firefox(options=option, executable_path=geckodriver_location)

    return driver

def set_user_number(user_number='3011207447'):
    # user_number = input("Digite o número da conta contrato")
    # User infos for Checking
    #conta_contrato = '3013917131'

    return user_number

def set_url():
    # Make URL Parametes
    url = 'https://pa.equatorialenergia.com.br/'

    return url



def main():

    url = set_url()
    opcoes = webdriver_options_setup()
    driver = webdriver_exec_setup('geckodriver', opcoes)
    conta_contrato = set_user_number()

    # Driver's Actions
    driver.get(url)
    time.sleep(5)

    # Put infos client into form
    driver.find_element_by_xpath('//*[@id="contrato-payment-code"]').send_keys(conta_contrato)
    driver.find_element_by_xpath('/html/body/section[1]/header/div/div/div[3]/div/div[1]/form[2]/input[2]').click()
    time.sleep(5)

    bills = driver.find_elements_by_xpath('//*[@id="list-bills"]/tbody')
    if len(bills) <= 0:
        print('Não há contas registradas no momento')
        exit(0)

    contas = []
    identifica_fatura = 0

    for bill in bills:
        for tr in bill.find_elements_by_xpath('.//tr'):
            # print(tr.get_attribute('data-vencimento'))
            # print(tr.get_attribute('data-referencia'))
            # print(tr.get_attribute('data-bill-value'))
            # print(tr.get_attribute('data-codigo-pagamento'))
            contas.append( \
            	{ \
            		identifica_fatura: {"data-vencimento": tr.get_attribute('data-vencimento'), \
            			"mes_referencia": tr.get_attribute('data-referencia'), \
            			"valor": tr.get_attribute('data-bill-value'), \
            			"codigo_pagamento": tr.get_attribute('data-codigo-pagamento'), \
            		},
            	}, \
            )

        identifica_fatura = identifica_fatura + 1

    time.sleep(5)
    driver.quit()
    print("=======")
    print(contas)
    print()

if __name__ == '__main__':
    main()

