# Emotion Detection in "La Chute" by Albert Camus: Analyzing Clamence's Dual Personality

## Description:
This project aims to analyze the emotions and sentiments expressed in Albert Camus' novel "La Chute" through its main character, Clamence. By leveraging Natural Language Processing (NLP) techniques, the project extracts and processes the text from the novel, detects emotions and sentiments, and visualizes the emotional distribution throughout the book. The goal is to gain insights into Clamence's dual personality and the emotional undertones of his narrative.

## Skills Demonstrated:
- **Natural Language Processing (NLP):** Extracting and processing text data from a PDF file, tokenizing sentences, and performing sentiment analysis and emotion detection.
- **Data Visualization:** Creating bar charts and radar charts to visualize the distribution of detected emotions.
- **Python Programming:** Writing and organizing Python code, working with various libraries, and handling file operations.
- **Text Processing:** Using libraries such as PyPDF2 and PyMuPDF for PDF text extraction and spaCy for sentence tokenization.
- **Emotion Detection and Sentiment Analysis:** Implementing emotion and sentiment analysis using TextBlob and the Hugging Face transformers pipeline.

## Tools/Libraries:
- **PyPDF2:** A library for reading and extracting text from PDF files.
- **PyMuPDF (fitz):** Another library for working with PDF documents, used for text extraction.
- **json:** Used for saving extracted text and results in JSON format.
- **spaCy:** An NLP library used for tokenizing sentences in the text.
- **TextBlob:** A library for performing sentiment analysis.
- **transformers:** A library from Hugging Face used for emotion detection with pre-trained models.
- **matplotlib:** A plotting library used for creating bar charts and radar charts to visualize the emotional distribution.
- **numpy:** A library for numerical operations, used in generating angles for radar charts.

## Project Structure:
1. **Text Extraction:**
   - Extracts text from the PDF using PyPDF2 and PyMuPDF.
   - Saves the extracted text with page numbers to a JSON file.

2. **Text Processing:**
   - Combines all extracted text into a single string.
   - Tokenizes the text into sentences using spaCy.

3. **Emotion and Sentiment Analysis:**
   - Analyzes each sentence for sentiment (polarity and subjectivity) using TextBlob.
   - Detects emotions in each sentence using the Hugging Face transformers pipeline.
   - Aggregates the results, including the top emotion and its score.

4. **Data Visualization:**
   - Counts the frequency of each detected emotion.
   - Creates a bar chart to show the distribution of emotions.
   - Creates a radar chart to provide a visual representation of the emotional spectrum.

5. **Output:**
   - Writes the analysis results to a text file.
   - Displays the visualizations of emotion distribution.

## How to Run:
1. Ensure you have the required libraries installed. You can use `pip` to install them:
   ```sh
   pip install PyPDF2 PyMuPDF spacy textblob transformers matplotlib numpy
   ```
2. Download the "La Chute" PDF and save it in the `Data` directory with the name `camus_la_chute.pdf`.
3. Execute the `main()` function in the script to run the analysis:
   ```sh
   python your_script_name.py
   ```
4. The results will be saved in `results.txt`, and visualizations will be displayed.

## Example Usage:
```python
from data import extract_text_with_page_numbers, extract_all_text_as_list, write_results_to_file
from sentimentAnalyzer import analyze_sentiment
import json
import spacy
from transformers import pipeline
from processing import tokenize_sentences
from calculate_frequency import count_emotions
from vis_radar import plot_emotion_radar
from vis_bar import plot_emotion_distribution

filename = 'results.txt'

def main():
   results = []
   print(type(results))
   # Open the PDF file
   pdf_path = "Data/camus_la_chute.pdf"
   # Example usage:
   #json_output_path = "pdf_text_with_page_numbers.json"
   # extract_text_with_page_numbers(pdf_path, json_output_path)
   all_text_list = extract_all_text_as_list(pdf_path)
   text = all_text_list[0]
   # Tokenize sentences
   sentences = tokenize_sentences(text)
   print("sentences are ready")
   for sentence in sentences:
       result = analyze_sentiment(sentence)
       tuple_result = (sentence, result)
       results.append(tuple_result)
       # results = str(results)
   write_results_to_file(results, filename)
   emotion_dictionary = count_emotions(results)
   plot_emotion_radar(emotion_dictionary)
   plot_emotion_distribution(emotion_dictionary)

if __name__ == "__main__":
   main()
```

