import yfinance as yf
import pandas as pd
import os

def fetch_market_data(start_date="2023-01-01"):
    # Ticker: TTF Gas (TTF=F) und CO2 Zertifikate (CFI.PA)
    tickers = {
        "TTF=F": "gas_ttf",
        "CFI.PA": "co2_eua"
    }
    
    print("Lade Marktdaten von Yahoo Finance...")
    data = yf.download(list(tickers.keys()), start=start_date)['Close']
    
    # Spalten umbenennen
    data = data.rename(columns=tickers)
    
    # Lücken füllen (Wochenenden/Feiertage) mit Forward-Fill
    data = data.ffill()
    
    # In CSV speichern
    os.makedirs('data', exist_ok=True)
    data.to_csv('data/market_fundamentals.csv')
    print("Erfolg: Marktdaten unter 'data/market_fundamentals.csv' gespeichert.")
    return data

if __name__ == "__main__":
    fetch_market_data()
