import pandas as pd 
import streamlit as st
import plotly.express as px 
import numpy as np
st.set_page_config(layout='wide',page_title='Sales EDA')
df=pd.read_csv('E:/preprocessing 8/cleaning_df.csv',index_col=0)
st.title('what is the precentage of each city in the Data ?')
st.plotly_chart(px.pie(df,names='city'))
rev_city=df.groupby('city')['Price Each'].sum().sort_values(ascending=False).reset_index()
st.title('what is the totla number of order per state ? ')
st.plotly_chart(px.bar(rev_city,'city',y='Price Each',labels={'Price Each' :'Total Rev'},text_auto=True))
df_sorted=df.sort_values(by='Order Date')
df_sorted['com_rev']=df_sorted['Price Each'].cumsum().round(2)
st.title('what is cmulatitave revenue from start data till and end ?')
st.plotly_chart(px.line(df_sorted,x='Order Date',y='com_rev'))
