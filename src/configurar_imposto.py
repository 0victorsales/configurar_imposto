import dotenv
from config import links 
from config import xpath
from config import credentials
from time import sleep
from modules import xperfomance
import os

#carregando valores do env
dotenv.load_dotenv(dotenv.find_dotenv())
email = os.getenv("email")
senha = os.getenv("senha")

xp = xperfomance.Xpath_Perfomance()

# Abrindo site Omie
xp.abrir_site(links.link_omie)

# Fazendo login no Omie
xp.click(xpath.xpath_email)
xp.enviar_texto(xpath.xpath_email, email)
xp.click(xpath.xpath_click__email)
xp.click(xpath.xpath_senha)
xp.enviar_texto(xpath.xpath_senha, senha)
xp.click(xpath.xpath_click_senha)
sleep(1)

# Entrando na base
xp.abrir_site(links.link_base)
sleep(1)
xp.click(xpath.xpath_mensage_box)
xp.click(xpath.xpath_vendas)
sleep(1)


xp.click(xpath.xpath_vendas_nfe)
sleep(1)
xp.click(xpath.xpath_configurar_impostos)
sleep(5)

