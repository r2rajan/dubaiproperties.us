import matplotlib.pyplot as plt
import numpy as np
# categorize tiers
def categorize_tier(price):
    if price <= 100:
        return "Tier 3"
    elif 101 <= price <= 125:
        return "Tier 2"
    else:
        return "Tier 1"
# Input data
data = [
    ("Al-Barsha South", 350),
    ("Al-Furjan", 300),
    ("Al-Jaddaf", 350),
    ("BlueWaters Island", 950),
    ("Business Bay", 500),
    ("CityWalk", 500),
    ("DAMAC Hills (Apartments)", 300),
    ("DIFC", 480),
    ("Discovery Gardens", 350),
    ("Downtown Dubai", 450),
    ("Dubai Hills", 400),
    ("Dubai South", 299),
    ("Festival City", 279),
    ("Greens", 430),
    ("JVT/JVC", 330),
    ("JBR", 450),
    ("Jumeirah Lake Towers (JLT)", 400),
    ("MBR City", 300),
    ("Madinat Jumeirah", 500),
    ("Dubai Marina", 500),
    ("Meydan", 400),
    ("Palm Jumeirah", 550),
    ("Ras-al-Khor", 300),
    ("Silicon Oasis", 300),
    ("Sports city", 300),
    ("TECOM", 320),
]

# Conversion rate for AED to USD
aed_to_usd = 0.27

# Create a DataFrame
df = pd.DataFrame(data, columns=["Location", "Price (AED)"])

# Add a USD column
df["Price (USD)"] = df["Price (AED)"] * aed_to_usd

# Sort the data by location alphabetically
df = df.sort_values(by="Location").reset_index(drop=True)

# Sort the data by price in ascending order
df_sorted = df.sort_values(by="Price (AED)").reset_index(drop=True)

df_sorted["Tier"] = df_sorted["Price (USD)"].apply(categorize_tier)

df_sorted

import matplotlib.pyplot as plt
import numpy as np

# Data
locations = [
    "Festival City", "Dubai South", "Al-Furjan", "Silicon Oasis",
    "Ras-al-Khor", "MBR City", "DAMAC Hills (Apartments)", "Sports city",
    "TECOM", "JVT/JVC", "Al-Barsha South", "Al-Jaddaf", "Discovery Gardens",
    "Meydan", "Jumeirah Lake Towers (JLT)", "Dubai Hills", "Greens", "JBR",
    "Downtown Dubai", "DIFC", "CityWalk", "Business Bay", "Madinat Jumeirah",
    "Dubai Marina", "Palm Jumeirah"
]

prices_aed = [
    279, 299, 300, 300, 300, 300, 300, 300, 320, 330, 350, 350, 350,
    400, 400, 400, 430, 450, 450, 480, 500, 500, 500, 500, 550
]

# Conversion rate: 1 AED = 0.27 USD
prices_usd = [price * 0.27 for price in prices_aed]

# Bar width for side-by-side comparison
bar_width = 0.4
index = np.arange(len(locations))

# Plotting
plt.figure(figsize=(14, 10))
plt.barh(index - bar_width / 2, prices_aed, bar_width, label="Price (AED)", color='skyblue', edgecolor='black')
plt.barh(index + bar_width / 2, prices_usd, bar_width, label="Price (USD)", color='lightgreen', edgecolor='black')

# Add labels, title, and legend
plt.xlabel("Price", fontsize=12)
plt.yticks(index, locations, fontsize=10)
plt.title("Short term rental per night Prices by Location (AED and USD)", fontsize=14)
plt.legend(loc="upper right")

# Adjust layout and display
plt.tight_layout()
plt.show()
