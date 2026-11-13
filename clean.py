import os
import shutil
import sys

def remove_artifact(path: str) -> None:
  """
  Removes a file or directory if it exists.
  :param path: Path to the file or directory to remove.
  """
  try:
    if os.path.isdir(path):
      shutil.rmtree(path)
      print(f"🗑️ Removed directory: {path}")
    elif os.path.isfile(path):
      os.remove(path)
      print(f"🗑️ Removed file: {path}")
    else:
      print(f"ℹ️ Skipped (not found): {path}")
  except PermissionError:
    print(f"❌ Permission denied while trying to remove: {path}", file=sys.stderr)
  except Exception as exc:
    print(f"❌ Error removing {path}: {exc}", file=sys.stderr)


def main() -> None:
  """
  Cleans up generated artifacts from the repository.
  """
  targets = [
    "__pycache__",
    "scraped_book_covers",
    "covers_annotation.csv",
    "results",
    "analyzed_data.csv",
    "histogram.png"
  ]

  print("Starting repository cleanup...")
  for target in targets:
    remove_artifact(target)
  print("Cleanup complete!")


if __name__ == "__main__":
  main()
