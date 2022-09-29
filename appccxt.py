import ccxt
import pandas as pd
import datetime
from datetime import datetime
print(dir(ccxt))
import plotly.graph_objects as go
import streamlit as st
from PIL import Image
from urllib.request import urlopen


# Titles and Subtitles
st.title("Dashboard Cryptomonedas")
st.header("HENRY Dashboard")

for exchange in ccxt.exchanges:
    print(exchange)

exchange = ccxt.ftx()
print(exchange)


# markets = exchange.load_markets()

# for market in markets:
#     print(market)


# order_book = exchange.fetch_order_book('BTC/USD')
# print(order_book)


# Bitcoin

BTC = exchange.fetch_ticker('BTC/USD')
print(BTC)

symbol= 'BTC/USD'
timeframe = '1d'
limit = 1
candles = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit= limit)
dfBTH = pd.DataFrame(candles, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
print(dfBTH) 



#streamlit
st.write("Bitcoin ($)")
imageBTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
st.image(imageBTC)
st.table(dfBTH)

####################################################################################################

# Ethereum

ETH = exchange.fetch_ticker('ETH/USD')
print(ETH)

symbol= 'ETH/USD'
timeframe = '1d'
limit = 1
candles = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit= limit)
dfETH = pd.DataFrame(candles, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
print(dfETH) 

#streamlit
st.write("Ethereum ($)")
imageETH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
st.image(imageETH)
st.table(dfETH)
#st.bar_chart(ETHHIS.Close)

#####################################################################################################

# Binance

BNB = exchange.fetch_ticker('BNB/USD')
print(BNB)

symbol= 'BNB/USD'
timeframe = '1d'
limit = 1
candles = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit= limit)
dfBNB = pd.DataFrame(candles, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
print(dfBNB) 

#streamlit
st.write("Binance ($)")
imageBNB = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1839.png'))
st.image(imageBNB)
st.table(dfBNB)
#st.bar_chart(BNBHIS.Close)

####################################################################################################

# Riple = 'XRP-USD'

XRP = exchange.fetch_ticker('XRP/USD')
print(XRP)

symbol= 'XRP/USD'
timeframe = '1d'
limit = 1
candles = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit= limit)
dfXRP = pd.DataFrame(candles, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
print(dfXRP) 

st.write("Riple ($)")
imageXRP = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))
st.image(imageXRP)
st.table(dfXRP)
#st.bar_chart(XRPHIS.Close)

####################################################################################################

# Solana = 'SOL-USD'

SOL = exchange.fetch_ticker('SOL/USD')
print(SOL)

symbol= 'SOL/USD'
timeframe = '1d'
limit = 1
candles = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit= limit)
dfSOL = pd.DataFrame(candles, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
print(dfSOL) 

#Solana
st.write("Solana ($)")
imageSOL = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/5426.png'))
st.image(imageSOL)
st.table(dfSOL)
#st.bar_chart(SOLHIS.Close)


####################################################################################################

# Dogecoin = 'DOGE-USD'

DOGE = exchange.fetch_ticker('DOGE/USD')
print(DOGE)

symbol= 'DOGE/USD'
timeframe = '1d'
limit = 1
candles = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit= limit)
dfDOGE = pd.DataFrame(candles, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
print(dfDOGE) 

#Dogecoin
st.write("Dogecoin ($)")
imageDOGE = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/74.png'))
st.image(imageDOGE)
st.table(dfDOGE)
#st.bar_chart(DOGEHIS.Close)
#####################################################################################################

# Shiba = 'SHIB-USD'

SHIB = exchange.fetch_ticker('SHIB/USD')
print(SHIB)

symbol= 'SHIB/USD'
timeframe = '1d'
limit = 1
candles = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit= limit)
dfSHIB = pd.DataFrame(candles, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
print(dfSHIB) 

#Shiba
st.write("Shiba ($)")
imageSHIB = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/5994.png'))
st.image(imageSHIB)
st.table(dfSHIB)
#st.bar_chart(SHIBHIS.Close)

####################################################################################################

# Polkadot = 'DOT-USD'

DOT = exchange.fetch_ticker('DOT/USD')
print(DOT)

symbol= 'DOT/USD'
timeframe = '1d'
limit = 1
candles = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit= limit)
dfDOT = pd.DataFrame(candles, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
print(dfDOT) 

#streamlit
st.write("Polkadot ($)")
imageDOT = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/6636.png'))
st.image(imageDOT)
st.table(dfDOT)
#st.bar_chart(DOTHIS.Close)

#####################################################################################################
# polygon MATIC/USD

MATIC = exchange.fetch_ticker('MATIC/USD')
print(MATIC)

symbol= 'MATIC/USD'
timeframe = '1d'
limit = 1
candles = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit= limit)
dfMATIC = pd.DataFrame(candles, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
print(dfMATIC)

#streamlit
st.write("polygon ($)")
imageMATIC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/3890.png'))
st.image(imageMATIC)
st.table(dfMATIC)
#st.bar_chart(MATICHIS.Close)


