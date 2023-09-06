import telebot
from telebot import types
import mysql.connector
import psycopg2
from datetime import date






CHAVE_API = "6253633084:AAEDJfuYUyNWydjAJR4dsZUh3vZGmLfSUps"

bot = telebot.TeleBot(CHAVE_API)
def grava(mensagem):
    try:
        connection = psycopg2.connect(
            host = 'localhost',
            user = 'postgres',
            password = 'Lula#2022',
            database = 'postgres',
            port = '5432'
        )

        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name
        datamem = mensagem.date
        datamem1 = date.fromtimestamp(datamem)
        comando = f"""INSERT INTO monitoramento.acessobot (nome_acesso, data_acesso) VALUES ('{entrada}', '{datamem1}')"""
        cursor.execute(comando)
        connection.commit()

    except Exception as ex:
        print(ex)


@bot.message_handler(commands=["teste"])
def teste(mensagem):
    # bot.send_animation(mensagem.chat.id, 'https://telegram.org/img/t_logo.png')
    #bot.send_animation(mensagem.chat.id, 'https://core.telegram.org/file/811140934/1/tbDSLHSaijc/fdcc7b6d5fb3354adf')
    bot.send_animation(mensagem.chat.id, 'https://lh3.googleusercontent.com/pw/AIL4fc89IjFGEAESnEE_J-312ZjzRH3aBVnitaFl6zEWv8HIzpy3AqwXQ9zSChe1Ga-jgFAGzaKGr_tIvM-m1LlquIgTOr61FCtrKCthOL_ULsy0YyuQk_-Q7Jn0lUWHsDb7rx1zm80egZhEn2-L_X5pjW0Hz0dP_QmaPGmXMmq1qv12CI17wtBcwUpgK8OeSPqdS0j1tK4av5qA3ztzFMVvB-g83abwCcQgZQfd_ZegZH9NJFsLl5F-1pY0X7xl7BDTMnjNFLqrTXlRAyRo5dtB8HtUFG2PFnsZpWK-2v53Dhne_apbqIuFTy4sOAk50ESSpxqX3n8O1ihpRbe9qQkuPbeChfliyCaTfek3O6x_oNEGTs3Ir6S_qyms9S9_4fN8NpXN0sXWnUUnIl7BAwn8NjgQMYfvGlsU-ady3V4_3O7GcDwfyWdROV60sqTjoBGjXRicw5Y10hMkg-Tze0Qc3UmLUSpbCH5t2KpesSvQr5lUM_Am81bTciHX6iGxpcxfcx9vZnUPfREL_ROSMQ2cMTNZ4GRafZ1IJyasD9KtJYle07WUFfcL2BtCLDRzb8wsQNG79PMRMSl2oppf2I3evnHkqQ5iG3-iq5zXqOxHNriZwqFjmeUWOUl40wYXR2CEKo1_Z40xgNeQcoWB-rTeJDPe9gQm7HdC8eNrSdcj_kcyJO-qC51GB_RooF-NDk7ckKRig9l96H5qCbg9lrBHfLdYSEmQPUyu-YAzfuY6ED1N25TVWxJvyArZV4sO_YQiFfX7ZdkATpnmk02xjNVkAEof2OYKyJntqxUEQnVM7hJ_qNG-aF8N3YoIsmnwN_UfwzKXlK1R4x2zqdc2cTvLhk_y11qDSTXroIu0oyIJTT5mQ7vb_zeB63F6w6dGaPOp4OLfeFFGefrU3V8=w104-h220-no?authuser=0')
    #bot.send_animation(mensagem.chat.id, 'C:/Users\Compras\PycharmProjects\pythonProject\Imagens\img.png')


@bot.message_handler(commands=["P03"])
def P03(mensagem):
    try:
        connection = psycopg2.connect(
            host = '192.168.0.169',
            user = 'postgres',
            password = 'cetis',
            database = 'dbsitec',
            port = '5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name



        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 2 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)

    except Exception as ex:

        print(ex)

    bot.send_message(mensagem.chat.id, "Oi "+ entrada)
    bot.send_message(mensagem.chat.id, "O nivel do reservatorio P03 é:  " + str(resultado[5])+" m")
    comando1 = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 2 and cd_classe = 1 ORDER BY id DESC"""
    resultado1 = cursor.fetchone()
    if not resultado1[5] == 1:
        bot.send_message(mensagem.chat.id, "Bomba ligada")
    else:
        bot.send_message(mensagem.chat.id, "Bomba desligada")

    print(resultado1)




@bot.message_handler(commands=["P41"])
def P41(mensagem):
    try:
        connection = psycopg2.connect(
            host = '192.168.0.169',
            user = 'postgres',
            password = 'cetis',
            database = 'dbsitec',
            port = '5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name



        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 68 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)

    except Exception as ex:

        print(ex)

    bot.send_message(mensagem.chat.id, "Oi "+ entrada)
    bot.send_message(mensagem.chat.id, "O nivel do reservatorio P41 é:  " + str(resultado[5])+" m")
    comando1 = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 68 and cd_classe = 1 ORDER BY id DESC"""
    resultado1 = cursor.fetchone()
    if not resultado1[5] == 1:
        bot.send_message(mensagem.chat.id, "Bomba ligada")
    else:
        bot.send_message(mensagem.chat.id, "Bomba desligada")

    print(resultado1)

