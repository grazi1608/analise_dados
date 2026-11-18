
# Graziele Lopes Leite
# obs: não sei oq ru fiz, te amo Jana
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_excel("saeb_aprendizado_territorios-7-2023-EM.xlsx",
sheet_name="estados", engine="openpyxl")
st.set_page_config(page_title="Aprendizado", page_icon="📚", layout="centered")

st.title("Planilha de aprenzizado")
st.sidebar.header("Controles")
opcao = st.sidebar.radio("Selecione a visualização:", ["Tabela", "Gráficos"])
st.write("Dados sobre o aprendizado - Português insuficiente e matemática insuficiente")

abas = st.tabs([
    "MG",
    "MG",
    "CE",
    "PR",

])

anos = list(range(2023, 2026))
bairros = ["MG", "MG","CE","PR"]
dimensoes = ["Educacao", "Português insuficiente", "matemática insuficiente"]

df_tabela
np.random.seed(42)
dados_tabela_list = []
for ano in aprendizado:
  for b in territorio:
    base_val = 0.5 if b == "Taquaril" else 0.7
    iqvu = np.clip(base_val + np.random.normal(0, 0.05), 0.1, 0.95)
    dados_tabela_list.append({"aprendizado": str(ano), "NOMEUP": b, "IQVU": iqvu})
df_tabela = pd.DataFrame(dados_tabela_list)


dados_filtrado_list = []
for ano in  aprendizado:
  for b in bairros:
    row = {"Aprendizado": str(ano), "NOMEUP": b, "IQVU": np.random.uniform(0.4, 0.9)}
    for dim in dimensoes:
      row[dim] = np.random.uniform(0.3, 0.95)
    dados_filtrado_list.append(row)
df_filtrado = pd.DataFrame(dados_filtrado_list)


dados_empilhado_list = []
for b in bairros:
  for dim in dimensoes:
    dados_empilhado_list.append(
        {"territorios": b, "Dimensao": dim, "Valor": np.random.uniform(0.1, 0.3)}
    )
dados_empilhado = pd.DataFrame(dados_empilhado_list)

with abas[2]:
  st.header("matematica insuficiente")
  fig_barras = px.bar(
      df_tabela,
      x="Aprendizado",
      y="IQVU",
      color="NOMEUP",
      barmode="group",
      title="matematica insuficiente",
      color_discrete_map={"Taquaril": "#FF6B6B", "matematica": "#00F5D4"},
      template="plotly_dark",
  )
  fig_barras.update_xaxes(type="category")
  st.plotly_chart(fig_barras, use_container_width=True)

with abas[2]:
  st.header("portugues insuficiente")
  fig_barras = px.bar(
      df_tabela,
      x="Aprendizado",
      y="IQVU",
      color="NOMEUP",
      barmode="group",
      title="portugues insuficiente",
      color_discrete_map={"Taquaril": "#FF6B6B", "portugues": "#00F5D4"},
      template="plotly_dark",
  )
  fig_barras.update_xaxes(type="category")
  st.plotly_chart(fig_barras, use_container_width=True)

with abas[1]:
  st.header("Questão 2 — Gráfico de Linha Individual ")
  df_santa_ines = df_tabela[df_tabela["NOMEUP"] == "portugues"]
  fig_linha_santa_ines = px.line(
      df_santa_ines,
      x="ANO",
      y="IQVU",
      markers=True,
      title="portugues insuficiente (2023 a 2026)",
      template="plotly_dark",
  )
  fig_linha_santa_ines.update_traces(
      line_color="#00F5D4", line_width=3, marker_size=8
  )
  fig_linha_santa_ines.update_xaxes(type="category")
  st.plotly_chart(fig_linha_santa_ines, use_container_width=True)

with abas[1]:
  st.header(" Gráfico de Linha Individual ")
  df_santa_ines = df_tabela[df_tabela["NOMEUP"] == "matematica"]
  fig_linha_santa_ines = px.line(
      df_santa_ines,
      x="ANO",
      y="IQVU",
      markers=True,
      title="matematica insuficiente (2023 a 2026)",
      template="plotly_dark",
  )
  fig_linha_santa_ines.update_traces(
      line_color="#00F5D4", line_width=3, marker_size=8
  )
  fig_linha_santa_ines.update_xaxes(type="category")
  st.plotly_chart(fig_linha_santa_ines, use_container_width=True)

