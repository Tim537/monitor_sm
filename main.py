"""This file is the main module for monitoring"""
import os
import requests
from lxml import html
import yfinance

iex_private = os.environ["IEX_PRIVATE"]
iex_public = os.environ["IEX_PUBLIC"]

etf_url = f"https://api.iex.cloud/v1/data/core/quote/TSLA?token=pk_de14c32c30a64c2f8475eab0ab4fa2bb"
etf_site_raw = requests.get(etf_url)
etf_site_html = html.fromstring(etf_site_raw.content)
etf_site_html_string = html.tostring(etf_site_html)
etf_data = etf_site_raw.json()
print(etf_data[0]["latestPrice"])

nasdaq_api_key = "Auypjg3JddJmeUkpspuh"
import nasdaqdatalink
nasdaqdatalink.ApiConfig.api_key = nasdaq_api_key
mydata = nasdaqdatalink.get_table('ZACKS/FC', ticker='AE50')
print(mydata)


