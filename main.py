import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()

# IDENTIFICA O CAMINHO DE DIRETORIO ATUAL
dir_path = os.getcwd()

# CRIA NO CAMINHO DE DIRETORIO ATUAL UMA PASTA COM NOME PROFILE E O PERFIL NOMEADO DE = WPP
profile = os.path.join(dir_path, "profile", "wpp")

# CONFIGURAÇÕES GERAIS
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument(r"user-data-dir={}".format(profile))


# PASTA PADRÃO PARA DOWNLOAD
options.add_experimental_option("prefs", {
"download.default_directory": f"C:"
    })
driver = webdriver.Chrome(options=options)


########### PARTE 1 - ENVIAR MENSAGEM TEXTO
driver.get('https://web.whatsapp.com/send?phone=' + 'numero_telefone' + '&text=' + 'mensagem_aqui')
## DEFINE TEMPO ABERTURA WHATSAPP
driver.implicitly_wait(300)

## TEMPO GLOBAL DE ESPERA ENCONTRAR ELEMENTO
wait = WebDriverWait(driver, timeout=2)

## CAMINHO DO BOTÃO DE ENVIAR NO WHATSAPP
enviar_mensagem = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
wait.until(lambda d : enviar_mensagem.is_displayed())

## ATIVA O CLICK NO CAMINHO DO BOTÃO ENVIAR
enviar_mensagem.click()
print('Passou Parte 1')



####### PARTE 2 - ENVIAR IMAGEM
## ENCONTRA O CAMINHO DO MENU DO WHATSAPP
abrir_menu = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span')
wait.until(lambda d : abrir_menu.is_displayed())

## CLICA PARAR ABRIR O MENU DO WHATSAPP
abrir_menu.click()

## LOCALIZA SE O MENU ESTÁ ABERTO
menu_aberto = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div')
wait.until(lambda d : menu_aberto.is_displayed())

## ENCONTRA O CAMINHO DE ENVIO DA IMAGEM
abrir_imagem = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input')
wait.until(lambda d : abrir_imagem.is_enabled())

## ENCONTRA O CAMINHO DO ARQUIVO NA MAQUINA
abrir_imagem.send_keys("imagem_enviada_aqui")


##  ENCONTRA O CAMINHO DO BOTÃO ENVIAR IMAGEM E CLICA EM ENVIAR
enviar_imagem = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span')
wait.until(lambda d : enviar_imagem.is_displayed())
enviar_imagem.click()
print('Passou Parte 2')


time.sleep(5)
# mensagem_enviada = driver.find_element(By.CSS_SELECTOR, "span[aria-label*='Enviada']")
# wait.until(lambda d : mensagem_enviada.is_displayed())
print('enviada')



# FECHA O NAVEGADOR
print('Finalizando teste')
driver.quit()