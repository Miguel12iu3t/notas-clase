#importacion, primer uso de streamlit 
import streamlit as st

st.title("Calculadora ICI")

#Entrada de números
num1 = st.number_input("Ingrese el primer número:")
num2 = st.number_input("Ingrese el segundo número:")

#Operaciones matemáticas
operacion = st.selectbox("Seleccione una operación:", ["Suma", "Resta", "Multiplicación", "División"])

resultado = 0
#condicional la cual cada una de ellas hara su respectica operacion
#Nota: esta fue mi forma de resolver el ejercicio
if operacion == "Suma":
    resultado = num1 + num2
elif operacion == "Resta":
    resultado = num1 - num2
elif operacion == "Multiplicación":
    resultado = num1 * num2
elif operacion == "División":
    if num2 != 0:
        resultado = num1 / num2
    else:
        st.error("Error: No se puede dividir por cero")

#Mostrar el resultado
st.write(f"Resultado de = {resultado}")
