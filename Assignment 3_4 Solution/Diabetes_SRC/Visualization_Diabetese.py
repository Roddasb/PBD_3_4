#Question 2 A 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("/content/diabetes.csv")

# Set seed for reproducibility
np.random.seed(42)

# Take a random sample of 25 observations
sample = data.sample(n=25)

# Calculate mean glucose values for sample
sample_mean_glucose = sample['Glucose'].mean()
print('sample_mean_glucose:', sample_mean_glucose)

# Calculate the highest glucose value for the sample
sample_highest_glucose = sample['Glucose'].max()
print('Sample Highest Glucose Values:', sample_highest_glucose)

# Calculate mean glucose values for population
population_mean_glucose = data['Glucose'].mean()
print('population_mean_glucose:', population_mean_glucose)

# Calculate the highest glucose value for the population
population_highest_glucose = data['Glucose'].max()
print('population_highest_glucose:', population_highest_glucose)

# Visualize the comparison using scatter plots

# Scatter plot for mean glucose values
plt.figure(figsize=(10, 6))
plt.bar(['Sample', 'Population'], [sample_mean_glucose, population_mean_glucose], color=['blue', 'orange'], label='Mean Glucose')
plt.title('Mean Glucose Comparison')
plt.xlabel('Dataset')
plt.ylabel('Mean Glucose')
plt.legend()
plt.show()

# Scatter plot for highest glucose values
plt.figure(figsize=(10, 6))
plt.bar(['Sample', 'Population'], [sample_highest_glucose, population_highest_glucose], color=['blue', 'orange'], label='Highest Glucose')
plt.title('Highest Glucose Comparison')
plt.xlabel('Dataset')
plt.ylabel('Highest Glucose')
plt.legend()
plt.show()


#Question 2B

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("/content/diabetes.csv")

# Set seed for reproducibility
np.random.seed(42)

# Take a random sample of 25 observations
sample = data.sample(n=25)

# Calculate the 98th percentile of BMI for the sample
sample_98th_percentile_bmi = np.percentile(sample['BMI'], 98)
print('98th Percentile BMI (Sample):', sample_98th_percentile_bmi)

# Calculate the 98th percentile of BMI for the population
population_98th_percentile_bmi = np.percentile(data['BMI'], 98)
print('98th Percentile BMI (Population):', population_98th_percentile_bmi)

# Visualize the comparison using charts

# Bar chart for 98th percentile of BMI
plt.figure(figsize=(10, 6))
plt.bar(['Sample', 'Population'], [sample_98th_percentile_bmi, population_98th_percentile_bmi], color=['blue', 'orange'])
plt.title('98th Percentile BMI Comparison')
plt.xlabel('Dataset')
plt.ylabel('98th Percentile BMI')
plt.show()



'''Question 2 C) Using bootstrap (replace= True), create 500 samples (of 150 observation each) from the population and find the average mean, standard deviation and percentile for
BloodPressure and compare this with these statistics from the population for the same variable. Again, you should create charts for this comparison. Report on your findings.  (10 points)
 '''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv("/content/diabetes.csv")  # Replace "your_file.csv" with the actual path to your CSV file
blood_pressure_data = data["BloodPressure"].values

# Number of bootstrap samples and sample size
n_bootstrap_samples = 500
sample_size = 150

# Arrays to store statistics from bootstrap samples
bootstrap_means = np.zeros(n_bootstrap_samples)
bootstrap_stds = np.zeros(n_bootstrap_samples)
bootstrap_percentiles = np.zeros((n_bootstrap_samples, 5))  # 5 percentiles: 0, 25, 50, 75, 100

# Generate bootstrap samples and calculate statistics
for i in range(n_bootstrap_samples):
    # Generate bootstrap sample with replacement
    bootstrap_sample = np.random.choice(blood_pressure_data, size=sample_size, replace=True)

    # Calculate mean, standard deviation, and percentiles
    bootstrap_means[i] = np.mean(bootstrap_sample)
    bootstrap_stds[i] = np.std(bootstrap_sample)
    bootstrap_percentiles[i] = np.percentile(bootstrap_sample, [0, 25, 50, 75, 100])

# Calculate average statistics across all bootstrap samples
average_mean = np.mean(bootstrap_means)
average_std = np.mean(bootstrap_stds)
average_percentiles = np.mean(bootstrap_percentiles, axis=0)

