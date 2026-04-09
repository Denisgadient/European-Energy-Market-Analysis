import pandas as pd
import statsmodels.api as sm
import os

# 1. Daten laden
pwr = pd.read_csv('data/power_prices.csv', index_col=0, parse_dates=True)
mkt = pd.read_csv('data/market_fundamentals.csv', index_col=0, parse_dates=True)
df = pwr.join(mkt).dropna()

# 2. Modell definieren: Strompreis erklärt durch Gas und CO2
# Wir nutzen robuste Standardfehler (HC1), um Zeitreihen-Verzerrungen zu korrigieren
X = df[['gas_ttf', 'co2_eua']]
X = sm.add_constant(X)
y = df['pwr_de_da']

model = sm.OLS(y, X).fit(cov_type='HC1') 

# 3. Ergebnisse in Datei speichern
os.makedirs('outputs', exist_ok=True)
with open('outputs/model_summary.txt', 'w') as f:
    f.write(model.summary().as_text())

print("\n--- INSTITUTIONAL MODEL SUMMARY ---")
print(f"Gas Beta: {model.params['gas_ttf']:.2f} (Bedeutet: +1€ Gas => +{model.params['gas_ttf']:.2f}€ Strom)")
print(f"CO2 Beta: {model.params['co2_eua']:.2f}")
print(f"Modell-Güte (R2): {model.rsquared:.2f}")
print("\nDetaillierter Report unter 'outputs/model_summary.txt' gespeichert.")
