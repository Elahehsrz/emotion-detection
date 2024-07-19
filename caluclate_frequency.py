def count_emotions(results_list):
    emotion_frequency = {}

    for item in results_list:
        if len(item) == 2 and isinstance(item[1], dict) and 'top_emotion' in item[1]:
            top_emotion = item[1]['top_emotion']
            if top_emotion in emotion_frequency:
                emotion_frequency[top_emotion] += 1
            else:
                emotion_frequency[top_emotion] = 1
    
    return emotion_frequency