# Print statistics
print("Average Mean (Bootstrap):", average_mean)
print("Average Standard Deviation (Bootstrap):", average_std)
print("Average Percentiles (Bootstrap):", average_percentiles)

# Plot histograms of bootstrap means and percentiles
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(bootstrap_means, bins=30, color='skyblue', edgecolor='black')
plt.axvline(x=average_mean, color='red', linestyle='--', label='Average Mean')
plt.xlabel('Mean Blood Pressure')
plt.ylabel('Frequency')
plt.title('Distribution of Bootstrap Means')
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(bootstrap_percentiles[:, 2], bins=30, color='lightgreen', edgecolor='black')
plt.axvline(x=average_percentiles[2], color='red', linestyle='--', label='Average Median')
plt.xlabel('Median Blood Pressure')
plt.ylabel('Frequency')
plt.title('Distribution of Bootstrap Medians')
plt.legend()

plt.tight_layout()
plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv("/content/diabetes.csv")  # Replace "your_file.csv" with the actual path to your CSV file
population_blood_pressure = data["BloodPressure"].values

# Number of bootstrap samples and sample size
n_bootstrap_samples = 500
sample_size = 150

# Arrays to store statistics from bootstrap samples
bootstrap_means = np.zeros(n_bootstrap_samples)
bootstrap_stds = np.zeros(n_bootstrap_samples)
bootstrap_percentiles = np.zeros((n_bootstrap_samples, 5))  # 5 percentiles: 0, 25, 50, 75, 100

# Generate bootstrap samples and calculate statistics
for i in range(n_bootstrap_samples):
    # Generate bootstrap sample with replacement
    bootstrap_sample = np.random.choice(population_blood_pressure, size=sample_size, replace=True)

    # Calculate mean, standard deviation, and percentiles
    bootstrap_means[i] = np.mean(bootstrap_sample)
    bootstrap_stds[i] = np.std(bootstrap_sample)
    bootstrap_percentiles[i] = np.percentile(bootstrap_sample, [0, 25, 50, 75, 100])

# Calculate average statistics across all bootstrap samples
average_bootstrap_mean = np.mean(bootstrap_means)
average_bootstrap_std = np.mean(bootstrap_stds)
average_bootstrap_percentiles = np.mean(bootstrap_percentiles, axis=0)

# Calculate statistics from the population
population_mean = np.mean(population_blood_pressure)
population_std = np.std(population_blood_pressure)
population_percentiles = np.percentile(population_blood_pressure, [0, 25, 50, 75, 100])

# Print statistics
print("Average Mean (Bootstrap):", average_bootstrap_mean)
print("Average Standard Deviation (Bootstrap):", average_bootstrap_std)
print("Average Percentiles (Bootstrap):", average_bootstrap_percentiles)
print("Population Mean:", population_mean)
print("Population Standard Deviation:", population_std)
print("Population Percentiles:", population_percentiles)

# Plot comparison of means
plt.figure(figsize=(10, 6))
plt.hist(bootstrap_means, bins=30, color='skyblue', alpha=0.7, label='Bootstrap Sample Means')
plt.axvline(x=population_mean, color='red', linestyle='--', label='Population Mean')
plt.xlabel('Mean Blood Pressure')
plt.ylabel('Frequency')
plt.title('Comparison of Mean Blood Pressure')
plt.legend()
plt.show()

# Plot comparison of standard deviations
plt.figure(figsize=(10, 6))
plt.hist(bootstrap_stds, bins=30, color='lightgreen', alpha=0.7, label='Bootstrap Sample Standard Deviations')
plt.axvline(x=population_std, color='red', linestyle='--', label='Population Standard Deviation')
plt.xlabel('Standard Deviation of Blood Pressure')
plt.ylabel('Frequency')
plt.title('Comparison of Standard Deviation of Blood Pressure')
plt.legend()
plt.show()

# Plot comparison of percentiles
percentile_labels = ['0%', '25%', '50%', '75%', '100%']
plt.figure(figsize=(10, 6))
for i in range(5):
    plt.hist(bootstrap_percentiles[:, i], bins=30, alpha=0.5, label=f'Bootstrap Sample Percentile {percentile_labels[i]}')
plt.plot(percentile_labels, population_percentiles, marker='o', color='red', linestyle='--', label='Population Percentiles')
plt.xlabel('Percentiles of Blood Pressure')
plt.ylabel('Frequency')
plt.title('Comparison of Blood Pressure Percentiles')
plt.legend()
plt.show()