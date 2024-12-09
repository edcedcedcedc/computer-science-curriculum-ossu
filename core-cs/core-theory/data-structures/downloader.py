import os
import sys
import requests
from bs4 import BeautifulSoup


try:
    url = f"{sys.argv[1]}"
    output_dir = f"{sys.argv[2]}"

    os.makedirs(output_dir, exist_ok=True)

    response = requests.get(url)

except Exception as e:
    print(e); exit()

soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a'):
    file_name = link.get('href')
    

    if file_name in ("../", "/") or file_name.endswith('/'):
        continue
    
    file_url = url + file_name
    print(f"Downloading {file_name}...")
    
    try:

        file_response = requests.get(file_url)
        file_response.raise_for_status()
        
        with open(os.path.join(output_dir, file_name), 'wb') as f:
            f.write(file_response.content)
            
    except Exception as e:
        print(f"Failed to download {file_name}: {e}")

print("All files downloaded.")
