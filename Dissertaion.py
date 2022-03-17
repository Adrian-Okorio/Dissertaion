import numpy as np
import pandas as pd
import altair as alt
import streamlit as st


from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
plt.rcParams.update({'figure.figsize':(9,7), 'figure.dpi':120})

st.write(""" ## Malaria web  Application """)
st.write("""  introduction statment """)


st.write("""Table one contains the original dataset obtained from the MalairiaAtlas 
dataset, Click the button below to view the data set:""")
if st.button('Original_Data'):
     original = pd.read_csv("D:\Jupyter\original.csv")
     original
     type(original)

st.write("""  Below is data that was extracted after the data mining steps
 were taken which include 
1) Data Cleaning.
2) Data Integration.
3) Data Reduction.""")
df = pd.read_csv("D:\Jupyter\data.csv")
df
type(df)

st.write(""" ### Data Analysis """)
fig, axes = plt.subplots(1, 2, sharex=True)
axes[0].plot(df.infection_rate);
axes[0].set_title('Original Series')
plot_acf(df.infection_rate, ax=axes[1])
st.pyplot(fig)

st.write(""" Description of the data and why use first and 
second order diffrencaition""")
fig1, axes = plt.subplots(2, 2, sharex=True)
# 1st Differencing
axes[0, 0].plot(df.infection_rate.diff()); axes[0, 0].set_title('1st Order Differencing')
plot_acf(df.infection_rate.diff().dropna(), ax=axes[0, 1])

# 2nd Differencing
axes[1, 0].plot(df.infection_rate.diff().diff()); axes[1, 0].set_title('2nd Order Differencing')
plot_acf(df.infection_rate.diff().diff().dropna(), ax=axes[1, 1])
st.pyplot(fig1)
