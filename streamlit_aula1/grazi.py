import pandas as pd
import streamlit as st

st.title("Meu primeiro dash")
st.subheader("Graziele Lopes")

st.write("Olá, mundo!!!!!!!")


nome = "Grazi"
idade = 18

st.write(f"eu me chamo {nome} e tenho {idade}")
df = pd.DataFrame({
  'first column': ["Português", "Matemática", "Python", "Frame"],
   'second column': [5, 9, 7, 10]
 })

df