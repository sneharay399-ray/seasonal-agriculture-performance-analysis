"""
Generates an original synthetic dataset for the Seasonal Agriculture
Performance Analysis project. All values are simulated for the purpose
of this project and are not sourced from any external dataset.
"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

N = 2600

SEASONS = ["Kharif", "Rabi", "Zaid"]
SEASON_P = [0.42, 0.38, 0.20]

CROPS = ["Rice", "Wheat", "Maize", "Soybean", "Mustard",
         "Barley", "Sugarcane", "Groundnut"]

STATES = ["West Bengal", "Bihar", "Uttar Pradesh", "Odisha",
          "Assam", "Jharkhand", "Chhattisgarh", "Punjab"]

IRRIGATION = ["Canal", "Borewell", "Rainfed", "Drip", "Sprinkler"]

SOIL_TYPES = ["Alluvial", "Loamy", "Clay", "Sandy", "Black"]

SEED_VARIETY = ["High-Yield Variety", "Traditional"]

FARM_SIZE = ["Small", "Medium", "Large"]

season = rng.choice(SEASONS, size=N, p=SEASON_P)
crop = rng.choice(CROPS, size=N)
state = rng.choice(STATES, size=N)
irrigation = rng.choice(IRRIGATION, size=N, p=[0.28, 0.22, 0.22, 0.16, 0.12])
soil_type = rng.choice(SOIL_TYPES, size=N)
seed_variety = rng.choice(SEED_VARIETY, size=N, p=[0.62, 0.38])
farm_size = rng.choice(FARM_SIZE, size=N, p=[0.5, 0.33, 0.17])
year = rng.choice([2021, 2022, 2023, 2024], size=N)

# Season-driven base effects (own parameterisation)
season_yield_base = {"Kharif": 5.2, "Rabi": 4.6, "Zaid": 3.6}
season_rain_base = {"Kharif": 780, "Rabi": 210, "Zaid": 95}
season_temp_base = {"Kharif": 28.5, "Rabi": 21.0, "Zaid": 33.5}
season_humidity_base = {"Kharif": 78, "Rabi": 58, "Zaid": 45}
season_disease_base = {"Kharif": 0.42, "Rabi": 0.24, "Zaid": 0.31}
season_cost_base = {"Kharif": 46000, "Rabi": 41000, "Zaid": 39000}
season_price_base = {"Kharif": 1850, "Rabi": 2050, "Zaid": 1700}

crop_yield_mult = {
    "Rice": 1.05, "Wheat": 0.95, "Maize": 1.15, "Soybean": 0.75,
    "Mustard": 0.55, "Barley": 0.85, "Sugarcane": 6.5, "Groundnut": 0.7,
}

area = np.round(rng.gamma(shape=3.0, scale=0.7, size=N) + 0.3, 2)

rainfall = np.array([season_rain_base[s] for s in season]) + rng.normal(0, 60, N)
rainfall = np.clip(rainfall, 5, None)

temperature = np.array([season_temp_base[s] for s in season]) + rng.normal(0, 2.2, N)
humidity = np.array([season_humidity_base[s] for s in season]) + rng.normal(0, 6, N)
humidity = np.clip(humidity, 15, 95)

soil_ph = np.round(rng.normal(6.6, 0.5, N), 2)
fertilizer = np.round(rng.normal(120, 30, N) + (season == "Kharif") * 15, 1)
fertilizer = np.clip(fertilizer, 20, None)
pesticide = np.round(rng.normal(3.2, 1.1, N) + (season == "Kharif") * 0.6, 2)
pesticide = np.clip(pesticide, 0.1, None)

labor_hours = np.round(rng.normal(310, 70, N), 0)

irrigation_water_mult = {
    "Canal": 1.0, "Borewell": 1.1, "Rainfed": 0.55, "Drip": 0.65, "Sprinkler": 0.8
}
water_usage = np.array([irrigation_water_mult[i] for i in irrigation]) * (
    rainfall * 0.35 + rng.normal(250, 40, N)
)
water_usage = np.clip(water_usage, 50, None)

base_yield = np.array([season_yield_base[s] for s in season]) * np.array(
    [crop_yield_mult[c] for c in crop]
)
irrigation_yield_bonus = {
    "Drip": 1.18, "Sprinkler": 1.10, "Canal": 1.05, "Borewell": 1.0, "Rainfed": 0.82
}
yield_noise = rng.normal(0, 0.35, N)
yield_tonnes_per_ha = np.clip(
    base_yield * np.array([irrigation_yield_bonus[i] for i in irrigation])
    + (soil_ph.clip(6, 7.5) - 6) * 0.4
    + yield_noise,
    0.2, None,
)

production = np.round(yield_tonnes_per_ha * area, 2)

disease_incidence = np.clip(
    np.array([season_disease_base[s] for s in season]) * 100
    + rng.normal(0, 8, N) - (seed_variety == "High-Yield Variety") * 4,
    2, 95,
)
pest_incidence = np.clip(disease_incidence * rng.uniform(0.6, 1.1, N), 1, 95)

storage_loss = np.clip(rng.normal(6.5, 2.5, N) + (farm_size == "Small") * 1.2, 0.5, 25)

market_price = np.array([season_price_base[s] for s in season]) + rng.normal(0, 150, N)
market_price = np.clip(market_price, 500, None)

revenue = np.round(production * market_price * (1 - storage_loss / 100), 2)

cost = np.round(
    np.array([season_cost_base[s] for s in season]) * area
    + fertilizer * 15
    + pesticide * 400
    + water_usage * 2.5
    + labor_hours * 22
    + rng.normal(0, 4000, N),
    2,
)

profit = np.round(revenue - cost, 2)

water_efficiency = np.round(yield_tonnes_per_ha / (water_usage / 100), 3)

df = pd.DataFrame({
    "Record_ID": np.arange(1, N + 1),
    "Year": year,
    "Season": season,
    "Crop": crop,
    "State": state,
    "Farm_Size_Category": farm_size,
    "Area_Hectares": area,
    "Soil_Type": soil_type,
    "Soil_pH": soil_ph,
    "Seed_Variety": seed_variety,
    "Irrigation_Method": irrigation,
    "Rainfall_mm": np.round(rainfall, 1),
    "Temperature_C": np.round(temperature, 1),
    "Humidity_pct": np.round(humidity, 1),
    "Fertilizer_kg_per_ha": fertilizer,
    "Pesticide_kg_per_ha": pesticide,
    "Water_Usage_mm": np.round(water_usage, 1),
    "Water_Efficiency": water_efficiency,
    "Labor_Hours_per_ha": labor_hours,
    "Yield_tonnes_per_ha": np.round(yield_tonnes_per_ha, 3),
    "Production_tonnes": production,
    "Market_Price_per_ton": np.round(market_price, 1),
    "Storage_Loss_pct": np.round(storage_loss, 2),
    "Revenue_INR": revenue,
    "Cost_INR": cost,
    "Profit_INR": profit,
    "Disease_Incidence_pct": np.round(disease_incidence, 1),
    "Pest_Incidence_pct": np.round(pest_incidence, 1),
})

# Inject realistic messiness: missing values + duplicates, so the
# notebook has genuine cleaning work to do.
missing_cols = ["Rainfall_mm", "Soil_pH", "Fertilizer_kg_per_ha",
                "Yield_tonnes_per_ha", "Market_Price_per_ton", "Irrigation_Method"]
for col in missing_cols:
    n_missing = int(N * rng.uniform(0.015, 0.035))
    idx = rng.choice(df.index, size=n_missing, replace=False)
    df.loc[idx, col] = np.nan

dup_idx = rng.choice(df.index, size=25, replace=False)
df = pd.concat([df, df.loc[dup_idx]], ignore_index=True)
df = df.sample(frac=1, random_state=7).reset_index(drop=True)
df["Record_ID"] = np.arange(1, len(df) + 1)

df.to_csv("/home/claude/project/seasonal_agriculture_dataset.csv", index=False)
print(df.shape)
print(df.isna().sum().sum(), "missing values injected")
