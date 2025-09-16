import pyautogui
import time


## pyautogui.click -> clicar em algum lugar
## pyautogui.press -> apertar 1 tecla
## pyautogui.write -> escrever 1 texto
pyautogui.PAUSE = 0.5  #função para as pausas dos funções pyautogui

#Passo 1: Entrar no sistema da empresa: - https://dlp.hashtagtreinamentos.com/python/intensivao/login
#abrir o crhome  

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.press("perfil David")

#digitar o site
pyautogui.write("https://sei.iscon.edu.br/index.xhtml")
pyautogui.press("enter")
time.sleep(3)  #função pra garantir o site abrir 

#Passo 2: fazer login
pyautogui.click(x=1314, y=474)            #(x=1024, y=432)
pyautogui.press("entrar")
time.sleep(3)

pyautogui.click(x=886, y=318)            #(x=653, y=289)
pyautogui.press("Funcionario")


pyautogui.click(x=729, y=399)          #(x=287, y=437)
pyautogui.press("Impressão de declaração")

pyautogui.click(x=921, y=234)            #(x=643, y=240)
pyautogui.press("Lupa de pesquisa")

#pyautogui.write("Angela Maiara")
pyautogui.write("Geovanna Gabriela de Jesus Souza")

pyautogui.click(x=1514, y=246)                           #(x=1057, y=218)
pyautogui.press("Consultar")
time.sleep(2)

pyautogui.click(x=1615, y=325)         #(x=1137, y=286)
pyautogui.press("Selecionar")

pyautogui.click(x=1160, y=356)        #(x=1046, y=349)
pyautogui.press("Texto Padrão pra declarção")
pyautogui.click(x=1126, y=437)         #(x=807, y=427)
pyautogui.press("DECLARAÇÃO.2025.2")
time.sleep(1.5)

pyautogui.click(x=857, y=1002)        #(x=580, y=670)
pyautogui.press("imprimir")

pyautogui.click(x=610, y=438)         #(x=461, y=374)
pyautogui.press("GERAR RELATORIO (PDF) ")
time.sleep(5)


#pyautogui.press("enter")
pyautogui.hotkey("ctrl", "a")
pyautogui.press("Backspace")


#pyautogui.write("Angela Maiara")
pyautogui.write("Geovanna Gabriela de Jesus Souza")
time.sleep(2)


pyautogui.press("enter")
time.sleep(1.5)

pyautogui.click(x=1041, y=1051)          #(x=917, y=755)
pyautogui.press("Explorador de Arquivos")
time.sleep(2)

pyautogui.click(x=498, y=176)           #(x=497, y=199)
pyautogui.press("enter")
time.sleep(2)

pyautogui.click(x=140, y=11)           #(x=186, y=22)
time.sleep(2)

#Passo 3: Importar a base de dados
#Passo 4: Cadastrar 1 produto
#Passo 5: Repetir para todos os produtos 

#pyautogui > fazer automações com python 
