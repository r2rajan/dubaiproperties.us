import matplotlib.pyplot as plt
import numpy as np

# Data for tenants looking for apartments and villas/townhouses
apartment_furnishings = [65, 34]
villa_furnishings = [48, 51]

# Data for tenant preferences for apartment sizes
apartment_sizes = [35, 31, 24]  # One-bedroom, two-bedroom, studios

# Data for tenant preferences for villas
villa_sizes = [40, 38]  # Three-bedroom, Four-bedroom+

# Data for popular areas for renting apartments and villas
areas_apartments = ['JVC', 'Dubai Marina', 'Downtown Dubai', 'Business Bay', 'Deira']
areas_villas = ['Jumeirah', 'Dubai Hills Estate', 'Damac Hills 2', 'Al Barsha', 'Umm Suqeim']

# Plot for Furnishing Preferences (Apartments vs Villas)
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Apartment Furnishing Chart
ax[0].pie(apartment_furnishings, labels=['Furnished', 'Unfurnished'], autopct='%1.1f%%', startangle=90)
ax[0].set_title("Tenant Preferences for Apartment Furnishings")

# Villa Furnishing Chart
ax[1].pie(villa_furnishings, labels=['Furnished', 'Unfurnished'], autopct='%1.1f%%', startangle=90)
ax[1].set_title("Tenant Preferences for Villa Furnishings")

plt.tight_layout()

# Plot for Villa Sizes Preferences (3-Bedroom, 4-Bedroom+)
fig3, ax3 = plt.subplots(figsize=(8, 6))
villa_size_labels = ['3-Bedroom', '4-Bedroom+']
ax3.bar(villa_size_labels, villa_sizes, color=['blue', 'green'])
ax3.set_title("Tenant Preferences for Villa Sizes")
ax3.set_ylabel("Percentage (%)")
ax3.set_xlabel("Villa Size Type")

## Plot for Apartment Sizes Preferences (3-Bedroom, 4-Bedroom+)
fig3, ax3 = plt.subplots(figsize=(8, 6))
apartment_size_labels = ['1-Bedroom', '2-Bedroom+', 'studios']
ax3.bar(apartment_size_labels, apartment_sizes, color=['blue', 'green', 'orange'])
ax3.set_title("Tenant Preferences for Apartment Sizes")
ax3.set_ylabel("Percentage (%)")
ax3.set_xlabel("Apartment Size Type")

plt.tight_layout()
plt.show()
