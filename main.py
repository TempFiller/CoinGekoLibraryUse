# Python convention to indicate that this is a script which can be run.
if __name__ == '__main__':
    print('This is a working script')

# This is a Python script to use the CoinGeko API
# let’s go ahead and install it with Python with the command: pip install pycoingecko
# it is already installed in the virtual environment of this PyCharm project
# Link for API documentation/endpoints for Python (GitHub): https://github.com/man-c/pycoingecko

# import the pandas library to use its functions and to work with dataframes
import pandas as pd
# first step import the CoinGecko library and set the client up
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

# ########### here is a section of code (commented out) which list the possible func of the API#########################

# If you want to get a list of available coins using CoinGeck use the next lines.
# df means the usage of Pandas library to format a table:

# coins = cg.get_coins_list()
# df_coins = pd.DataFrame(coins, columns=['name'])
# df_coins

# In order to list all the supported coins prices, volume, market caps and related data for a specific
# currency (USD) use the next code lines. Again usage of Pandas library to format a table:

# coin_market=cg.get_coins_markets(vs_currency='usd')
# df_market = pd.DataFrame(coin_market, columns=['id','current_price','high_24h','low_24h'])
# df_market.set_index('id',inplace=True)
# df_market

# To get price data with more parameters like the 24hour change, volume or market cap, we can write the following code:
# cg.get_price(ids='Coinid', vs_currencies='usd', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')

#######################################################################################################################

# the following code is the relevant part to get the historical data for a project listed on CoinGeko
# we keep the code simple so that it can be understood with nearly no understanding of python
# so no OOP (i.e. Classes) or usage of a dictionary for the different Tokens, which could be used to shorten the code

# API IDs (in CoinGeko) of the biggest DeFi projects by TVL (DeFi Pulse, DeFi Llama) on the ETH Blockchain:
# (Curve DAO Token (CRV) = curve-dao-token, Maker (MKR) = maker, Aave (AAVE) = aave, Uniswap (UNI) = uniswap,
# Compound (COMP) = compound-governance-token, Instadapp (INST) = instadapp, Sushi Swap (SUSHI) = sushi,
# Balancer (BAL) = balancer, dYdX (DYDX) = dydx, Bancor Network Token (BNT) = bancor)
# IDs for Ethereum (ETH) = ethereum, Bitcoin (BTC) = bitcoin

# To obtain historical data with a precise UNIX timestamp range
# That includes price, market cap, and 24h volume within a range of timestamp (granularity auto)
# Start and end of the data period (01.01.2020-01.02.2022) - if data for the project is available
# Unix timestamp Wed Jan 01 2020 00:00:00 GMT+0100 (Mitteleuropäische Normalzeit) = 1577833200
# Unix timestamp Wed Feb 01 2022 00:00:00 GMT+0100 (Mitteleuropäische Normalzeit) = 1643756400


# here the necessary code to get the historical data for Bitcoin
history_BTC = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='usd', from_timestamp="1577833200",
                                                   to_timestamp='1643756400')

# the API call could be printed out  with the following statement (commented out):
# print(history_BTC)

# in the raw API call the data (price, volume & marketcap) are paired with the corresponding timestamp
# we use functions of the Pandas library to format a better table and separate timestamp and other values

# create a table with 4 specific columns
df_history_BTC = pd.DataFrame(history_BTC, columns=['timestamp', 'prices', 'market_caps', 'total_volumes'])

# set the column timestamp equal to the first row (index 0) of the column of the price column (i.e. timestamps of the prices)
df_history_BTC['timestamp'] = df_history_BTC['prices'].apply(lambda x: x[0])

# set the columns equal to the second row (index 1) of the column (i.e. delete the timestamps). we use lambda func here
df_history_BTC['prices'] = df_history_BTC['prices'].apply(lambda x: x[1])
df_history_BTC['market_caps'] = df_history_BTC['market_caps'].apply(lambda x: x[1])
df_history_BTC['total_volumes'] = df_history_BTC['total_volumes'].apply(lambda x: x[1])

# set the timestamps as the index of the table so that each timestamp hast a corresponding price, volume & marketcap
df_history_BTC.set_index('timestamp', inplace=True)

# save the created table as a CSV file which then can be used in the analysis (after some minor changes/formatting)
df_history_BTC.to_csv("BTC-History-Data.csv", index=True)

# with the following codeline the table can be printed in the python console
print(df_history_BTC)


# same operations as above for the other projects
# ETH historical data
history_ETH = cg.get_coin_market_chart_range_by_id(id='ethereum', vs_currency='usd', from_timestamp="1577833200",
                                                   to_timestamp='1643756400')
