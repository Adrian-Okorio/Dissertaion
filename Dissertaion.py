import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
import matplotlib as plt



st.write(""" ## Malaria web  Application """)
st.write("""  introduction statment """)


st.write("""Table one contains the original dataset obtained from the MalairiaAtlas 
dataset, Click the button below to view the data set:""")
if st.button('Original_Data'):
     original = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/original.csv")
     original
     type(original)

st.write("""  Below is data that was extracted after the data mining steps
 were taken which include 
1) Data Cleaning.
2) Data Integration.
3) Data Reduction.""")
df = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/data.csv")
df
type(df)

st.write(""" ### Data Analysis """)
#fig, axes = plt.subplots()
#axes[0].plot(df.infection_rate);
#axes[0].set_title('Original Series')
#plot_acf(df.infection_rate, ax=axes[1])
#st.pyplot(fig)

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

