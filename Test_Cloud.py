
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("Sales_Store_Preprocessed.csv")
st.title("Super Store")


st.metric(label="Total Sales in M$" , value=(df["Sales"]. sum() / 1000000). round (3))
st.write("")

fig_pie =px.pie(df , names = "Category" , values = "Sales" , title="Total Sales/Category ")
st.plotly_chart(fig_pie)
st.write("")
st.header("Discount Distribution")

fig_dist=ff.create_distplot([df["Discount"]] , ["Discount Destribution"] , show_hist= False , show_rug= False)
st.plotly_chart(fig_dist)
