import csv
import os
from typing import Iterator, Dict

class AnnotationIterator:
  """
  A custom iterator that yields file paths from a CSV annotation file.
  """
  def __init__(self, annotation_path: str) -> None:
    """
    Initializes the iterator with the path to the CSV annotation file.
    :param annotation_path: Path to the CSV file containing annotations.
    """
    if not os.path.exists(annotation_path):
      raise FileNotFoundError(f"Annotation file not found at: {annotation_path}")

    self.annotation_path: str = annotation_path
    self._file = open(self.annotation_path, mode='r', newline='', encoding='utf-8')
    self._reader = csv.reader(self._file)

    # Skip headers if present
    try:
      self._headers = next(self._reader)
    except StopIteration:
      self._headers = []

  def __iter__(self) -> 'AnnotationIterator':
    """Returns the iterator object itself."""
    return self

  def __next__(self) -> Dict[str, str]:
    """
    Returns the next record's absolute and relative paths.
    :return: A dictionary containing 'absolute_path' and 'relative_path'.
    """
    try:
      row = next(self._reader)
      if len(row) < 2:
        return self.__next__() # Skip malformed lines safely
      return {
        "absolute_path": row[0],
        "relative_path": row[1]
      }
    except StopIteration:
      self._file.close()
      raise StopIteration
