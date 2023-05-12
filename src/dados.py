import pandas as pd
import dotenv

from config import xpath
from config import credentials
from time import sleep
from modules import xperfomance
import os

def Config_cfop():

    xp = xperfomance.Xpath_Perfomance()

    # Criando data frame
    df_excel = pd.read_excel("produtos.xlsx")

    # Descobrindo tamanho da planilha
    tamanho_excel = df_excel.shape[0]
    lista_excel = []



    for i in tamanho_excel:
        num = 4
        ind = 2
        lista_excel = (df_excel.loc[num])
        if(lista_excel[ind]) != '':
            #NOTE -Entrando no CFOP
            xp.click(xpath.click_cfop)
            sleep(1)
            xp.click(xpath.click_barra_cfop)
            sleep(1)
            xp.enviar_texto(xpath.click_barra_cfop,lista_excel[ind])
            xp.pressionar_tecla(xpath.click_barra_cfop, "ENTER")
            sleep(2)
            xp.click_duplo(xpath.click_ncm)


            #NOTE - Configurando CFOP
            xp.click(xpath.bahia_cfop)
            sleep(10)

            num = num + 1
            ind = ind + 1
            

