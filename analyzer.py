import argparse
import os
import sys

import cv2
import pandas as pd
import matplotlib.pyplot as plt


def load_annotation(csv_path: str) -> pd.DataFrame:
  """
  Loads the annotation CSV and names the columns.
  :param csv_path: Path to the CSV file.
  :return: DataFrame with named columns.
  """
  if not os.path.exists(csv_path):
    raise FileNotFoundError(f"Annotation file not found: '{csv_path}'")

  df = pd.read_csv(csv_path)
  # Name the columns to reflect data content (Task 2)
  df.columns = ["Absolute Path", "Relative Path"]
  return df


def get_image_height(image_path: str) -> int:
  """
  Returns the height of the image.
  :param image_path: Path to the image.
  :return: Height in pixels, or 0 if the image cannot be read.
  """
  img = cv2.imread(image_path)
  if img is None:
    return 0
  return img.shape[0]


def add_height_column(df: pd.DataFrame) -> pd.DataFrame:
  """
  Adds a column with the height of each image (Variant 1).
  :param df: Input DataFrame.
  :return: DataFrame with the new 'Height' column.
  """
  df['Height'] = df['Absolute Path'].apply(get_image_height)
  return df


def sort_dataframe(df: pd.DataFrame, column: str) -> pd.DataFrame:
  """
  Sorts the DataFrame by the specified column.
  :param df: Input DataFrame.
  :param column: Column to sort by.
  :return: Sorted DataFrame.
  """
  return df.sort_values(by=column, ascending=True).reset_index(drop=True)


def filter_dataframe(df: pd.DataFrame, column: str, min_value: float) -> pd.DataFrame:
  """
  Filters the DataFrame by the specified column.
  :param df: Input DataFrame.
  :param column: Column to filter.
  :param min_value: Minimum value to keep.
  :return: Filtered DataFrame.
  """
  return df[df[column] >= min_value].reset_index(drop=True)


def plot_histogram(df: pd.DataFrame, column: str, output_path: str) -> None:
  """
  Creates and saves a histogram of the specified column.
  :param df: DataFrame containing the data.
  :param column: Column to plot.
  :param output_path: Path to save the graph image.
  """
  plt.figure(figsize=(10, 6))
  plt.hist(df[column], bins=20, color='skyblue', edgecolor='black')
  plt.title(f'Distribution of Image {column}')
  plt.xlabel(f'{column} (pixels)')
  plt.ylabel('Number of Images')
  plt.grid(axis='y', alpha=0.75)
  plt.savefig(output_path, dpi=120)
  plt.show()
  plt.close()


def main() -> None:
  """
  Main execution function for Lab 4, Variant 1.
  """
  parser = argparse.ArgumentParser(description="Laboratory Work No. 4, Variant 1: Data Analysis")
  parser.add_argument("--csv", required=True, help="Path to the annotation CSV file")
  parser.add_argument("--output_csv", required=True, help="Path to save the updated DataFrame")
  parser.add_argument("--output_plot", required=True, help="Path to save the histogram image")
  parser.add_argument("--min_height", type=int, default=0, help="Filter threshold for image height")
  args = parser.parse_args()

  try:
    # 1 & 2. Load data and name columns
    df = load_annotation(args.csv)

    # 3. Add new column
    df = add_height_column(df)

    # 4. Sort data by the new column
    df_sorted = sort_dataframe(df, 'Height')

    # 7. Save the dataframe
    df_sorted.to_csv(args.output_csv, index=False)
    print(f"💾 Sorted DataFrame saved to: {args.output_csv}")

    # 6 & 7. Plot histogram for all sorted data and save
    plot_histogram(df_sorted, 'Height', args.output_plot)
    print(f"📊 Histogram saved to: {args.output_plot}")

    # 5. Demonstrate filtering function
    df_filtered = filter_dataframe(df_sorted, 'Height', args.min_height)
    print(f"ℹ️ Filtering demo: {len(df_filtered)} out of {len(df_sorted)} images have a height >= {args.min_height} px.")

  except FileNotFoundError as exc:
    print(f"❌ File not found: {exc}", file=sys.stderr)
  except Exception as exc:
    print(f"❌ Unexpected error: {exc}", file=sys.stderr)


if __name__ == "__main__":
  main()
