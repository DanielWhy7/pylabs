import argparse
import sys
from scraper import get_genre_urls, download_book_covers, save_annotation_csv
from iterator import AnnotationIterator

def main() -> None:
  """
  Main driver execution managing programmatic interfaces.
  """
  parser = argparse.ArgumentParser(description="Lab 2: Variant 2 Equal Count Book Genre Scraper")
  parser.add_argument('--genres', type=str, nargs='+', required=True, help="List of target genres (e.g. Travel Mystery)")
  parser.add_argument('--count', type=int, default=15, help="Number of items to fetch per genre")
  parser.add_argument('--output_dir', type=str, default="downloaded_covers", help="Destination download path")
  parser.add_argument('--csv_path', type=str, default="annotation.csv", help="Target output annotation metadata CSV")
  
  args = parser.parse_args()
  
  try:
    print("🔍 Fetching target site catalogs...")
    available_genres = get_genre_urls()
    
    all_records = []
    for genre_name in args.genres:
      normalized_name = genre_name.strip().lower()
      if normalized_name not in available_genres:
        print(f"⚠️ Warning: Genre '{genre_name}' not found on site. Skipping.")
        continue
        
      print(f"📥 Downloading cover sets for genre: '{genre_name}'...")
      genre_dir = os.path.join(args.output_dir, normalized_name)
      records = download_book_covers(available_genres[normalized_name], args.count, genre_dir)
      all_records.extend(records)
      
    if all_records:
      save_annotation_csv(all_records, args.csv_path)
      print(f"✅ Download complete. Index metadata stored safely inside: {args.csv_path}")
      
      print("\n🔄 Verification step: Parsing file records through Custom Iterator...")
      path_iterator = AnnotationIterator(args.csv_path)
      for idx, entry in enumerate(path_iterator, 1):
        print(f"Record #{idx} -> Relative File Path: {entry['relative_path']}")
    else:
      print("❌ No matching files were scraped.")
      
  except Exception as exc:
    print(f"Fatal operation error encountered: {exc}", file=sys.stderr)

if __name__ == "__main__":
  main()
