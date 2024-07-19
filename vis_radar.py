import matplotlib.pyplot as plt
import numpy as np

def plot_emotion_radar(emotion_dictionary):
    # Extract labels and stats from the emotion dictionary
    labels = list(emotion_dictionary.keys())
    stats = list(emotion_dictionary.values())
    
    # Number of variables (emotions)
    num_vars = len(labels)
    
    # Compute angle of each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    # The plot is made in a circular (not polygon) space, so we need to "complete the loop"
    stats += stats[:1]
    angles += angles[:1]
    
    # Plot
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, stats, color='red', alpha=0.25)
    ax.plot(angles, stats, color='red', linewidth=2)
    
    # Filling in each segment with color
    ax.fill(angles, stats, color='red', alpha=0.25)
    ax.set_yticklabels([])
    
    # Adding labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    
    plt.title('Emotion Detection Radar Chart')
    plt.show()


