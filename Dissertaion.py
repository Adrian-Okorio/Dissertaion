import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plt.rcParams.update({'figure.figsize': (9, 7), 'figure.dpi': 120})

st.write(""" # Malaria web  Application """)

st.sidebar.header("Malaria web  Application", )
st.sidebar.write("Designed by " "\n **Okorio Adrian**")
st.sidebar.write("**18/U/23523/PS**")
st.sidebar.write("**1800723523**")

st.sidebar.write("A Web Application supporting the  Dissertation Submitted to the School of "
                 "Statistics and Planning in Partial "
                 "Fulfillment of the Requirements of the Award of the Degree of Bachelor of "
                 "Statistics of Makerere University.")

st.header("Introduction")
st.write("""  The application uses ARIMA model to forecast a time series using the past Values.
in this web app an arima model is built to forecast and test for seasonality""")

st.write("""An ARIMA model is characterized by 3 terms: p, d, q
where,
p is the order of the AR term
q is the order of the MA term
d is the number of differencing required to make the time series stationary""")

st.write("""Table one contains the original dataset obtained from the MalairiaAtlas
dataset, Click the button below to view the data set:""")
if st.button('View Original_Data(raw data)'):
    original = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/original.csv")
    original
    type(original)

with st.expander("Expand to view cleaned dataset"):
    st.write("""  Below is data that was extracted after the data mining steps
     were taken which include
    1) Data Cleaning.
    2) Data Integration.
    3) Data Reduction.""")
    df = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/data.csv")
    df
    type(df)
    st.write("""The image below shows the most affected areas; a study survey shows 
    P. Falciparum is the leading cause of malaria in different parts of Uganda followed by P. Vivax""")
    st.image("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/diagram.jpg")

xls = pd.ExcelFile('https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/years1.xlsx')
dfyears_a = pd.read_excel(xls, 'years_a')

df1992 = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/1992.csv")
df1993 = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/1993.csv")
df1994 = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/1994.csv")
df1995 = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/1995.csv")
df1996 = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/1996.csv")
df1999 = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/1999.csv")
df2001 = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/2001.csv")
df2002 = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/2002.csv")
df2003 = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/2003.csv")
df2004 = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/2004.csv")
df2005 = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/2005.csv")
df2006 = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/2006.csv")
df2007 = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/2007.csv")
df2008 = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/2008.csv")
df2009 = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/2009.csv")
df2010 = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/2010.csv")
df2011 = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/2011.csv")
df2014 = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/2014.csv")
df2015 = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/2015.csv")
df2016 = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/2016.csv")

with st.expander("Run Various Monthly analysis"):
    # dfyears_a = years available
    option = st.selectbox(
        "which year's data would you like Analyse?",
        (dfyears_a.Years))
    st.write('You selected:', option)
    if option == 1992:
        x = df1992
    elif option == 1993:
        x = df1993
    elif option == 1994:
        x = df1994
    elif option == 1995:
        x = df1995
    elif option == 1996:
        x = df1996
    elif option == 1999:
        x = df1999
    elif option == 2001:
        x = df2001
    elif option == 2002:
        x = df2002
    elif option == 2003:
        x = df2003
    elif option == 2004:
        x = df2004
    elif option == 2005:
        x = df1999
    elif option == 2006:
        x = df2006
    elif option == 2007:
        x = df2007
    elif option == 2008:
        x = df2008
    elif option == 2009:
        x = df2009
    elif option == 2010:
        x = df2010
    elif option == 2011:
        x = df2011
    elif option == 2014:
        x = df2014
    elif option == 2015:
        x = df2015
    elif option == 2016:
        x = df2016
    labels = x.month

    col1, col2 = st.columns(2)
    with col1:
        fig7, axes = plt.subplots()
        axes.pie(x.positive, labels=labels, startangle=90, autopct='%.1f%%')
        st.pyplot(fig7)

    with col2:
        x
    labels = x.month
    fig9, axes = plt.subplots()
    axes.barh(x.month, x.positive, )
    st.pyplot(fig9)

