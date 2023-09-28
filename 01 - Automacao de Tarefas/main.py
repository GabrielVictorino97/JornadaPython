import pyautogui
import time
import pandas

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> atalho (combinação de teclas)

pyautogui.PAUSE = 0.3

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=605, y=59)
time.sleep(2)
pyautogui.hotkey('ctrl', 'a')
# pyautogui.click(x=785, y=595) abrir perfil chrome
url = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(url)
pyautogui.press("enter")

time.sleep(3)
pyautogui.click(x=799, y=400) 
pyautogui.write("email.com")

pyautogui.press("tab")
pyautogui.write("senha")

pyautogui.click(x=985, y=562) #login
time.sleep(3)

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:

# preencher campos
    pyautogui.click(x=816, y=320)
    
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
        
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(10000)