import os
import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from typing import List, Dict

BASE_URL = "https://toscrape.com"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def get_genre_urls() -> Dict[str, str]:
  """
  Scrapes the main page to index all available book genres and their relative URLs.
  :return: A dictionary mapping lowercase genre names to their full page URLs.
  """
  response = requests.get(BASE_URL, headers=HEADERS)
  response.raise_for_status()

  soup = BeautifulSoup(response.text, 'html.parser')
  side_categories = soup.find('div', class_='side_categories')
  if not side_categories:
    return {}

  links = side_categories.find('ul').find('ul').find_all('a')
  return {link.text.strip().lower(): urljoin(BASE_URL, link['href']) for link in links}

def download_book_covers(genre_url: str, count: int, output_dir: str) -> List[Dict[str, str]]:
  """
  Downloads a specified number of book cover images from a given genre page.
  :param genre_url: The full URL to the starting page of the genre.
  :param count: Total number of cover images to download.
  :param output_dir: Destination folder path.
  :return: A list of dictionaries representing downloaded image paths for the annotation CSV.
  """
  downloaded_records: List[Dict[str, str]] = []
  current_url = genre_url

  os.makedirs(output_dir, exist_ok=True)

  while current_url and len(downloaded_records) < count:
    response = requests.get(current_url, headers=HEADERS)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
  
    books = soup.find_all('article', class_='product_pod')
    for book in books:
      if len(downloaded_records) >= count:
        break
      
      img_tag = book.find('img', class_='thumbnail')
      if not img_tag or 'src' not in img_tag.attrs:
        continue
      
      img_url = urljoin(current_url, img_tag['src'])
      img_name = os.path.basename(img_url)
      dest_path = os.path.join(output_dir, f"{len(downloaded_records) + 1}_{img_name}")
    
      # Download and write file
      img_data = requests.get(img_url, headers=HEADERS).content
      with open(dest_path, 'wb') as img_file:
        img_file.write(img_data)
      
      downloaded_records.append({
        "absolute_path": os.path.abspath(dest_path),
        "relative_path": os.path.relpath(dest_path)
      })
    
    # Handle pagination pages safely
    next_button = soup.find('li', class_='next')
    current_url = urljoin(current_url, next_button.find('a')['href']) if next_button else None
  
  return downloaded_records

def save_annotation_csv(records: List[Dict[str, str]], annotation_path: str) -> None:
  """
  Appends or creates an annotation file mapping file paths.
  :param records: List of path records.
  :param annotation_path: Path to target CSV file.
  """
  file_exists = os.path.exists(annotation_path)
  with open(annotation_path, mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    if not file_exists:
      writer.writerow(["Absolute Path", "Relative Path"])
    for record in records:
      writer.writerow([record["absolute_path"], record["relative_path"]])
