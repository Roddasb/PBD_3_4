import pandas as pd
import numpy as np

# Read the CSV file
data = pd.read_csv("/content/diabetes.csv")

# Data cleaning
# Replace 0 values in the "Glucose" column with NaN
data['Glucose'].replace(0, np.nan, inplace=True)

# Drop rows with missing values in the "Glucose" column
cleaned_data = data.dropna(subset=['Glucose'])

# Save the cleaned DataFrame to a new CSV file
cleaned_data.to_csv("/content/cleaned_diabetes.csv", index=False)
