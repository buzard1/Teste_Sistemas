from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Configuração do WebDriver(nesse exemplo, estamos usando o Chrome)
driver = webdriver.Chrome()

#Acessa a página de cadastro usando o caminho absoluto com protocolo file://
#Certifique-se de que o caminho está apontando para um arquivo HTML específico

driver.get("C:/Users/matheus_d_anjos/Documents/teste_sistemas/produto.html")

#Preenche o campo Nome
nome_input = driver.find_element(By.ID,"id_produto")
nome_input.send_keys("3")

#Preenche o campo CPF
cpf_input = driver.find_element(By.ID,"descricao")
cpf_input.send_keys("tenis abibas")

#Preenche o campo Endereço
endereco_input = driver.find_element(By.ID,"marca")
endereco_input.send_keys("abibas")

#Preenche o campo Telefone
telefone_input = driver.find_element(By.ID,"quantidade")
telefone_input.send_keys("5")

telefone_input = driver.find_element(By.ID,"preco")
telefone_input.send_keys("250,60")

#Clica no botão de Cadastrar
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()

#Aguarda um momento para visualiza o resultado(em uma aplicação real, você verificaria a resposta)
time.sleep(8)

#Fechar o navegador
driver.quit()