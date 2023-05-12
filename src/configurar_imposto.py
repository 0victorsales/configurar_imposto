import dotenv
from dados import Config_cfop
from config import links 
from config import xpath
from config import credentials
from time import sleep
from modules import xperfomance
import os


# carregando valores do env
dotenv.load_dotenv(dotenv.find_dotenv())
email = os.getenv("email")
senha = os.getenv("senha")



xp = xperfomance.Xpath_Perfomance()

#NOTE Abrindo site Omie
xp.abrir_site(links.link_omie)

#NOTE Fazendo login no Omie
xp.click(xpath.barra_email)
xp.enviar_texto(xpath.barra_email, email)
xp.click(xpath.click__email)
xp.click(xpath.barra_senha)
xp.enviar_texto(xpath.barra_senha, senha)
xp.click(xpath.click_senha)
sleep(1)

#NOTE Entrando na base
xp.abrir_site(links.link_base)
sleep(1)
xp.click(xpath.click_mensage_box)

#NOTE - Entrando no ambiente de vendas/Nenário imposto 
xp.click(xpath.click_vendas)
sleep(1)
xp.click(xpath.click_vendas_nfe)
sleep(1)
xp.click(xpath.click_configurar_impostos)


# #NOTE -Entrando no CFOP
# xp.click(xpath.click_cfop)
# sleep(1)
# xp.click(xpath.click_barra_cfop)
# sleep(1)
# xp.enviar_texto(xpath.click_barra_cfop,ncm)
# xp.pressionar_tecla(xpath.click_barra_cfop, "ENTER")
# sleep(2)
# xp.click_duplo(xpath.click_ncm)


# #NOTE - Configurando CFOP
# xp.click(xpath.bahia_cfop)
# sleep(10)

Config_cfop()

