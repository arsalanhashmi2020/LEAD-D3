import os
import csv

# Paths
csv_file_path = "datasets.csv"  # Path to the CSV containing Name and Link
downloaded_folder_path = "C:\\Users\\Arsalan Hashmi\\Desktop\\Semester 8\\RA Work\\datasets"  # Path to the folder of downloaded datasets
downloaded_csv_path = "Downloaded.csv"  # Output CSV for downloaded datasets
undownloaded_csv_path = "Undownloaded.csv"  # Output CSV for undownloaded datasets

# Load dataset information from the CSV
datasets = []
with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        datasets.append({"Name": row["Name"], "Link": row["Link"]})

# Get the list of downloaded dataset names (folder names)
downloaded_datasets = os.listdir(downloaded_folder_path)

# Prepare data for downloaded and undownloaded CSVs
downloaded = []
undownloaded = []

for dataset in datasets:
    dataset_name = dataset["Name"]
    dataset_link = dataset["Link"]
    
    # Check if dataset is downloaded
    if dataset_name in downloaded_datasets:
        file_path = os.path.join(downloaded_folder_path, dataset_name)
        downloaded.append({"Name": dataset_name, "Link": dataset_link, "File Path": file_path})
    else:
        undownloaded.append({"Name": dataset_name, "Link": dataset_link})

# Write the Downloaded.csv
with open(downloaded_csv_path, "w", newline="") as downloaded_file:
    fieldnames = ["Name", "Link", "File Path"]
    writer = csv.DictWriter(downloaded_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(downloaded)

# Write the Undownloaded.csv
with open(undownloaded_csv_path, "w", newline="") as undownloaded_file:
    fieldnames = ["Name", "Link"]
    writer = csv.DictWriter(undownloaded_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(undownloaded)

print("Comparison complete. CSV files created:")
print(f"- Downloaded: {downloaded_csv_path}")
print(f"- Undownloaded: {undownloaded_csv_path}")
