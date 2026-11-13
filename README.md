# Application Programming Labs: Lab 1 - Regular Expressions

This repository contains the solution for **Laboratory Work No. 1**, focusing on text parsing and data filtration using **Regular Expressions** in Python.

The core objective (Variant 1) is to automate the processing of a structured roster of individuals. The program parses the dataset, isolates all profiles with a verified male gender flag, counts them, and exports the filtered results to a new, sequentially numbered text file.

## 📁 Repository Structure

```text
.
├── info/                  # All lab documentation and guidelines
│   ├── APPLICATION_PROGRAMMING_LABS_README.md
│   ├── lab1.md
│   └── lab_guide.md
├── main.py                # Main executable script
├── data.txt               # Input dataset (100 profiles)
├── .gitignore             # Ignores generated output files (e.g., output.txt)
└── README.md              # Project documentation
```

## 🌟 Key Features

*   **Bilingual Compatibility:** Seamlessly handles both English (`Sex: Male`) and Russian (`Пол: Мужской`) datasets.
*   **Robust Regex Parsing:** Uses positive lookahead constraints to accurately split the dataset into individual profile blocks regardless of variations in spacing or formatting.
*   **Dynamic Serialization:** Outputs the filtered profiles while maintaining the original key-value order and re-indexing the newly generated list sequentially.
*   **Error Handling:** Gracefully handles missing files and permission errors using standard exception handling.

## 🚀 Getting Started

### Prerequisites

*   Python 3.8 or higher is required.
*   No external dependencies are needed; the script relies entirely on Python's standard libraries (`argparse`, `re`, `sys`, `typing`).

### Usage

Run the script by providing the path to the input dataset. By default, it saves the results to `output.txt`.

**Basic execution:**
```bash
python main.py data.txt
```

**Custom output file:**
You can use the `-o` or `--output` flag to specify a different destination file:
```bash
python main.py data.txt -o filtered_males.txt
```

**Expected Output:**
```text
Number of male profiles: 49
Profiles saved to file: output.txt
```

## ⚙️ Architecture & Mechanics

The program operates on a clean three-phase pipeline:

### 1. Data Demarcation and Extraction
The input file is split into individual profiles using an assertive forward-looking pattern: `\n(?=\d+\))`. 
* This locates positions immediately followed by a number and a closing parenthesis (e.g., `1)`, `2)`) without consuming the delimiter itself.
* Each block is then parsed into a dictionary using the pattern `^([^:]+)(:)\s*(.*)$` to separate the field names from the values.

### 2. Targeted Parameter Verification
To isolate the male profiles, the program evaluates the extracted dictionary values using strict exact-match constraints:
*   **Pattern:** `^(М|м|Мужской|мужской|M|m|Male|male)$`
*   The `^` and `$` anchors prevent false positives (e.g., ignoring words that merely contain "Male" as a substring).

### 3. File I/O and Automation
*   The `parse_profiles` function returns a list of dictionaries.
*   The `main` function filters this list, prints the final count, and writes the serialized data back to the disk using UTF-8 encoding.
*   The `.gitignore` ensures that local test outputs (like `output.txt`) do not pollute the repository history.

## 📊 Processing Metrics

When executed against the provided `data.txt`:
*   **Total Checked Roster:** 100 individuals
*   **Extracted Matches:** 49 Male profiles
*   **Output State:** Non-matching profiles are completely purged, and the remaining 49 profiles are cleanly re-indexed from `1)` to `49)`.

## 🛡️ Formatting Rules

The code strictly adheres to the formatting guidelines outlined in `info/lab_guide.md`:
*   **PEP8** compliance.
*   Full **type-hinting** for function arguments and returns.
*   Comprehensive **docstrings** for all functions.
*   Modular design with execution guarded by `if __name__ == '__main__':`.
