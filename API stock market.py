import yfinance as yf
import pandas as pd
import tkinter as tk
from tkinter import ttk

# List of Indian stock tickers (Yahoo Finance tickers)
indian_stocks = {
    'Reliance Industries': 'RELIANCE.NS',
    'Tata Consultancy Services': 'TCS.NS',
    'Infosys': 'INFY.NS',
    'HDFC Bank': 'HDFCBANK.NS',
    'ICICI Bank': 'ICICIBANK.NS'
}

# Function to get live price of a stock
def get_live_price(ticker):
    stock = yf.Ticker(ticker)
    todays_data = stock.history(period='1d')
    return todays_data['Close'][0]

# Function to fetch and display the stock price
def fetch_price():
    company = search_var.get()
    ticker = indian_stocks.get(company)
    if ticker:
        try:
            price = get_live_price(ticker)
            result_var.set(f'The current price of {company} ({ticker}) is {price}')
        except Exception as e:
            result_var.set(f'Could not fetch data for {company}. Error: {e}')
    else:
        result_var.set('Company not found.')

# GUI setup
root = tk.Tk()
root.title('Indian Stock Market Live Prices')

tk.Label(root, text='Enter Company Name:').pack(pady=10)

search_var = tk.StringVar()
search_entry = ttk.Combobox(root, textvariable=search_var)
search_entry['values'] = list(indian_stocks.keys())
search_entry.pack(pady=10)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, wraplength=400).pack(pady=10)

tk.Button(root, text='Get Live Price', command=fetch_price).pack(pady=10)

root.mainloop()