with st.expander("summary Statitiscis"):
    st.header("General summary")
    dfmonth = pd.read_csv("https://raw.githubusercontent.com/Aredo-A/Dissertaion/main/month.csv")
    dfmonth
    fig10, axes = plt.subplots()
    axes.barh(dfmonth.month, dfmonth.positive, )
    st.pyplot(fig10)

    col5, col6 = st.columns(2)
    with col5:
        lable1 = dfmonth.month
        fig11, axes = plt.subplots()
        axes.pie(dfmonth.positive, labels=lable1, startangle=90, autopct='%.1f%%')
        st.pyplot(fig11)

    with col6:
        st.write("""Form the summary statistics its realized that seasonality plays a big role in 
        the malaria infection rate with months like December November and May having the 
        highest requested malaria infections over the years.
                        """)

with st.expander("Arima Description (What ARIMA is)"):
    st.header("Autoregressive Integrated Moving Average (ARIMA)")
    st.write("An autoregressive integrated moving average, or ARIMA,"
             "is a statistical analysis model that uses time series data to "
             "either better understand the data set or to predict future trends. "
             "A statistical model is autoregressive if it predicts future"
             "values based on past values. For example, an ARIMA model might seek "
             "to predict a stock's future prices based on its past performance or "
             "forecast a company's earnings based on past periods.")
    st.write("An autoregressive integrated moving average model is a form of regression "
             "analysis that gauges the strength of one dependent variable relative to other"
             " changing variables. The model's goal is to predict future securities or financial "
             "market moves by examining the differences between values in the series "
             "instead of through actual values."
             "An ARIMA model can be understood by outlining each of its components as follows:")
    st.write("**Autoregression (AR)**: refers to a model that shows a changing variable that regresses "
             "on its own lagged, or prior, values.")
    st.write("**Integrated (I)**: represents the differencing of raw observations to allow for the "
             "time series to become stationary (i.e., data values are replaced by the difference between "
             "the data values and the previous values).")
    st.write("**Moving average (MA)**:  incorporates the dependency between an observation and a "
             "residual error from a moving average model applied to lagged observations")

