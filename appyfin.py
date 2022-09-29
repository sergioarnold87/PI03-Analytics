import streamlit as st
import pandas as pd

import yfinance as yf
import streamlit as streamlit
from PIL import Image
from urllib.request import urlopen

# Titles and Subtitles
st.title("Dashboard Cryptomonedas")
st.header("HENRY Dashboard")

#Defining ticker variables
Bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'
Binance ='BNB-USD'
Riple = 'XRP-USD'
Solana = 'SOL-USD'
Dogecoin = 'DOGE-USD'
Shiba = 'SHIB-USD'
Polkadot = 'DOT-USD'
polygon = 'MATIC-USD'

# Access data from Yahoo Finance
BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
BNB_Data = yf.Ticker(Binance)
XRP_Data = yf.Ticker(Riple)
SOL_Data = yf.Ticker(Solana)
DOGE_Data = yf.Ticker(Dogecoin)
SHIB_Data = yf.Ticker(Shiba)
DOT_Data = yf.Ticker(Polkadot)
MATIC_Data = yf.Ticker(polygon)

# Fetch history data from Yahoo Finance
BTCHIS = BTC_Data.history(period="max")
ETHHIS = ETH_Data.history(period="max")
BNBHIS = BNB_Data.history(period="max")
XRPHIS = XRP_Data.history(period="max")
SOLHIS = SOL_Data.history(period="max")
DOGEHIS = DOGE_Data.history(period="max")
SHIBHIS = SHIB_Data.history(period="max")
DOTHIS = DOT_Data.history(period="max")
MATICHIS = MATIC_Data.history(period="max")

#Fetch crypto data for the dataframe
BTC = yf.download(Bitcoin, start = "2022-09-27", end = "2022-09-27")
ETH = yf.download(Ethereum, start = "2022-09-27", end = "2022-09-27")
BNB = yf.download(Binance, start = "2022-09-27", end = "2022-09-27")
XRP = yf.download(Riple, start = "2022-09-27", end = "2022-09-27")
SOL = yf.download(Solana, start = "2022-09-27", end = "2022-09-27")
DOGE = yf.download(Dogecoin, start = "2022-09-27", end = "2022-09-27")
SHIB = yf.download(Shiba, start = "2022-09-27", end = "2022-09-27")
DOT = yf.download(Polkadot, start = "2022-09-27", end = "2022-09-27")
MATIC = yf.download(polygon, start = "2022-09-27", end = "2022-09-27")

#####################################################################################################

#Bitcoin
st.write("Bitcoin ($)")
imageBTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
st.image(imageBTC)
st.table(BTC)
st.bar_chart(BTCHIS.Close)

#####################################################################################################

#####################################################################################################

#Ethereum
st.write("Ethereum ($)")
imageETH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
st.image(imageETH)
st.table(ETH)
st.bar_chart(ETHHIS.Close)
#####################################################################################################

#####################################################################################################

#Binance
st.write("Binance ($)")
imageBNB = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1839.png'))
st.image(imageBNB)
st.table(BNB)
st.bar_chart(BNBHIS.Close)
#####################################################################################################

#####################################################################################################
#Riple
st.write("Riple ($)")
imageXRP = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))
st.image(imageXRP)
st.table(XRP)
st.bar_chart(XRPHIS.Close)

#####################################################################################################

#####################################################################################################

#Solana
st.write("Solana ($)")
imageSOL = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/5426.png'))
st.image(imageSOL)
st.table(SOL)
st.bar_chart(SOLHIS.Close)

#####################################################################################################

#####################################################################################################

#Dogecoin
st.write("Dogecoin ($)")
imageDOGE = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/74.png'))
st.image(imageDOGE)
st.table(DOGE)
st.bar_chart(DOGEHIS.Close)
#####################################################################################################

#####################################################################################################

#Shiba
st.write("Shiba ($)")
imageSHIB = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/5994.png'))
st.image(imageSHIB)
st.table(SHIB)
st.bar_chart(SHIBHIS.Close)
#####################################################################################################

#####################################################################################################
#Polkadot
st.write("Polkadot ($)")
imageDOT = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/6636.png'))
st.image(imageDOT)
st.table(DOT)
st.bar_chart(DOTHIS.Close)
#####################################################################################################

#####################################################################################################
#polygon
st.write("polygon ($)")
imageMATIC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/3890.png'))
st.image(imageMATIC)
st.table(MATIC)
st.bar_chart(MATICHIS.Close)
#####################################################################################################














