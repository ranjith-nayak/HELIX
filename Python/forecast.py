import pandas as pd
from prophet import Prophet

# ============================
# STEP 1: Load Monthly Revenue
# ============================

file_path = r"C:\Users\user\Desktop\Helix\Forecasting(ML)\monthly_revenue.csv"

df = pd.read_csv(file_path)

# Rename columns for Prophet
df.columns = ["ds", "y"]

# Convert Month column to Date
df["ds"] = pd.to_datetime(df["ds"])

# Sort data
df = df.sort_values("ds")

# Display first few rows
print(df.head())

# ============================
# STEP 2: Train Prophet Model
# ============================

model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=False,
    daily_seasonality=False
)

model.fit(df)

# ============================
# STEP 3: Forecast Next 12 Months
# ============================

future = model.make_future_dataframe(
    periods=12,
    freq="MS"
)

forecast = model.predict(future)

# ============================
# STEP 4: Keep Required Columns
# ============================

forecast_output = forecast[
    [
        "ds",
        "yhat",
        "yhat_lower",
        "yhat_upper"
    ]
]

# ============================
# STEP 5: Save Forecast
# ============================

output_path = r"C:\Users\user\Desktop\Helix\Forecasting(ML)\forecast.csv"

forecast_output.to_csv(output_path, index=False)

print("\n===================================")
print("Forecast generated successfully!")
print("Saved to:")
print(output_path)
print("===================================")