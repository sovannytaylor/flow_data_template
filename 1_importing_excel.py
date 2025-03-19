import os
import matplotlib.pyplot as plt
import pandas as pd
from loguru import logger

logger.info('Import ok')

input_folder = 'raw_data'
output_folder = 'python_results/excel_clean_up/'

if not os.path.exists(output_folder):
    os.mkdir(output_folder)


# List all Excel files in the folder (assuming only one Excel file)
input_files = [f for f in os.listdir(input_folder) if f.endswith('.xlsx')]

input_file = input_files[0]  # Get the only Excel file name
file_path = os.path.join(input_folder, input_file)  # Construct the full path

# Load all sheets from the selected Excel file into a dictionary of DataFrames because I put each experiment on a different sheet 
sheets_dict = pd.read_excel(file_path, sheet_name=None)

# Add a column to each dataframe that indicates the sheet name/ replicate
for sheet_name, df in sheets_dict.items():
    df['Sheet'] = sheet_name 

logger.info('Sheet added as a column')

# Merge it into a new dataframe 
merged_df = pd.concat(sheets_dict.values(), ignore_index=True)

# Define file name
output_file = 'merged_data.xlsx'

# Combine the folder and file name to create the full path
output_path = os.path.join(output_folder, output_file)

# Save the DataFrame to the specified path
merged_df.to_excel(output_path, index=False)

logger.info('Excel merged and imported successfully')

