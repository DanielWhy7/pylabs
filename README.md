# Multi-Genre Book Cover Scraper & Image Processing Suite

An enterprise-grade, highly resilient multi-module application that combines three laboratory assignments:
1. **Web Scraping (Lab No. 2):** Systematically crawls book categories to extract thumbnail cover illustrations from the Books to Scrape sandbox network.
2. **Image Processing (Lab No. 3, Variant 1):** Applies a sequence of multi-dimensional array transformations (crop, rotate, overlay) to the collected images using NumPy and OpenCV.
3. **Data Analysis (Lab No. 4, Variant 1):** Analyzes the scraped images using Pandas, calculating image heights and generating histograms.

The architecture strictly adheres to programmatic decoupling rules, containing isolated components for network operations, cross-platform file sanitization, precise dataset indexing, standalone image-processing routines, and data analysis pipelines.

## 🌟 Key Features

**Scraping Subsystem (Lab No. 2)**
*   **Resilient Element Extraction:** Avoids brittle DOM tree structures by using deep pattern-matching link filtration to locate book categories.
*   **Smart Pagination Traversal:** Dynamically checks and resolves next link bindings until target collection criteria are met.
*   **Global Collision Protection:** Enforces strict execution offset counters to generate sequential file titles across all subdirectories.
*   **Dual-Path Dataset Generation:** Automatically logs matching pairs of absolute storage addresses and portable environment-relative paths.

**Image-Processing Subsystem (Lab No. 3, Variant 1)**
*   **Top-Left Cropping (Transformation 1):** Crops images to caller-specified dimensions, anchored at the top-left pixel.
*   **Lossless Rotation (Transformation 4):** Rotates images by an arbitrary angle around the center, expanding the canvas so no corner content is clipped.
*   **Semi-Transparent Overlay (Transformation 10):** Composites a second image on top of the first with a configurable alpha blending coefficient.

**Data Analysis Subsystem (Lab No. 4, Variant 1)**
*   **Pandas DataFrame Integration:** Loads the CSV annotation into a structured, queryable format.
*   **Dynamic Feature Engineering:** Automatically extracts image heights (Variant 1) and adds them as a new column.
*   **Sorting & Filtering:** Provides native Pandas sorting and custom filtering logic.
*   **Histogram Visualization:** Generates and saves a labeled Matplotlib histogram of the image height distribution.

## 📁 Repository Structure

```text
├── main.py             # CLI entry point for Lab 3 (Image Processing)
├── analyzer.py         # CLI entry point for Lab 4 (Data Analysis)
├── scraper.py          # Core scraping mechanics for Lab 2
├── iterator.py         # Custom sequence class validating structural integrity of Lab 2 CSV output
├── image_processor.py  # Image transformations: crop (1), rotate (4), semi-transparent overlay (10)
├── visualizer.py       # Terminal rendering via term-image for processed images
├── clean.py            # Utility script to remove generated artifacts (caches, outputs)
└── requirements.txt    # External package installation dependencies manifest
```

## 🚀 Getting Started

### Prerequisites

This application requires Python 3.10 or higher. Ensure the package installer manager tool `pip` is available.

### Installation

1. Clone the project repository and navigate to it:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>
   ```
2. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Linux / macOS
   source .venv/bin/activate
   # Windows (PowerShell)
   .venv\Scripts\Activate.ps1
   ```
3. Install necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🛠️ Usage Documentation

The project is functionally divided into three stages.

### Stage 1 — Scrape Book Covers (Lab No. 2)
Use the `scraper.py` module to download images. This generates the `scraped_book_covers/` directory and the `covers_annotation.csv` file.

### Stage 2 — Apply Image Transformations (Lab No. 3, Variant 1)
Execute the image-processing pipeline via `main.py`. Variant 1 chains three transformations in order: **crop → rotate → overlay**.

**Example:**
```bash
python main.py \
  --image "scraped_book_covers/Academic/177_d94e6206c2decd3acd9a61b2cbac7eaf.jpg" \
  --overlay "scraped_book_covers/Business/154_92274a95b7c251fea59a2b8a78275ab4.jpg" \
  --output "results/variant1_result.jpg" \
  --crop_width 90 \
  --crop_height 90 \
  --angle 30 \
  --alpha 0.4
```

### Stage 3 — Analyze Data (Lab No. 4, Variant 1)
Run `analyzer.py` to process the Lab 2 CSV file. It will add an `Height` column, sort the data, save a new CSV, and generate a histogram.

**Example:**
```bash
python analyzer.py \
  --csv "covers_annotation.csv" \
  --output_csv "analyzed_data.csv" \
  --output_plot "histogram.png" \
  --min_height 150
```

## 🧹 Cleanup Utility

A convenience script `clean.py` is provided to quickly remove generated test outputs and caches (`__pycache__`, `scraped_book_covers`, `covers_annotation.csv`, `analyzed_data.csv`, `histogram.png`).

```bash
python clean.py
```

## 🛡️ License Configuration Profile

This project distribution framework application is globally distributed under the regulatory criteria of the GNU GPLv3 Free Software License Agreement. Review your matching rights regarding open modification, sharing, and commercial compliance constraints inside the standalone LICENSE code text layout documentation profile located within the parent branch.
