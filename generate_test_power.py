import pandas as pd
import numpy as np

def generate_power_prices():
    # Lade die bereits heruntergeladenen Fundamentaldaten
    mkt = pd.read_csv('data/market_fundamentals.csv', index_col=0, parse_dates=True)
    
    # Simuliere Strompreis basierend auf Grenzkosten-Logik:
    # Strom ≈ (Gas * 2) + (CO2 * 0.4) + Grundlast-Rauschen
    np.random.seed(42)
    noise = np.random.normal(0, 10, len(mkt))
    pwr_prices = (mkt['gas_ttf'] * 2.1) + (mkt['co2_eua'] * 0.38) + 20 + noise
    
    df_pwr = pd.DataFrame({'pwr_de_da': pwr_prices}, index=mkt.index)
    df_pwr.to_csv('data/power_prices.csv')
    print("Erfolg: Test-Strompreise unter 'data/power_prices.csv' gespeichert.")

if __name__ == "__main__":
    generate_power_prices()
