# Text Analyzer

A simple Python text analysis app built with Gradio. It lets you paste in any text and quickly see:

- Total number of words
- Total number of characters
- The most common word

The app runs in a local web interface, making it easy to test short paragraphs, notes, or sample text.

## Features

- Clean and lightweight interface
- Counts words from the entered text
- Counts characters from the original input
- Finds the most frequent word in the text
- Includes a clear button to reset the input and output fields

## How It Works

The app processes text using the following steps:

1. Converts the text to lowercase
2. Removes punctuation
3. Splits the text into words
4. Counts the words and characters
5. Identifies the most common word

If no text is entered, the app returns `No words entered`.

## Project Structure

```text
text analyzer/
|- text_analyzer.py
|- README.md
```

## Requirements

- Python 3.8 or newer
- `gradio`

## Installation

1. Clone or download this project.
2. Open a terminal in the project folder.
3. Install the required package:

```bash
pip install gradio
```

## Usage

Run the app with:

```bash
python text_analyzer.py
```

After running the command, Gradio will start a local server and provide a URL in the terminal. Open that URL in your browser to use the app.

## Example

Input:

```text
Hello world! Hello everyone.
```

Output:

```text
Words:3
Characters:28
Most common: hello
```

## Notes

- Character count includes spaces and punctuation from the original text.
- Word counting is based on cleaned text, so punctuation is removed before analysis.
- If multiple words appear the same number of times, the first one encountered is returned as the most common word.

## Possible Improvements

- Add sentence count
- Show all repeated words, not just the most common one
- Handle extra whitespace more explicitly
- Add a requirements file for easier setup
- Deploy the app online with Gradio sharing or Hugging Face Spaces

## License

This project is open for personal and educational use. You can add a license file if you plan to share or publish it publicly.
