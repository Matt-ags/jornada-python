
 
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

import pyautogui
import time

pyautogui.PAUSE = 1 # o python faz os códigos muito rápido, portanto, colocamos uma pausa (1 segundo)!

# Certo, precisamos acessar o "windows" para pesquisar o crhome, para acessar o sistema!
# Apertamos uma tecla:

# Passo 01: Abrir o sistema da empresa 
#     sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.press("win") # pressiona tecla windows

time.sleep(20) # deixei estes tempos grandes pois o pc ta lento que dói

pyautogui.write("chrome") # escreve chrome

time.sleep(20)

pyautogui.press("enter") # pressiona enter

time.sleep(50)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") # escreve o link

time.sleep(10)

pyautogui.press("enter") # pressiona enter

# pedimos pro computador esperar um pouco para carregar a página
time.sleep(30)

# Passo 02: Login (coloque qualquer coisa, estamos só simulando)

# Certo, como eu faço pro mouse ir e clicar em algum lugar da tela?
# Com o auxiliar.py, encontramos o local em que vamos colocar o mouse:
# email:
pyautogui.click(x=880, y=403) # clica no local do email (posição depende da resolução de tela)
pyautogui.write("teste@gmail.com") # escreve o email

# AO APERTAR  A TECLA TAB, VAMOS PARA O PRÓXIMO CAMPO DE ESCRITA

pyautogui.press("tab") # ir pra senha
pyautogui.write("senhalegal")

pyautogui.press("tab") # ir pro botão
pyautogui.press("enter")

# Passo 03: Importar a base de dados
# Uma das bibliotecas é a pandas

import pandas
tabela = pandas.read_csv("aula01\produtos.csv") # QUERO LER UM ARQUIVO CSV, O NOME DELE É ARQUIVOS.CSV (COMO ESTAMOS NA MESMA PASTA, NÃO PRECISA MANDAR O CAMINHO COMPLETO -> só deixa do jeito que fiz, tinha dado erro antes) 
# Tambem, guardamos a tabela em uma variável chamada "tabela"

# Passo 04: Cadastrar um produto

time.sleep(10) # esperar a página carregar

# QUEREMOS REPETIR PARA TODOS OS PRODUTOS, ENTRAMOS NO PASSO 5:

# Passo 05: Confirmar e repetir o passo 4 até cadastrar todos os produtos

# para cada liha da tabela, vamos executar isso:

# .index são as linhas da tabela, o linha é o "item da lista", podeia usar o .columns para pegar colunas!

for linha in tabela.index:

    pyautogui.click(x=801, y=290) # código do produto (clicando para colocar as informações)

    # código:

    # show, mas como vamos localizar o que queremos?
    # usamos o loc para localizar, e [linha, "codigo"] para pegar o código da linha, que é linha|coluna
    codigo = tabela.loc[linha, "codigo"] # linha e coluna
    pyautogui.write(codigo) # escreve o código do produto
    pyautogui.press("tab") # aperta a tecla tab para ir para o próximo campo

    # marca:
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca) # escreve a marca do produto
    pyautogui.press("tab") # aperta a tecla tab para ir para o próximo campo

    # tipo:
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo) # escreve o tipo do produto
    pyautogui.press("tab") # aperta a tecla tab para ir para o próximo campo

    # categoria:
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preço unitario:
    precounitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(precounitario))
    pyautogui.press("tab")

    # custo:
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # observações:
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan": # se NÃO for nulo, faz issp
        pyautogui.write(obs)
        
    pyautogui.press("tab")

    # enviar:
    pyautogui.press("enter")

    # vamos voltar pro inicio da tela para cadastrar o próximo produto
    # scroll negativo => para baixo
    # scroll positivo => para cima
    pyautogui.scroll(1000)

    # ATÉ AQUI
