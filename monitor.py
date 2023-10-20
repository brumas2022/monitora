import streamlit as st
import psycopg2

st.header("Monitor de nivel de poços e reservatorios do SANEAR")
st.write("---")


poco = st.selectbox("Escolha o poço", ("P41","P42","P64","P03","P59","P58","P04","P34","P54","P45","P32","P55","P51","P30","P01","P07","P23","P61"))
    
if poco == "P41":
        id = 68
elif poco == "/P42":
        id = 71
elif poco == "/P64":
        id = 1
elif poco == "/P03":
        id = 2
elif poco == "/P59":
        id = 50
elif poco == "/P58":
        id = 52
elif poco == "/P04":
        id = 67
elif poco == "/P34":
        id = 69
elif poco == "/P54":
        id = 70
elif poco == "/P45":
        id = 72
elif poco == "/P32":
        id = 75
elif poco == "/P55":
        id = 80
elif poco == "/P51":
        id = 100
elif poco == "/P30":
        id = 101
elif poco == "/P01":
        id = 102
elif poco == "/P07":
        id = 103
elif poco == "/P23":
        id = 104
elif poco == "/P61":
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








   
