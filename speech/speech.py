import os
import librosa
import librosa.display
import librosa.effects as le
import IPython.display as ipd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from skimage.transform import resize


model1 = load_model(r"D:\socialbot\speech\model\model1.h5")
model2 = load_model(r"D:\socialbot\speech\model\model2.h5")
model3 = load_model(r"D:\socialbot\speech\model\model3.h5")
model4 = load_model(r"D:\socialbot\speech\model\model4.h5")
model5 = load_model(r"D:\socialbot\speech\model\model5.h5")

def predict_model(audio1):       
    target_shape = (128, 128)
    y, sr = librosa.load(audio1, sr=None)
    y_stretched = librosa.effects.time_stretch(y, rate=1)
    Mel_spectrogram = librosa.feature.melspectrogram(y=y_stretched, sr=sr)
    Mel_spectrogram = resize(np.expand_dims(Mel_spectrogram, axis=-1), target_shape)
    Mel_spectrogram = tf.reshape(Mel_spectrogram, (1,) + target_shape + (1,))
    return Mel_spectrogram

def models_system(MSG):
    
    predictions = model1.predict(MSG)
    class_probabilities = predictions[0]
    predicted_class_index = np.argmax(class_probabilities)

    if predicted_class_index==0:#negative
        predictions = model2.predict(MSG)
        class_probabilities = predictions[0]
        predicted_class_index = np.argmax(class_probabilities)

        if predicted_class_index==0:#model5
            predictions = model5.predict(MSG)
            class_probabilities = predictions[0]
            predicted_class_index = np.argmax(class_probabilities)
            if predicted_class_index==0:
                Final_pred="Angry"
            elif predicted_class_index==1:
                Final_pred="Happy"   
            
        elif predicted_class_index==1:
            Final_pred="Disgusted"
        elif predicted_class_index==2:
            Final_pred="Fearful"        
        elif predicted_class_index==3:#model4
            predictions = model4.predict(MSG)
            class_probabilities = predictions[0]
            predicted_class_index = np.argmax(class_probabilities)
            if predicted_class_index==0:
                Final_pred="Sad"
            elif predicted_class_index==1:
                Final_pred="Neutral"

    elif predicted_class_index==1:#positive
        predictions = model3.predict(MSG)
        class_probabilities = predictions[0]
        predicted_class_index = np.argmax(class_probabilities)

        if predicted_class_index==0:#model5
            predictions = model5.predict(MSG)
            class_probabilities = predictions[0]
            predicted_class_index = np.argmax(class_probabilities)
            if predicted_class_index==0:
                Final_pred="Angry"
            elif predicted_class_index==1:
                Final_pred="Happy"     
            
            
        elif predicted_class_index==1:#model4
            predictions = model4.predict(MSG)
            class_probabilities = predictions[0]
            predicted_class_index = np.argmax(class_probabilities)
            if predicted_class_index==0:
                Final_pred="Sad"
            elif predicted_class_index==1:
                Final_pred="Neutral"
    return Final_pred

def predict_emotion(audio_file):
    # Preprocess audio file
    mel_spectrogram = predict_model(audio_file)
    
    # Use models_system to make predictions
    emotion_prediction = models_system(mel_spectrogram)

    return emotion_prediction

audio_file_path = r"D:\socialbot\speech\recorded_audio.wav"
predicted_emotion = predict_emotion(audio_file_path)
print("Predicted Emotion:", predicted_emotion)

# Write the final detected emotion to the output file in D:\1 directory
output_file_path = r"D:\socialbot\emotion.txt"  # Adjust the path as needed
with open(output_file_path, 'a') as output_file:
    output_file.write(f"The user's speech is {predicted_emotion}\n")

output_file_path = r"D:\socialbot\emotion4GPT.txt"  # Adjust the path as needed
with open(output_file_path, 'a') as output_file:
    output_file.write(f"The user's speech is detected by the error-prone model as [{predicted_emotion}]. The speech models can sometimes be trusted if same as others.\n")
