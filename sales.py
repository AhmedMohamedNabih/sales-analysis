# import pandas as pd 
# import streamlit as st
# import plotly.express as px 
# import numpy as np
# st.set_page_config(layout="wide", page_title="Sales EDA", initial_sidebar_state="expanded")
# st.sidebar.header("sales")


# st.set_page_config(layout='wide',page_title='Sales EDA')
# df = pd.read_csv('cleaning_df.csv', index_col=0)
# st.title('what is the precentage of each city in the Data ?')
# st.plotly_chart(px.pie(df,names='city'))
# rev_city=df.groupby('city')['Price Each'].sum().sort_values(ascending=False).reset_index()
# st.title('what is the totla number of order per state ? ')
# st.plotly_chart(px.bar(rev_city,'city',y='Price Each',labels={'Price Each' :'Total Rev'},text_auto=True))
# df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
# df_sorted=df.sort_values(by='Order Date')
# df_sorted['com_rev']=df_sorted['Price Each'].cumsum().round(2)
# st.title('what is cmulatitave revenue from start data till and end ?')
# st.plotly_chart(px.line(df_sorted,x='Order Date',y='com_rev'))



import pandas as pd 
import streamlit as st
import plotly.express as px 
import numpy as np

st.set_page_config(layout="wide", page_title="Sales EDA", initial_sidebar_state="expanded")

df = pd.read_csv('cleaning_df.csv', index_col=0)

# مهم قبل استخدام التواريخ
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

state = st.sidebar.selectbox('State', df['state'].unique())
city  = st.sidebar.selectbox('city',  df['city'].unique())

Start_date = st.sidebar.date_input(
    'Staer Date',
    min_value=df['Order Date'].min(),
    max_value=df['Order Date'].max(),
    value=df['Order Date'].min()
)
End_date = st.sidebar.date_input(
    'End Date',
    min_value=df['Order Date'].min(),
    max_value=df['Order Date'].max(),
    value=df['Order Date'].max()
)
top_n = st.sidebar.slider('Top N', min_value=1, max_value=int(df['Product'].nunique()), value=5)

# فلترة صحيحة بالتواريخ (بدون str)
df_2 = df[
    (df['state'] == state) &
    (df['city'] == city) &
    (df['Order Date'] >= pd.to_datetime(Start_date)) &
    (df['Order Date'] <= pd.to_datetime(End_date))
]

st.dataframe(df_2, use_container_width=True)

prod_count = (
    df_2['Product']
    .value_counts()
    .reset_index(name='count')
    .rename(columns={'index': 'Product'})
    .head(top_n)
)

st.plotly_chart(
    px.bar(prod_count, x='Product', y='count', title=f'the nmost popular {top_n}', text_auto=True),
    use_container_width=True
)



