import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque

# Base website
base_url = "https://www.pbs.gov.pk/"

# Directory to save PDFs
pdf_dir = "pbs_pdfs"
os.makedirs(pdf_dir, exist_ok=True)

# To keep track of visited pages
visited = set()
queue = deque([base_url])  # BFS queue

# Store found PDF links
pdf_links = set()

while queue:
    url = queue.popleft()

    # Skip if already visited
    if url in visited:
        continue
    visited.add(url)

    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            continue

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all links
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(url, href)

            # Check if it's a PDF
            if full_url.endswith('.pdf'):
                if full_url not in pdf_links:
                    pdf_links.add(full_url)

                    # Download the PDF
                    try:
                        pdf_response = requests.get(full_url, stream=True, timeout=10)
                        if pdf_response.status_code == 200:
                            filename = os.path.join(pdf_dir, os.path.basename(full_url))
                            with open(filename, "wb") as f:
                                for chunk in pdf_response.iter_content(chunk_size=1024):
                                    f.write(chunk)
                            print(f"✅ Downloaded: {filename}")
                    except requests.RequestException:
                        print(f"❌ Failed to download: {full_url}")

            else:
                # Ensure it's an internal PBS link (avoid external sites)
                if urlparse(full_url).netloc == urlparse(base_url).netloc:
                    queue.append(full_url)

    except requests.RequestException:
        continue

# Save found PDFs to a file
with open("pbs_pdfs.txt", "w") as file:
    for pdf in pdf_links:
        file.write(pdf + "\n")

print("\n🎉 All PDFs downloaded successfully! Check the 'pbs_pdfs' folder.")
