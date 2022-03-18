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
st.write("""  imaage description of the most affected areas in udanda """)
st.write(""" data collected description""")
st.image("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/diagram.jpg")

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


st.write("""  auto correlation description """)
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

st.write("""  identify if the model needs any AR terms""")
st.write("""Partial autocorrelation of lag (k) of a series is the coefficient of that lag in the autoregression equation of Y.
""")
st.image("https://www.machinelearningplus.com/wp-content/uploads/2021/06/arima-equation.jpg")



fig8, axes = plt.subplots(1, 2, sharex=True)
axes[0].plot(df.infection_rate.diff()); axes[0].set_title('1st Differencing')
axes[1].set(ylim=(0,5))
plot_pacf(df.infection_rate.diff().dropna(), lags= 10, ax=axes[1])

st.pyplot(fig8)




st.write("""The ACF tells how many MA terms are required to remove any autocorrelation in the stationarized series.
Let’s see the autocorrelation plot of the differenced series.""")
fig6, axes = plt.subplots(1, 2, sharex=True)
axes[0].plot(df.infection_rate.diff()); axes[0].set_title('1st Differencing')
axes[1].set(ylim=(0,1.2))
plot_acf(df.infection_rate.diff().dropna(), ax=axes[1])
st.pyplot(fig6)


st.write(""" ### Building the ARIMA Model""")
model = ARIMA(df.infection_rate, order=(1,1,1))
model_fit = model.fit()
st.write(model_fit.summary())


# Plot residual errors
residuals = pd.DataFrame(model_fit.resid)
fig3, ax = plt.subplots(1,2)
residuals.plot(title="Residuals", ax=ax[0])
residuals.plot(kind='kde', title='Density', ax=ax[1])
st.pyplot(fig3)

#---------------------------------------------------------------

# Create Training and Test
train = df.infection_rate[:15]
test = df.infection_rate[15:]


# Build Model
model = ARIMA(train, order=(3, 2, 1))
fitted = model.fit()
st.write(fitted.summary())



fig4, axes = plt.subplots(1, sharex=True)
axes.plot(train);
axes.plot(test)
axes.set_title('Forecast')

st.pyplot(fig4)

fc = fitted.forecast(15, alpha=0.05)
fc
fc_series = pd.Series(fc, index=test.index)
lower_series = pd.Series(fc[:20], index=test.index)
upper_series = pd.Series(fc[20:], index=test.index)

fig5, axes = plt.subplots(1, sharex=True)
axes.plot(train, label='training')
axes.plot(test, label='actual')
axes.plot(fc_series, label='forecast')
axes.fill_between(lower_series.index, lower_series, upper_series,
                 color='k', alpha=.15)
axes.legend(loc='upper left', fontsize=8)
st.pyplot(fig5)
