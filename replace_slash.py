import pandas as pd

# Read the CSV file
df = pd.read_csv('datasets.csv')

# Replace all "/" with "-" in the 'Name' and 'Link' columns
df['Name'] = df['Name'].str.replace('/', '-', regex=False)

# Save the modified DataFrame to a new CSV file
df.to_csv('output.csv', index=False)

print("CSV file updated successfully!")
