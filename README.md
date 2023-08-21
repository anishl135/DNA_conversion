# DNA_conversion

# DNA Sequence Processor

The DNA Sequence Processor is a simple Python application built using the Tkinter library. It allows users to input a DNA sequence (consisting of A, T, G, C characters) and performs various operations on it.

## Features

- **Validation:** Ensures that the input DNA sequence contains only valid characters (A, T, G, C).

- **mRNA Conversion:** Converts the input DNA sequence into its corresponding mRNA sequence.

- **Complementary Strand:** Provides the complementary strand of the input DNA sequence.

- **tRNA Sequence:** Generates the tRNA sequence by replacing T with U in the input DNA sequence.

- **Protein Sequence:** Translates the mRNA sequence into a protein sequence using the codon table.

## Usage

1. Enter a DNA sequence using only A, T, G, and C characters (turn on caps lock).

2. Click the "Process Sequence" button.

3. The application will display the following information:
   - mRNA Sequence
   - Complementary Strand
   - tRNA Sequence
   - Protein Sequence

## Installation

To run the DNA Sequence Processor, make sure you have Python installed on your system. You will also need the Tkinter library, which is usually included with Python.

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the repository's directory.

3. Run the following command to start the application:

   ```bash
   python dna_gui.py
The application window will open, allowing you to input and process DNA sequences.
Example
Here's an example of a valid input and its output:

    ```bash
   
      Input: ATGCTA   
    
    Output:

    mRNA Sequence: UACGAU
    Complementary Strand: TACGAT
    tRNA Sequence: UACGAU
    Protein Sequence: Tyr-Arg


Author
This DNA Sequence Processor was developed by Anish.

Feel free to contribute to this project or report any issues you encounter.

Happy DNA processing!