with st.expander("Run full analysis using ARIMA"):
    st.write(""" ### Data Analysis """)
    st.write("""Because, term ‘Auto Regressive’ in ARIMA means it is a linear regression model that uses its own lags as 
    predictors. Linear regression models, as you know, work best when the predictors are not correlated and are 
    independent of each other. The most common approach is to difference it. That is, subtract the previous value from 
    the current value. Sometimes, depending on the complexity of the series, more than one differencing may be needed.""")

    st.write(
        """A pure Auto Regressive (AR only) model is one where Yt depends only on its own lags. That is, Yt is a function 
        of the ‘lags of Yt’s """)
    st.image("https://www.machinelearningplus.com/wp-content/uploads/2019/02/Equation-1-min.png")

    st.write(
        """ Likewise a pure Moving Average (MA only) model is one where Yt depends only on the lagged forecast errors""")
    st.image("https://www.machinelearningplus.com/wp-content/uploads/2019/02/Equation-2-min.png")

    st.write("""An ARIMA model is one where the time series was differenced at least once to make it stationary and you 
    combine the AR and the MA terms. So the equation becomes:""")
    st.image("https://www.machinelearningplus.com/wp-content/uploads/2019/02/Equation-4-min.png")

    st.write("""The null hypothesis of the ADF test is that the time series is non-stationary. So, if the p-value of the 
    test is less than the significance level (0.05) then you reject the null hypothesis and infer that the time series is 
    indeed stationary. """)

    result = adfuller(df.infection_rate.dropna())
    st.write('*ADF Statistic*: %f' % result[0])
    st.write('*p-value*: %f' % result[1])

    fig, axes = plt.subplots(1, 2, sharex=True)
    axes[0].plot(df.infection_rate);
    axes[0].set_title('Original Series')
    plot_acf(df.infection_rate, ax=axes[1])
    st.pyplot(fig)
    st.write(
        """Since P-value is greater than the significance level, let’s difference the series and see how the 
        autocorrelation plot looks like """)

    fig1, axes = plt.subplots(2, 2, sharex=True)
    # 1st Differencing
    axes[0, 0].plot(df.infection_rate.diff());
    axes[0, 0].set_title('1st Order Differencing')
    plot_acf(df.infection_rate.diff().dropna(), ax=axes[0, 1])

    # 2nd Differencing
    axes[1, 0].plot(df.infection_rate.diff().diff());
    axes[1, 0].set_title('2nd Order Differencing')
    plot_acf(df.infection_rate.diff().diff().dropna(), ax=axes[1, 1])
    st.pyplot(fig1)

    st.write(""" identify if the model needs any AR terms""")
    st.write("""Partial autocorrection of lag (k) of a series is the coefficient of that lag 
    in the autoregression equation of Y.
    """)
    st.image("https://www.machinelearningplus.com/wp-content/uploads/2021/06/arima-equation.jpg")

    st.write(""" Any autocorrection in a stationarized series can be rectified by adding enough AR terms. So,
    we initially take the order of AR term to be equal to as many lags that crosses the significance limit in 
    the PACF plot.""")

    fig8, axes = plt.subplots(1, 2, sharex=True)
    axes[0].plot(df.infection_rate.diff());
    axes[0].set_title('1st Differencing')
    axes[1].set(ylim=(0, 5))
    plot_pacf(df.infection_rate.diff().dropna(), lags=10, ax=axes[1])

    st.pyplot(fig8)

    st.write("""The ACF tells how many MA terms are required to remove any autocorrection in the stationarized series.
    Let’s see the autocorrection plot of the differenced series.""")
    fig6, axes = plt.subplots(1, 2, sharex=True)
    axes[0].plot(df.infection_rate.diff());
    axes[0].set_title('1st Differencing')
    axes[1].set(ylim=(0, 1.2))
    plot_acf(df.infection_rate.diff().dropna(), ax=axes[1])
    st.pyplot(fig6)

    st.write(""" ### Building the ARIMA Model""")
    model = ARIMA(df.infection_rate, order=(1, 1, 1))
    model_fit = model.fit()
    st.write(model_fit.summary())

    # Plot residual errors
    residuals = pd.DataFrame(model_fit.resid)
    fig3, ax = plt.subplots(1, 2)
    residuals.plot(title="Residuals", ax=ax[0])
    residuals.plot(kind='kde', title='Density', ax=ax[1])
    st.pyplot(fig3)

    # Create Training and Test
    train = df.infection_rate[:15]
    test = df.infection_rate[15:]

    # Build Model
    model = ARIMA(train, order=(3, 2, 1))
    fitted = model.fit()
    st.write(fitted.summary())

    col3, col4 = st.columns(2)
    with col4:
        fig4, axes = plt.subplots(1, sharex=True)
        axes.plot(train);
        axes.plot(test)
        axes.set_title('Forecast')

        st.pyplot(fig4)

        fc = fitted.forecast(15, alpha=0.05)

    with col3:
        fc

    fc_series = pd.Series(fc, index=test.index)
    lower_series = pd.Series(fc[:20], index=test.index)
    upper_series = pd.Series(fc[20:], index=test.index)

    fig5, axes = plt.subplots(1, sharex=True)
    axes.plot(train, label='training')
    axes.plot(test, label='actual')
    axes.set_title('Forecast vs Actual')
    axes.plot(fc_series, label='forecast')
    axes.fill_between(lower_series.index, lower_series, upper_series,
                      color='k', alpha=.15)
    axes.legend(loc='upper left', fontsize=8)
    st.pyplot(fig5)

    st.write("""forecast data shows a reduction in the spread of malaria in Uganda""")



