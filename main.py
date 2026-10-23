import argparse
import sys
import os
import requests
from typing import List, Dict
from scraper import extract_all_genres, fetch_covers_from_genre, write_annotation_manifest
from iterator import CoverPathIterator

def run_pipeline() -> None:
  """
  Orchestrates programmatic setup steps executing Variant 1 instructions, managing cross-module dependencies.
  """
  cli_parser = argparse.ArgumentParser(
    description="Laboratory 2 Work: Comprehensive Multi-Genre Image Scraping Suite (Variant 1)"
  )
  cli_parser.add_argument(
    '--count', type=int, required=True,
    help="Target number of book thumbnail records requested for recovery inside every distinct genre catalog"
  )
  cli_parser.add_argument(
    '--output_dir', type=str, default="scraped_book_covers",
    help="Custom filesystem path specifying where file download structures must assemble (Default: scraped_book_covers)"
  )
  cli_parser.add_argument(
    '--csv_path', type=str, default="covers_annotation.csv",
    help="Assigned document storage target name routing compilation tracking parameters (Default: covers_annotation.csv)"
  )

  parsed_arguments = cli_parser.parse_args()

  try:
    print("🌐 Contacting digital interface indexes...")
    discovered_genres: Dict[str, str] = extract_all_genres()

    session_compiled_records: List[Dict[str, str]] = []
    running_total_count: int = 0

    print(f"📂 Found {len(discovered_genres)} active genres. Beginning targeted downloads tracking processes...")

    for name_token, target_web_endpoint in discovered_genres.items():
      # Sanitize folder path assignments against reserved filesystem special symbol anomalies
      sanitized_folder_name: str = name_token.replace(" ", "_").replace("/", "-")
      genre_target_path: str = os.path.join(parsed_arguments.output_dir, sanitized_folder_name)

      print(f"  📥 Downloading up to {parsed_arguments.count} items from category context: '{name_token}'...")

      genre_batch: List[Dict[str, str]] = fetch_covers_from_genre(
        genre_url=target_web_endpoint,
        limit=parsed_arguments.count,
        dest_folder=genre_target_path,
        session_offset=running_total_count
      )

      session_compiled_records.extend(genre_batch)
      running_total_count += len(genre_batch)

    if session_compiled_records:
      write_annotation_manifest(session_compiled_records, parsed_arguments.csv_path)
      print(f"\n✨ Script successful! Captured {running_total_count} files total across discovered site categories.")
      print(f"📄 Operational parameters mapped inside manifest log sheet: '{parsed_arguments.csv_path}'")

      print("\n🔄 Initializing custom sequence loop generator test execution loop...")
      index_path_iterator = CoverPathIterator(parsed_arguments.csv_path)

      # Print sample confirmation items out using the built-in custom next iterator workflow verification method
      for structural_index, item_entry in enumerate(index_path_iterator, start=1):
        print(f"  [File #{structural_index}] Relative Path Output Verified -> {item_entry['relative_path']}")
    else:
      print("⚠️ System operational warning: No matching content files were retrieved during analysis.")

  except requests.RequestException as connection_error:
    print(f"❌ Network operation failure tracking parameters: {connection_error}", file=sys.stderr)
  except Exception as general_system_exception:
    print(f"❌ Fatal execution engine breakdown: {general_system_exception}", file=sys.stderr)

if __name__ == "__main__":
  run_pipeline()
