from selenium import webdriver
from selenium .webdriver.common.keys import Keys
from time import sleep

#Abre o Google Chrome
navegador = webdriver.Chrome()

#Insere a URL
navegador.get("https://www.verdemaratevoce.com.br/")

#Delay p/ aparecer botão
sleep(10)

#Fecha Anúncio
fechar_anuncio = navegador.find_element_by_xpath('//*[@id="largeModal"]/div/div/div[3]/button').click()

# Faz a busca e dá enter
buscar_elemento = navegador.find_element_by_id('inputBuscaRapida').send_keys(("Cerveja Heineken"),(Keys.RETURN))
sleep(3)

#Abre o produto desejado
abre_elemento = navegador.find_element_by_xpath('/html/body/app-root/app-produto-busca/div/div/div[1]/div/div[3]/app-produto-card/div/div/app-produto-imagem/a/div/img').click()
sleep(3)

#Procura a tag do preço e printa no console
preco = navegador.find_element_by_xpath('//*[@id="product"]/div/app-tag-preco/div/div[2]').text
print("[Preço] Cerveja Heineken Long Neck 330 Ml - " '\n' + preco)

#Fecha o navegador
navegador.quit()






