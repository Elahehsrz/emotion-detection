import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
def plot_emotion_distribution(emotion_dict):
    # Extract keys and values from the dictionary
    labels = list(emotion_dict.keys())
    stats = list(emotion_dict.values())

    # Create the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(labels, stats, color=['blue', 'green', 'gray', 'red', 'purple', 'orange', 'pink'])

    # Add titles and labels
    plt.title('Emotion Distribution')
    plt.xlabel('Emotions')
    plt.ylabel('Frequency')

    # Show the bar chart
    plt.show()
