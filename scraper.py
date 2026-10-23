import os
import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from typing import List, Dict

BASE_URL: str = "https://books.toscrape.com/"
HTTP_HEADERS: Dict[str, str] = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

def extract_all_genres() -> Dict[str, str]:
  """Retrieves storefront markup and inventories every listed book category genre using resilient href matching."""
  response = requests.get(BASE_URL, headers=HTTP_HEADERS)
  response.raise_for_status()
  soup = BeautifulSoup(response.text, 'html.parser')

  genre_links = [link for link in soup.find_all('a', href=True) if "category/books/" in link['href']]
  if not genre_links:
    raise ValueError("Critical error: Unable to map structure. Sidebar navigation link paths could not be located.")

  return {link.text.strip(): urljoin(BASE_URL, link['href']) for link in genre_links}

def fetch_covers_from_genre(genre_url: str, limit: int, dest_folder: str, session_offset: int) -> List[Dict[str, str]]:
  """Processes paginated book lists in a genre to download cover illustrations."""
  downloaded_items: List[Dict[str, str]] = []
  current_page_url: str | None = genre_url
  os.makedirs(dest_folder, exist_ok=True)

  while current_page_url and len(downloaded_items) < limit:
    response = requests.get(current_page_url, headers=HTTP_HEADERS)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    for pod in soup.find_all('article', class_='product_pod'):
      if len(downloaded_items) >= limit:
        break
      img_tag = pod.find('img', class_='thumbnail')
      if not img_tag or 'src' not in img_tag.attrs:
        continue

      absolute_img_url = urljoin(current_page_url, img_tag['src'])
      item_id = session_offset + len(downloaded_items) + 1
      filename = f"{item_id}_{os.path.basename(absolute_img_url)}"
      full_disk_path = os.path.join(dest_folder, filename)

      img_response = requests.get(absolute_img_url, headers=HTTP_HEADERS)
      if img_response.ok:
        with open(full_disk_path, 'wb') as f:
          f.write(img_response.content)
        downloaded_items.append({
          "absolute_path": os.path.abspath(full_disk_path),
          "relative_path": os.path.relpath(full_disk_path)
        })

    next_li = soup.find('li', class_='next')
    current_page_url = urljoin(current_page_url, next_li.find('a')['href']) if next_li else None

  return downloaded_items

def write_annotation_manifest(data_records: List[Dict[str, str]], target_csv_path: str) -> None:
  """Appends path pairs systematically inside a CSV data collection log tracking sheet."""
  has_existing = os.path.exists(target_csv_path)
  with open(target_csv_path, mode='a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    if not has_existing:
      writer.writerow(["Absolute Path", "Relative Path"])
    for item in data_records:
      writer.writerow([item["absolute_path"], item["relative_path"]])
