# European Energy Market Analysis
A quantitative framework to model and forecast German Day-Ahead power prices based on TTF Gas and EUA Carbon fundamentals.

## Overview
This project quantifies the marginal cost drivers of the European electricity market using OLS regression. It maps fuel prices to power price volatility.

### Key Features
* **Automated Pipeline:** Data fetching via Yahoo Finance.
* **Econometric Modeling:** OLS regression with `HC1` robust standard errors.
* **Scenario Engine:** Quantitative stress-testing for market regimes.

## Statistics & Results
* **Gas Sensitivity (Beta):** `2.06`
* **Model Fit (R2):** `0.77`
* **Stress Test:** Forecasts **142.80 EUR/MWh** (High-Gas/High-CO2).

## Project Structure
* `/data`: Market time-series (CSV).
* `/outputs`: Regression summaries and forecast tables.
* `model.py`: Core statistical logic.
* `scenarios.py`: Simulation and stress-testing.
