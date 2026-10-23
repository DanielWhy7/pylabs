import csv
import os
from typing import Iterator, Dict, Any, List

class CoverPathIterator:
  """
  Custom sequence iterator over downloaded image absolute and relative file locations
  derived from a saved laboratory annotation index sheet.
  """
  def __init__(self, annotation_path: str) -> None:
    """
    Initializes the sequence stream iterator tracking generated annotation records.
    :param annotation_path: Absolute or relative disk file path to the parsed CSV tracker metadata index.
    """
    if not os.path.exists(annotation_path):
      raise FileNotFoundError(f"Requested index manifest target not found on disk at: '{annotation_path}'")

    self.annotation_path: str = annotation_path
    self._file_stream = open(self.annotation_path, mode='r', newline='', encoding='utf-8')
    self._csv_reader = csv.reader(self._file_stream)

    # Safely capture and isolate column header labels if present
    try:
      self._headers: List[str] = next(self._csv_reader)
    except StopIteration:
      self._headers = []

  def __iter__(self) -> 'CoverPathIterator':
    """
    Returns the instance itself to conform to Python's standard iteration structure.
    :return: Current CoverPathIterator object context.
    """
    return self

  def __next__(self) -> Dict[str, str]:
    """
    Advances sequentially and extracts path pairs from the underlying annotation records.
    :return: Dictionary object referencing both absolute and relative filesystem paths.
    :raises StopIteration: Signifies that file row processing targets have been fully exhausted.
    """
    try:
      row: List[str] = next(self._csv_reader)
      # Safeguard parsing context against corrupted or incomplete spreadsheet lines
      if len(row) < 2:
        return self.__next__()

      return {
        "absolute_path": row[0].strip(),
        "relative_path": row[1].strip()
      }
    except StopIteration:
      self._file_stream.close()
      raise StopIteration
