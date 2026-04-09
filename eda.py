import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Verzeichnisse erstellen
os.makedirs('outputs/figures', exist_ok=True)

# 1. Daten laden und mergen
pwr = pd.read_csv('data/power_prices.csv', index_col=0, parse_dates=True)
mkt = pd.read_csv('data/market_fundamentals.csv', index_col=0, parse_dates=True)
df = pwr.join(mkt).dropna()

# 2. Korrelationsmatrix
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='RdYlGn', center=0)
plt.title('Korrelationsmatrix: Strom, Gas & CO2')
plt.savefig('outputs/figures/correlation_matrix.png')

# 3. Preis-Entwicklung Plot
fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.plot(df.index, df['pwr_de_da'], color='blue', label='Strom DE DA (EUR/MWh)')
ax1.set_ylabel('Strompreis', color='blue')

ax2 = ax1.twinx()
ax2.plot(df.index, df['gas_ttf'], color='orange', label='TTF Gas (EUR/MWh)', alpha=0.7)
ax2.set_ylabel('Gaspreis', color='orange')

plt.title('Markt-Monitoring: Strom vs. Gas')
plt.savefig('outputs/figures/price_trends.png')
print("EDA abgeschlossen. Charts unter 'outputs/figures/' gespeichert.")