@bot.message_handler(commands=["montreal", "marcos"])
def montreal(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 121 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)

    print(mensagem.chat.id)
    bot.send_message(820304760, "Acessou o bot:  "+entrada)
    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria Montreal é:  " + str(resultado[5]) + " m")


@bot.message_handler(commands=["donaneuma"])
def donaneuma(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 120 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)

    print(mensagem.chat.id)
    bot.send_message(820304760, "Acessou o bot:  "+entrada)
    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria Dona Neuma é:  " + str(resultado[5]) + " m")


@bot.message_handler(commands=["alfredo"])
def alfredodecastro(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 119 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)

    print(mensagem.chat.id)
    bot.send_message(820304760, "Acessou o bot:  "+entrada)
    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria Alfredo de Castro é:  " + str(resultado[5]) + " m")


@bot.message_handler(commands=["amelia"])
def mariaamelia(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 117 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)

    print(mensagem.chat.id)
    bot.send_message(820304760, "Acessou o bot:  "+entrada)
    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria Maria Amelia é:  " + str(resultado[5]) + " m")

@bot.message_handler(commands=["juscelino"])
def juscelinofarias(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 63 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)

    print(mensagem.chat.id)
    bot.send_message(820304760, "Acessou o bot:  "+entrada)
    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria Juscelino Farias é:  " + str(resultado[5]) + " m")



@bot.message_handler(commands=["novaera"])
def novaera(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 47 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)

    print(mensagem.chat.id)
    bot.send_message(820304760, "Acessou o bot:  "+entrada+" para ver Nova Era")
    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria Nova Era é:  " + str(resultado[5]) + " m")


@bot.message_handler(commands=["saojose"])
def saojose(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 40 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)

    print(mensagem.chat.id)
    bot.send_message(820304760, "Acessou o bot:  "+entrada)
    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria São José é:  " + str(resultado[5]) + " m")



@bot.message_handler(commands=["centro"])
def centro(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 36 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)

    print(mensagem.chat.id)
    bot.send_message(820304760, "Acessou o bot:  "+entrada)
    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria Centro é:  " + str(resultado[5]) + " m")


@bot.message_handler(commands=["padrelothar"])
def padrelothar(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 29 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)

    print(mensagem.chat.id)
    bot.send_message(820304760, "Acessou o bot:  "+entrada)
    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria Padre Lothar é:  " + str(resultado[5]) + " m")


@bot.message_handler(commands=["trespoderes"])
def trespoderes(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 28 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)

    print(mensagem.chat.id)
    bot.send_message(820304760, "Acessou o bot:  "+entrada)
    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria Tres Poderes é:  " + str(resultado[5]) + " m")


@bot.message_handler(commands=["sitio"])
def sitiofarias(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 24 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)

    print(mensagem.chat.id)
    bot.send_message(820304760, "Acessou o bot:  "+entrada)
    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria Sitio Farias é:  " + str(resultado[5]) + " m")


@bot.message_handler(commands=["lajeadinho"])
def lajeadinho(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 20 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)


    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria Lajeadinho é:  " + str(resultado[5]) + " m")



@bot.message_handler(commands=["mariatereza"])
def mariatereza(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 15 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)


    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria Maria Tereza é:  " + str(resultado[5]) + " m")


@bot.message_handler(commands=["cardoso"])
def cardoso(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 13 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)


    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria Cardoso é:  " + str(resultado[5]) + " m")


@bot.message_handler(commands=["ipanema"])
def ipanema(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 9 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)


    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria Ipanema é:  " + str(resultado[5]) + " m")


@bot.message_handler(commands=["vilagoulart"])
def vilagoulart(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 8 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)


    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria Vila Goulart é:  " + str(resultado[5]) + " m")




@bot.message_handler(commands=["maracana"])
def maracana(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 6 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)


    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria Maracana é:  " + str(resultado[5]) + " m")


@bot.message_handler(commands=["E13demaio"])
def E13demaio(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 4 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)


    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria 13 de Maio é:  " + str(resultado[5]) + " m")


@bot.message_handler(commands=["riovermelho"])
def riovermelho(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 7 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)


    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria Rio Vermelho é:  " + str(resultado[5]) + " m")

@bot.message_handler(commands=["canaa"])
def canaa(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 5 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)


    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria Canaã é:  " + str(resultado[5]) + " m")

