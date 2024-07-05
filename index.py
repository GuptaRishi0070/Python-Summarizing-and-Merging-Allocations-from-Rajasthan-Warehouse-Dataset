import pandas as pd
from collections import defaultdict

# Title: Summarizing and Merging Allocations from Rajasthan Warehouse Dataset

# Load the dataset
file_path = 'C:/Users/Rishi/Desktop/Rajasthan/Rajasthan_WH.xlsx'
data = pd.read_excel(file_path, sheet_name="FPS")
print(data.columns)

# Create a defaultdict to store summed allocations
allocation_dict = defaultdict(int)

# Iterate over the rows of the dataframe to sum allocations by latitude and longitude
for index, row in data.iterrows():
    lat_long = (row['FPS_Latitude'], row['FPS_Longitude'])
    allocation_dict[lat_long] += row['August 2024 Allotment (K.G.)']

# Convert the dictionary to a DataFrame
allocation_df = pd.DataFrame(
    [(lat, long, allocation) for (lat, long), allocation in allocation_dict.items()],
    columns=['FPS_Latitude', 'FPS_Longitude', 'Summed_Allocation']
)

# Merge the summed allocations back into the original DataFrame
merged_df = pd.merge(data, allocation_df, on=['FPS_Latitude', 'FPS_Longitude'], how='left')

# Drop duplicates based on latitude and longitude
final_df = merged_df.drop_duplicates(subset=['FPS_Latitude', 'FPS_Longitude'])

# Save the DataFrame to an Excel file
output_file_path = 'fci_data_with_all_columns.xlsx'
final_df.to_excel(output_file_path, index=False)

print(f"Data successfully written to {output_file_path}")
