import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf



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
fig, axes = plt.subplots(1, 2, sharex=True)
axes[0].plot(df.infection_rate);
axes[0].set_title('Original Series')
plot_acf(df.infection_rate, ax=axes[1])
st.pyplot(fig)
