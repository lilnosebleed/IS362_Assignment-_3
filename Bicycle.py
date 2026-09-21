import pandas as pd

# 1. Create a list of the cumulative odometer readings (Day 1 through Day 7)
odometer_readings = [55, 120, 185, 260, 335, 410, 490]

# 2. Create the pandas object
cumulative_series = pd.Series(odometer_readings, name="Cumulative Miles")

# 3. Calculate the miles done each day
# .diff() subtracts the previous row from the current row. /.fillna() is used so Day 1 data can be initialized without losing the value.
daily_miles = cumulative_series.diff().fillna(cumulative_series[0])

# 4. Displaying Results
print("--- Cumulative Odometer Readings ---")
print(cumulative_series)

print("\n--- Miles Ridden Each Individual Day ---")
print(daily_miles)
