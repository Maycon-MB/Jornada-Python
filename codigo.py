import pyautogui
import time
import pandas as pd
# Passo a passo do projeto

# Passo 1 - Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# apertar teclas de atalho -> pyautogui.hotkey  exemplo: pyautogui.hotkey("ctrl", "C")
# intervalo em cada comando -> pyautogui.PAUSE

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.PAUSE = 1

pyautogui.press("win")

pyautogui.write("Chrome")

pyautogui.press("Enter")

pyautogui.write(link)

pyautogui.press("Enter")

# espera 3 segundos
time.sleep(3)

# Passo 2 - Fazer login
pyautogui.click(x=683, y=384)

pyautogui.write("emailteste@gmail.com")

pyautogui.press("tab")

pyautogui.write("minhasenha")

pyautogui.click(x=929, y=532)
time.sleep(3)


# Passo 3 - Importar a base de dados
# instalar pandas
tabela = pd.read_csv(r"C:\Users\MayconBruno\Documents\Jornada Python\Python Power Up Automação de Tarefas  Jornada Python [Aula 1]\Produtos.csv")
print(tabela)

for linha in tabela.index:

    # Passo 4 - Cadastrar um produto 
    pyautogui.click(x=702, y=250)

    # pegar da tabela o valor do campo que a gente quer preencher com tabela.loc

    # código
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"])) # "1"
    pyautogui.press("tab")

    #preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs): # Está verificando se o valor da variável obs não é um valor NaN (Not a Number) usando a função pd.isna(obs). 
        pyautogui.write(obs)
    
    # enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")

    # pyautogui.scroll - scroll serve para rolar a tela. Valores positivos para rolar pra cima, valor negativo pra rolar pra baixo.
    pyautogui.scroll(5000)

    # Passo 5 - Repetir isso até acabar a base de dados