@bot.message_handler(commands=["jdflores"])
def jdflores(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 44 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)


    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria Jd Flores é:  " + str(resultado[5]) + " m")

@bot.message_handler(commands=["canivete"])
def canivete(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 54 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)


    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria Canivete é:  " + str(resultado[5]) + " m")

@bot.message_handler(commands=["lirios"])
def lirios(mensagem):
    try:
        connection = psycopg2.connect(
            host='192.168.0.169',
            user='postgres',
            password='cetis',
            database='dbsitec',
            port='5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name

        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 3 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada + " acessou o bot")
        grava(mensagem)
    except Exception as ex:
        print(ex)


    bot.send_message(mensagem.chat.id, "Oi " + entrada)
    bot.send_message(mensagem.chat.id, "O nivel neste momento da elevatoria Lírios é:  " + str(resultado[5]) + " m")
    comando1 = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 3 and cd_classe = 1 ORDER BY id DESC"""
    resultado1 = cursor.fetchone()
    if not resultado1[5] == 1:
        bot.send_message(mensagem.chat.id, "Bomba ligada")
    else:
        bot.send_message(mensagem.chat.id, "Bomba desligada")

    print(resultado1)
@bot.message_handler(commands=["P42"])
def P42(mensagem):
    try:
        connection = psycopg2.connect(
            host = '192.168.0.169',
            user = 'postgres',
            password = 'cetis',
            database = 'dbsitec',
            port = '5432'
        )
        print("conexao exitosa")
        cursor = connection.cursor()
        entrada = mensagem.from_user.first_name ##+ " " + mensagem.from_user.last_name



        comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 71 and cd_classe = 10  ORDER BY id DESC"""

        cursor.execute(comando)
        resultado = cursor.fetchone()
        print(resultado)
        print(entrada+" acessou o bot")

    except Exception as ex:

        print(ex)

    bot.send_message(mensagem.chat.id, "Oi "+ entrada)
    bot.send_message(mensagem.chat.id, "O nivel do reservatorio P42 é:  " + str(resultado[5])+" m")
    comando1 = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 71 and cd_classe = 1 ORDER BY id DESC"""
    resultado1 = cursor.fetchone()
    if not resultado1[5] == 1:
        bot.send_message(mensagem.chat.id, "Bomba ligada")
    else:
        bot.send_message(mensagem.chat.id, "Bomba desligada")

    print(resultado1)
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)

def responder(mensagem):
    #texto = """
    #Reservatorios
    #-----------------------------------------
    #/P03 - Jardim Atlantico I
    #/P41 - Globo Recreio I
    #/P42 - Globo Recreio II
    #-----------------------------------------
    #Elevatorias de Esgoto
    #-----------------------------------------
    #/montreal
    #/donaneuma
    #/alfredo
    #/amelia
    #/juscelino
    #/novaera
    #/saojose
    #/centro
    #/padrelothar
    #/trespoderes
    #/sitio
    #/lajeadinho
    #/mariatereza
    #/cardoso
    #/ipanema
    #/vilagoulart
    #/maracana
    #/E13demaio
    #/canaa
    #/jdflores
    #/canivete
    #/riovermelho
    #/lirios """

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('/montreal')
    btn2 = types.KeyboardButton('/donaneuma')
    btn3 = types.KeyboardButton('/alfredo')
    btn4 = types.KeyboardButton('/amelia')
    btn5 = types.KeyboardButton('/juscelino')
    btn6 = types.KeyboardButton('/novaera')
    btn7 = types.KeyboardButton('/saojose')
    btn8 = types.KeyboardButton('/centro')
    btn9 = types.KeyboardButton('/padrelothar')
    btn10 = types.KeyboardButton('/trespoderes')
    btn11 = types.KeyboardButton('/sitio')
    btn12 = types.KeyboardButton('/lajeadinho')
    btn13 = types.KeyboardButton('/mariatereza')
    btn14 = types.KeyboardButton('/cardoso')
    btn15 = types.KeyboardButton('/ipanema')
    btn16 = types.KeyboardButton('/vilagoulart')
    btn17 = types.KeyboardButton('/maracana')
    btn18 = types.KeyboardButton('/E13demaio')
    btn19 = types.KeyboardButton('/canaa')
    btn20 = types.KeyboardButton('/jdflores')
    btn21 = types.KeyboardButton('/canivete')
    btn22 = types.KeyboardButton('/riovermelho')
    btn23 = types.KeyboardButton('/lirios')

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16,
               btn17,btn18, btn19, btn20, btn21, btn22, btn23 )
    bot.send_message(mensagem.chat.id, "Escolha elevatoria ", reply_markup=markup)



    #bot.reply_to(mensagem, texto)
    #a = mensagem.text
    #print(a)

bot.infinity_polling(timeout=100)
