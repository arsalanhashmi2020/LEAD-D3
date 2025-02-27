import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import datetime

# Load the CSV containing links and folder paths
links_df = pd.read_csv('Downloaded.csv')  # Replace with your actual CSV file path

# Define the correspondence between metadata and table fields
correspondence = {
    "Category": "Business Area",
    "Name": "Dataset Name",
    "Description": "Dataset Description",
    "Source": "Dataset Source",
    "Since": "Available Since",
    "Until": "Available Upto",
    "Last Refreshed": "Last Refresh Date",
    "Date Accessed": None,  # Will be filled with the current date
}

# Process each link and folder path
for _, row in links_df.iterrows():
    link = row['Link']  # Adjust column name as per your CSV
    folder_path = row['File Path']  # Adjust column name as per your CSV

    # Fetch the webpage
    response = requests.get(link)
    if response.status_code != 200:
        print(f"Failed to access {link}")
        continue

    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', id="report_R83904628546086563")
    if not table:
        print(f"No table found on {link}")
        continue

    # Extract metadata from the table
    metadata = {key: None for key in correspondence.keys()}
    metadata["Date Accessed"] = datetime.now().strftime("%Y-%m-%d")

    for tr in table.find_all('tr'):
        cells = tr.find_all('td')
        if len(cells) == 2:
            key_cell = cells[0].find(class_='L')
            value_cell = cells[1].find(class_='R')
            if key_cell and value_cell:
                key = key_cell.get_text(strip=True)
                value = value_cell.get_text(strip=True)
                for metadata_key, table_key in correspondence.items():
                    if table_key == key:
                        metadata[metadata_key] = value
                        break

    # Create a metadata DataFrame
    metadata_df = pd.DataFrame([metadata])

    # Ensure the folder exists
    os.makedirs(folder_path, exist_ok=True)

    # Save the metadata to a CSV in the folder
    metadata_csv_path = os.path.join(folder_path, "metadata.csv")
    metadata_df.to_csv(metadata_csv_path, index=False)

    print(f"Metadata saved to {metadata_csv_path}")
