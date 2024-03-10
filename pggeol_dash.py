import streamlit as st
import pandas as pd
import plotly.express as px 

st.set_page_config(layout="wide")

df = pd.read_csv("insights.csv", sep=";", decimal=",")
df["Data"] = pd.to_datetime(df["Data"], dayfirst=True)
df=df.sort_values("Data")
df["Month"] = df["Data"].apply(lambda x:str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())


df_filtred = df[df["Month"] == month]


col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

fig_date = px.bar(df_filtred, x="Data", y="Seguidores", color="Data", title="Seguidores alcançados")
fig_date.update_xaxes(tickformat="%d-%m-%Y") 
col1.plotly_chart(fig_date, use_container_width=True)

fig_pub = px.bar(df_filtred, x="Data", y="Alcance", color="Seguidores", title="Entrega (engajamento)")
fig_pub.update_xaxes(tickformat="%d-%m-%Y") 
col2.plotly_chart(fig_pub, use_container_width=True)

fig_enjoy = px.bar(df_filtred, x="Alcance", y="Seguidores", color= "Data", title="Alcance das publicações")
fig_enjoy.update_xaxes(tickformat="%d-%m-%Y") 
col3.plotly_chart(fig_enjoy, use_container_width=True, )



df["Alcance" ] = pd.to_datetime(df["Alcance"], dayfirst=True)
df=df.sort_values("Alcance")

df["alun"] = df["Alcance"].apply(lambda x:str(x.day) + "-" + str(x.week))
monthy = st.sidebar.selectbox("Discentes", df ["alun"].unique())

df_filt = df[df["alun"] == monthy]

col1 = st.columns(1)

fig_filt = px.bar(df_filt, x= "Discentes", y="Conection time", color="Social", title="Perfis localizados dos discentes")
col4.plotly_chart(fig_filt, use_container_width=True)
##filtragem dos discentes (HOJE)
##Trazer os discentes (egressos) na Semana
##Passa e-mail para os discentes solicitando o credenciamento nas redes sociais
##Redigir a proposta de Projeto para o Permanecer 