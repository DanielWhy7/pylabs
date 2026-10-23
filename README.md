Laboratory Work No. 1: Regular Expressions (Program Explanation)


📌 Project Architecture & Objective

The core purpose of this program is to automate the filtration of structured text data sets using regular expression constraints. Operating under Variant 1, the architecture processes an input roster of individuals to isolate, count, and export all profile entries containing verified male gender flags.
The system relies on a three-phase pipeline:
1. Parsing Phase: Ingests raw text, identifies individual profile partitions, and translates text blocks into memory-efficient data structures.
2. Filtering Phase: Evaluates the target parameters utilizing regex token matching.
3. Serialization Phase: Re-indexes the compliant targets sequentially and yields a uniform plaintext delivery export.

🛠️ Internal Mechanics & Execution Logic


1. Data Demarcation and Extraction

The database structure splits unique individuals via dynamic profile headers (1), 2), etc.). The program isolates profiles by applying a text split configuration based on an assertive forward-looking pattern:
\(\text{Regex\ Pattern\ Used:\ }\texttt{\backslash \ n(?=\backslash \ d+\backslash \ )}\)
• \n: Targets standard system line breaks.
• (?=\d+\)): A positive lookahead constraint. It locates positions immediately followed by one or more digits and a closing parenthesis without consuming those characters during the boundary split.
Once isolated, each component string line is checked using standard key-value delimiter patterns (^([^:]+)(:)\s*(.*)$) to build mapping dictionaries.

2. Targeted Parameter Verification

To isolate targeted profile types, the application evaluates the data mapped under the key Пол (Gender). The assessment applies a strict exact-match configuration:
\(\text{Regex\ Pattern\ Used:\ }\texttt{\textasciicircum (М|}{}\texttt{м|}{}\texttt{Мужской|}{}\texttt{мужской)$}\)
• ^ and $: Anchors demanding that the input string strictly starts and stops within the pattern limits, eliminating substring false positives.
• (М|м|Мужской|мужской): An explicit alternation group capturing all accepted variations of the targeted class flag.

3. File I/O and Automation Arguments

The program implements the Python standard argparse component to handle terminal-level variable inputs dynamically.
• Positional Argument: Accept a variable path target specifying the location of the source profile dataset (filename).
• Optional Flag (-o / --output): Provides user discretion over the export destination string, defaulting implicitly to output.txt if left undefined.

📊 Processing Metrics & Findings

When executed against the provided base profile index file, the utility tracks and resolves the dataset down to the following functional counts:
• Total Checked Roster Size: 100 individuals.
• Extracted Match Count: 49 Male Profiles correctly qualified through the regex filter system.
• Output Consistency: The filtered data output completely purges out non-matching profile metrics while strictly maintaining sequentially normalized numbering sequence indexes (ranging from 1) up to 49)) inside the generated text file.
