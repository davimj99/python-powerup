import pyautogui
import time


## pyautogui.click -> clicar em algum lugar
## pyautogui.press -> apertar 1 tecla
## pyautogui.write -> escrever 1 texto
pyautogui.PAUSE = 0.5  #função para as pausas dos funções pyautoguAngela Maiarai

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
pyautogui.click(x=1314, y=474)               #(x=1024, y=432)
pyautogui.press("entrar")
time.sleep(3)

pyautogui.click(x=886, y=318)                  #(x=653, y=289)
pyautogui.press("Funcionario")


pyautogui.click(x=265, y=501)                                #(x=531, y=493)
pyautogui.press("Requerimento")
pyautogui.scroll(-200) #rola a pagina pra baixo com o mouse nº positivo pra cima e negativo pra baixo
time.sleep(1.5)

pyautogui.click(x=1859, y=417)  #(x=1117, y=418)
pyautogui.press("Tipo")


pyautogui.click(x=1526, y=525)                    #(x=1110, y=96)
pyautogui.press("Declaração de Escolaridade")
time.sleep(1.5)

pyautogui.click(x=157, y=419)            #(x=175, y=413)
pyautogui.press("Situação")

pyautogui.click(x=235, y=699)                     #(x=121, y=343)
pyautogui.press("Novo-inicio")
time.sleep(2)



pyautogui.click(x=972, y=515)                     #(x=671, y=526)
pyautogui.press("Consultar")
pyautogui.scroll(-300)

