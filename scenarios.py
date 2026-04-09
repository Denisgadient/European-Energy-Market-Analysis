import pandas as pd
import os

# Wir nutzen die Betas aus deinem erfolgreichen Modell-Run
beta_gas = 2.06
beta_co2 = 0.22
intercept = 20.0  # Geschätzter Basispreis aus dem Modell

def run_scenarios():
    scenarios = {
        "Status Quo": {"gas": 30, "co2": 70},
        "Gas-Schock (+50%)": {"gas": 45, "co2": 70},
        "CO2-Rally (+20%)": {"gas": 30, "co2": 84},
        "Stress-Szenario (Heiß/Teuer)": {"gas": 50, "co2": 90}
    }
    
    results = []
    for name, inputs in scenarios.items():
        predicted_pwr = intercept + (inputs['gas'] * beta_gas) + (inputs['co2'] * beta_co2)
        results.append({
            "Szenario": name,
            "Gas-Preis": inputs['gas'],
            "CO2-Preis": inputs['co2'],
            "Proj. Strompreis": round(predicted_pwr, 2)
        })
    
    df_scenarios = pd.DataFrame(results)
    os.makedirs('outputs', exist_ok=True)
    df_scenarios.to_csv('outputs/scenarios_results.csv', index=False)
    
    print("\n--- STRATEGISCHE SZENARIO-ANALYSE ---")
    print(df_scenarios.to_string(index=False))
    print("\nErgebnisse unter 'outputs/scenarios_results.csv' gespeichert.")

if __name__ == "__main__":
    run_scenarios()