df_history_ETH = pd.DataFrame(history_ETH, columns=['timestamp', 'prices', 'market_caps', 'total_volumes'])
df_history_ETH['timestamp'] = df_history_ETH['prices'].apply(lambda x: x[0])
df_history_ETH['prices'] = df_history_ETH['prices'].apply(lambda x: x[1])
df_history_ETH['market_caps'] = df_history_ETH['market_caps'].apply(lambda x: x[1])
df_history_ETH['total_volumes'] = df_history_ETH['total_volumes'].apply(lambda x: x[1])
df_history_ETH.set_index('timestamp', inplace=True)
df_history_ETH.to_csv("ETH-History-Data.csv", index=True)
print(df_history_ETH)


# CURVE DAO historical data
history_CURVE = cg.get_coin_market_chart_range_by_id(id='curve-dao-token', vs_currency='usd', from_timestamp="1577833200",
                                     to_timestamp='1643756400')
df_history_CURVE = pd.DataFrame(history_CURVE, columns=['timestamp', 'prices', 'market_caps', 'total_volumes'])
df_history_CURVE['timestamp'] = df_history_CURVE['prices'].apply(lambda x: x[0])
df_history_CURVE['prices'] = df_history_CURVE['prices'].apply(lambda x: x[1])
df_history_CURVE['market_caps'] = df_history_CURVE['market_caps'].apply(lambda x: x[1])
df_history_CURVE['total_volumes'] = df_history_CURVE['total_volumes'].apply(lambda x: x[1])
df_history_CURVE.set_index('timestamp', inplace=True)
df_history_CURVE.to_csv("CURVE-History-Data.csv", index=True)
print(df_history_CURVE)


# Maker DAO historical data
history_MAKER = cg.get_coin_market_chart_range_by_id(id='maker', vs_currency='usd', from_timestamp="1577833200",
                                     to_timestamp='1643756400')
df_history_MAKER = pd.DataFrame(history_MAKER, columns=['timestamp', 'prices', 'market_caps', 'total_volumes'])
df_history_MAKER['timestamp'] = df_history_MAKER['prices'].apply(lambda x: x[0])
df_history_MAKER['prices'] = df_history_MAKER['prices'].apply(lambda x: x[1])
df_history_MAKER['market_caps'] = df_history_MAKER['market_caps'].apply(lambda x: x[1])
df_history_MAKER['total_volumes'] = df_history_MAKER['total_volumes'].apply(lambda x: x[1])
df_history_MAKER.set_index('timestamp', inplace=True)
df_history_MAKER.to_csv("MAKER-History-Data.csv", index=True)
print(df_history_MAKER)


# AAVE historical data
history_AAVE = cg.get_coin_market_chart_range_by_id(id='aave', vs_currency='usd', from_timestamp="1577833200",
                                     to_timestamp='1643756400')
df_history_AAVE = pd.DataFrame(history_AAVE, columns=['timestamp', 'prices', 'market_caps', 'total_volumes'])
df_history_AAVE['timestamp'] = df_history_AAVE['prices'].apply(lambda x: x[0])
df_history_AAVE['prices'] = df_history_AAVE['prices'].apply(lambda x: x[1])
df_history_AAVE['market_caps'] = df_history_AAVE['market_caps'].apply(lambda x: x[1])
df_history_AAVE['total_volumes'] = df_history_AAVE['total_volumes'].apply(lambda x: x[1])
df_history_AAVE.set_index('timestamp', inplace=True)
df_history_AAVE.to_csv("AAVE-History-Data.csv", index=True)
print(df_history_AAVE)


# UNI historical data
history_UNI = cg.get_coin_market_chart_range_by_id(id='uniswap', vs_currency='usd', from_timestamp="1577833200",
                                     to_timestamp='1643756400')
df_history_UNI = pd.DataFrame(history_UNI, columns=['timestamp', 'prices', 'market_caps', 'total_volumes'])
df_history_UNI['timestamp'] = df_history_UNI['prices'].apply(lambda x: x[0])
df_history_UNI['prices'] = df_history_UNI['prices'].apply(lambda x: x[1])
df_history_UNI['market_caps'] = df_history_UNI['market_caps'].apply(lambda x: x[1])
df_history_UNI['total_volumes'] = df_history_UNI['total_volumes'].apply(lambda x: x[1])
df_history_UNI.set_index('timestamp', inplace=True)
df_history_UNI.to_csv("UNI-History-Data.csv", index=True)
print(df_history_UNI)


# COMP historical data
history_COMP = cg.get_coin_market_chart_range_by_id(id='compound-governance-token', vs_currency='usd', from_timestamp="1577833200",
                                     to_timestamp='1643756400')
df_history_COMP = pd.DataFrame(history_COMP, columns=['timestamp', 'prices', 'market_caps', 'total_volumes'])
df_history_COMP['timestamp'] = df_history_COMP['prices'].apply(lambda x: x[0])
df_history_COMP['prices'] = df_history_COMP['prices'].apply(lambda x: x[1])
df_history_COMP['market_caps'] = df_history_COMP['market_caps'].apply(lambda x: x[1])
df_history_COMP['total_volumes'] = df_history_COMP['total_volumes'].apply(lambda x: x[1])
df_history_COMP.set_index('timestamp', inplace=True)
df_history_COMP.to_csv("COMP-History-Data.csv", index=True)
print(df_history_COMP)


