import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Here we will load the file in the directry that are in the google folder
data_file = 'Input.xlsx'
output_directory = 'extracted_articles'

# here we will create the folder where the output data from links will be stored
os.makedirs(output_directory, exist_ok=True)

df = pd.read_excel(data_file)





def extract_article(url, url_id):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('title').get_text(strip=True)
        article_body = ' '.join([p.get_text(strip=True) for p in soup.find_all('p')])



        with open(os.path.join(output_directory, f"{url_id}.txt"), 'w', encoding='utf-8') as file:
            file.write(f"Title: {title}\n\n{article_body}")
        
        print(f"Successfully extracted article for URL_ID: {url_id}")
    except Exception as e:
        print(f"Error extracting article for URL_ID: {url_id}, URL: {url}. Error: {e}")

for _, row in df.iterrows():
    url = row['URL']
    url_id = row['URL_ID']
    extract_article(url, url_id)

print("Article extraction completed.")
