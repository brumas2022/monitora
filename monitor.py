import streamlit as st
import psycopg2

    poco = st.selectbox("Escolha o poço", ("P41","P42","P64","P03","P59","P58","P04","P34","P54","P45","P32","P55","P51","P30","P01","P07","P23","P61"))
    
    if poco == "P41":
        id = 68
    elif mensagem.text == "/P42":
        print(mensagem.text)
        id = 71
    elif mensagem.text == "/P64":
        print(mensagem.text)
        id = 1
    elif mensagem.text == "/P03":
        id = 2
    elif mensagem.text == "/P59":
        id = 50
    elif mensagem.text == "/P58":
        id = 52
    elif mensagem.text == "/P04":
        id = 67
    elif mensagem.text == "/P34":
        id = 69
    elif mensagem.text == "/P54":
        id = 70
    elif mensagem.text == "/P45":
        id = 72
    elif mensagem.text == "/P32":
        id = 75
    elif mensagem.text == "/P55":
        id = 80
    elif mensagem.text == "/P51":
        id = 100
    elif mensagem.text == "/P30":
        id = 101
    elif mensagem.text == "/P01":
        id = 102
    elif mensagem.text == "/P07":
        id = 103
    elif mensagem.text == "/P23":
        id = 104
    elif mensagem.text == "/P61":
        id = 108

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
        
        comando = f"SELECT * FROM saneamento.registro_grandezas WHERE id_amb = {id} and cd_classe = 10  ORDER BY id DESC LIMIT 2"

        cursor.execute(comando)
        resultado = cursor.fetchone()
        st.write(resultado)

    except Exception as ex:

        print(ex)








   
