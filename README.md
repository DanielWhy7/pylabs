# Multi-Genre Book Cover Scraper & Image Processing Suite

An enterprise-grade, highly resilient multi-module application that combines two laboratory assignments:
1. **Web Scraping (Lab No. 2):** Systematically crawls book categories to extract thumbnail cover illustrations from the Books to Scrape sandbox network.
2. **Image Processing (Lab No. 3, Variant 1):** Applies a sequence of multi-dimensional array transformations (crop, rotate, overlay) to the collected images using NumPy and OpenCV.

The architecture strictly adheres to programmatic decoupling rules, containing isolated components for network operations, cross-platform file sanitization, precise dataset indexing, and standalone image-processing routines.

## 🌟 Key Features

**Scraping Subsystem (Lab No. 2)**
*   **Resilient Element Extraction:** Avoids brittle DOM tree structures by using deep pattern-matching link filtration to locate book categories.
*   **Smart Pagination Traversal:** Dynamically checks and resolves next link bindings until target collection criteria are met.
*   **Global Collision Protection:** Enforces strict execution offset counters to generate sequential file titles across all subdirectories.
*   **Dual-Path Dataset Generation:** Automatically logs matching pairs of absolute storage addresses and portable environment-relative paths.
*   **High-Performance Stream Iterator:** Implements a custom low-overhead iterator to sequentially scan data indices line-by-line.

**Image-Processing Subsystem (Lab No. 3, Variant 1)**
*   **Top-Left Cropping (Transformation 1):** Crops images to caller-specified dimensions, anchored at the top-left pixel.
*   **Lossless Rotation (Transformation 4):** Rotates images by an arbitrary angle around the center, expanding the canvas so no corner content is clipped.
*   **Semi-Transparent Overlay (Transformation 10):** Composites a second image on top of the first with a configurable alpha blending coefficient.
*   **Terminal Visualization:** Renders the processed result inline within the terminal using the Kitty graphics protocol (via `term-image`).
*   **Graceful Failure Handling:** Distinguishes between missing files, invalid parameters, and I/O errors, surfacing each with a targeted message on stderr.

## 📁 Repository Structure

```text
├── main.py             # CLI entry point for Lab 3 (Image Processing)
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
   *(Note: If you are on Python 3.14, you may need to install `pillow>=11.3.0` manually first to satisfy `term-image`'s dependencies).*

## 🛠️ Usage Documentation

The project is functionally divided into two stages. 

### Stage 1 — Scrape Book Covers (Lab No. 2)

*(Note: While `main.py` is currently dedicated to Lab 3, the scraping pipeline can be executed by importing `scraper.py` or running a small wrapper script).*

To scrape covers, you will utilize the `scraper.py` module. It supports downloading a specific number of images per genre:

```python
# Example of how to trigger the scraper module manually
from scraper import extract_all_genres, fetch_covers_from_genre, write_annotation_manifest
```
*The scraper outputs images into subdirectories and logs their paths into a CSV file (e.g., `covers_annotation.csv`).*

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

**Tips and Constraints:**
*   The crop dimensions are safely clamped to the base image's dimensions. If you request a `100x100` crop on a `97x155` image, it will automatically resize the crop to `97x100` and print a warning, preventing crashes.
*   The overlay image is resized to match the cropped base dimensions.
*   `--alpha` must be within `[0, 1]`. A value of `0.4` means the overlay is 40% opaque.

## ⚙️ Arguments Specification Guide

### Stage 1 — Scraping (Lab No. 2 Implementation inside `scraper.py`)
| CLI Argument Flag | Element Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `--count` | int | None | Exact image extraction quota per category genre. |
| `--output_dir` | str | "scraped_book_covers" | Workspace directory for image subfolders. |
| `--csv_path` | str | "covers_annotation.csv" | Destination path for the tracking index sheet. |

### Stage 2 — Image Processing (Lab No. 3, implemented in `main.py`)
| CLI Argument Flag | Element Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `--image` | str | None (Required) | Path to the base image to be processed. |
| `--overlay` | str | None (Required) | Path to the image composited on top of the base. |
| `--output` | str | None (Required) | Destination path where the final processed image is written. |
| `--crop_width` | int | None (Required) | Crop width in pixels, anchored at the top-left corner. |
| `--crop_height`| int | None (Required) | Crop height in pixels, anchored at the top-left corner. |
| `--angle` | float | 45.0 | Rotation angle in degrees, counter-clockwise around the center. |
| `--alpha` | float | 0.5 | Overlay opacity coefficient in the inclusive range `[0, 1]`. |
| `--comparison`| str | "comparison.png" | Destination path for the comparison output (Note: currently renders to terminal). |

## 📊 Variant 1 Transformation Pipeline

The exact sequence applied by `main.py`:

1.  Load the base image and the overlay image with OpenCV (BGR layout).
2.  Print both original dimensions to the console.
3.  Crop the base image to `(crop_width, crop_height)` starting from the top-left pixel **[Transformation 1]**.
4.  Rotate the cropped result by `--angle` degrees around its center, expanding the canvas so no content is lost **[Transformation 4]**.
5.  Resize the overlay to match the rotated image's shape, then blend with `cv2.addWeighted` at `--alpha` **[Transformation 10]**.
6.  Write the final image to `--output` via `cv2.imwrite`.
7.  Render the final image inline in the terminal using the `term-image` library (requires a Kitty, Ghostty, or WezTerm compatible terminal).

## 🧹 Cleanup Utility

A convenience script `clean.py` is provided to quickly remove generated test outputs and caches (`__pycache__`, `scraped_book_covers`, `covers_annotation.csv`).

```bash
python clean.py
```

## 🛡️ License Configuration Profile

This project distribution framework application is globally distributed under the regulatory criteria of the GNU GPLv3 Free Software License Agreement. Review your matching rights regarding open modification, sharing, and commercial compliance constraints inside the standalone LICENSE code text layout documentation profile located within the parent branch.
