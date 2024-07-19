import sys
from data import extract_text_with_page_numbers, extract_all_text_as_list, write_results_to_file
from sentimentAnalyzer import analyze_sentiment
import json
import spacy
from transformers import pipeline
from processing import tokenize_sentences
from caluclate_frequency import count_emotions
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
    text= all_text_list[0]
    # Tokenize sentences
    sentences = tokenize_sentences(text)
    print("sentences are ready")
    for sentence in sentences:
        result = analyze_sentiment(sentence )
        tuple_result = (sentence, result)
        results.append(tuple_result)
        #results= str(results)
    write_results_to_file(results, filename)
    emotion_dictionary = count_emotions(results)
    plot_emotion_radar(emotion_dictionary)
    plot_emotion_distribution(emotion_dictionary)
        
        


if __name__ == "__main__":
    main()

