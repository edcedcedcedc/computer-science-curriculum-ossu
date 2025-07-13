"""
MIT License

Copyright (c) 10-12-2024 Andro Ranogajec, @edcedcedcedc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
            
"""
import os
import sys
import requests
from bs4 import BeautifulSoup

def download(output_dir, response, url):
    soup = BeautifulSoup(response.text, 'html.parser')
    print(output_dir, response, url)
    for link in soup.find_all('a'):
        file_name = link.get('href')
        print('# Current filename: ', file_name)
        file_url = url + file_name

        if (file_name in ("../", "/") or 
           file_name.startswith("?") or 
           file_name.startswith("/")):
            continue
        
        elif file_name.endswith('/'):
            try:
                new_output_dir = output_dir + "/" + file_name.strip("/")
                new_url = file_url

                print(f"# New output directory: ", new_output_dir)
                print(f"# New output url: ", new_url)
                os.makedirs(new_output_dir, exist_ok=True)
                
                response = requests.get(new_url)
                if response.status_code == 200:
                    print("# Recursively calling myself...")
                    print(new_output_dir, response, new_url)
                    download(new_output_dir, response, new_url)
                    continue  
                else:
                    raise Exception(f"# Response status code: {response.status_code}")
                    
            except Exception as e:
                        print(e); exit()

        print(f"# Downloading {file_name}...")

        try:
            file_response = requests.get(file_url)
            file_response.raise_for_status()
           
            with open(os.path.join(output_dir, file_name), 'wb') as f:
                f.write(file_response.content)
                
        except Exception as e:
            print(f"# Failed to download, {e}, filename: {file_name}")

    print("# All files downloaded.")
   
try:
    url = f"{sys.argv[1]}"
    output_dir = f"{sys.argv[2]}"
    print("# Output directory: ", output_dir)
    os.makedirs(output_dir, exist_ok=True)
    response = requests.get(url)

    if response.status_code == 200:
        download(output_dir, response, url)
    else:
        raise Exception(f"# Wrong formatting(use: <functionName link 'path/to/save'>) or dead link, response status code: {response.status_code}")
            
except Exception as e:
            print(e); exit()