# INST historical data
history_INST = cg.get_coin_market_chart_range_by_id(id='instadapp', vs_currency='usd', from_timestamp="1577833200",
                                     to_timestamp='1643756400')
df_history_INST = pd.DataFrame(history_INST, columns=['timestamp', 'prices', 'market_caps', 'total_volumes'])
df_history_INST['timestamp'] = df_history_INST['prices'].apply(lambda x: x[0])
df_history_INST['prices'] = df_history_INST['prices'].apply(lambda x: x[1])
df_history_INST['market_caps'] = df_history_INST['market_caps'].apply(lambda x: x[1])
df_history_INST['total_volumes'] = df_history_INST['total_volumes'].apply(lambda x: x[1])
df_history_INST.set_index('timestamp', inplace=True)
df_history_INST.to_csv("INST-History-Data.csv", index=True)
print(df_history_INST)


# SUSHI historical data
history_SUSHI = cg.get_coin_market_chart_range_by_id(id='sushi', vs_currency='usd', from_timestamp="1577833200",
                                     to_timestamp='1643756400')
df_history_SUSHI = pd.DataFrame(history_SUSHI, columns=['timestamp', 'prices', 'market_caps', 'total_volumes'])
df_history_SUSHI['timestamp'] = df_history_SUSHI['prices'].apply(lambda x: x[0])
df_history_SUSHI['prices'] = df_history_SUSHI['prices'].apply(lambda x: x[1])
df_history_SUSHI['market_caps'] = df_history_SUSHI['market_caps'].apply(lambda x: x[1])
df_history_SUSHI['total_volumes'] = df_history_SUSHI['total_volumes'].apply(lambda x: x[1])
df_history_SUSHI.set_index('timestamp', inplace=True)
df_history_SUSHI.to_csv("SUSHI-History-Data.csv", index=True)
print(df_history_SUSHI)

# BAL historical data
history_BAL = cg.get_coin_market_chart_range_by_id(id='balancer', vs_currency='usd', from_timestamp="1577833200",
                                     to_timestamp='1643756400')
df_history_BAL = pd.DataFrame(history_BAL, columns=['timestamp', 'prices', 'market_caps', 'total_volumes'])
df_history_BAL['timestamp'] = df_history_BAL['prices'].apply(lambda x: x[0])
df_history_BAL['prices'] = df_history_BAL['prices'].apply(lambda x: x[1])
df_history_BAL['market_caps'] = df_history_BAL['market_caps'].apply(lambda x: x[1])
df_history_BAL['total_volumes'] = df_history_BAL['total_volumes'].apply(lambda x: x[1])
df_history_BAL.set_index('timestamp', inplace=True)
df_history_BAL.to_csv("BAL-History-Data.csv", index=True)
print(df_history_BAL)

# DYDX historical data
history_DYDX = cg.get_coin_market_chart_range_by_id(id='dydx', vs_currency='usd', from_timestamp="1577833200",
                                     to_timestamp='1643756400')
df_history_DYDX = pd.DataFrame(history_DYDX, columns=['timestamp', 'prices', 'market_caps', 'total_volumes'])
df_history_DYDX['timestamp'] = df_history_DYDX['prices'].apply(lambda x: x[0])
df_history_DYDX['prices'] = df_history_DYDX['prices'].apply(lambda x: x[1])
df_history_DYDX['market_caps'] = df_history_DYDX['market_caps'].apply(lambda x: x[1])
df_history_DYDX['total_volumes'] = df_history_DYDX['total_volumes'].apply(lambda x: x[1])
df_history_DYDX.set_index('timestamp', inplace=True)
df_history_DYDX.to_csv("DYDX-History-Data.csv", index=True)
print(df_history_DYDX)



# BNT historical data
history_BNT = cg.get_coin_market_chart_range_by_id(id='bancor', vs_currency='usd', from_timestamp="1577833200",
                                     to_timestamp='1643756400')
df_history_BNT = pd.DataFrame(history_BNT, columns=['timestamp', 'prices', 'market_caps', 'total_volumes'])
df_history_BNT['timestamp'] = df_history_BNT['prices'].apply(lambda x: x[0])
df_history_BNT['prices'] = df_history_BNT['prices'].apply(lambda x: x[1])
df_history_BNT['market_caps'] = df_history_BNT['market_caps'].apply(lambda x: x[1])
df_history_BNT['total_volumes'] = df_history_BNT['total_volumes'].apply(lambda x: x[1])
df_history_BNT.set_index('timestamp', inplace=True)
df_history_BNT.to_csv("BNT-History-Data.csv", index=True)
print(df_history_BNT)