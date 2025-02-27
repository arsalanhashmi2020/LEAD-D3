import os
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import shutil

# Path to the chromedriver executable
chromedriver_path = 'C:\\chromedriver\\chromedriver.exe'

# Configure Chrome options to specify download directory
chrome_options = Options()
download_dir = 'C:\\Users\\Arsalan Hashmi\\Desktop\\Semester 8\\RA Work\\datasets'  # Change to your desired download folder

# Set up Chrome preferences for automatic downloading
chrome_prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,  # Disable download prompt
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_argument('--headless')  # Run Chrome in headless mode
chrome_options.add_experimental_option("prefs", chrome_prefs)
# Setup chromedriver service and webdriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Read the CSV containing dataset names and links
csv_file = 'output.csv'  # Path to your CSV file
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        dataset_name = row['Name']
        print(dataset_name)
        dataset_link = row['Link']
        
        # Create a folder for each dataset
        dataset_folder = os.path.join(download_dir, dataset_name)
        if not os.path.exists(dataset_folder):
            os.makedirs(dataset_folder)

        # Navigate to the dataset link
        driver.get(dataset_link)

        try:
            # Wait for the download button to be clickable and click it
            btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'B2049812945457063'))
            )
            btn.click()
            print("Downloading...")

            # Wait for the download to complete
            time.sleep(30)  # Adjust the sleep time based on your internet speed and dataset size
        except Exception as e:
            print(f"Error downloading {dataset_name} from {dataset_link}: {e}")
            continue  # Skip to the next dataset if error occurs

        # Rename and move the downloaded file into the corresponding folder
        downloaded_file = os.path.join(download_dir, 'dataset.csv')  # The default name of the downloaded file
        if os.path.exists(downloaded_file):
            shutil.move(downloaded_file, os.path.join(dataset_folder, f'{dataset_name}.csv'))  
        else:
            print(f"File for {dataset_name} not found.")
        time.sleep(10)

driver.quit()
