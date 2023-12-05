import cv2
import numpy as np
import tensorflow as tf
from collections import Counter
import time

# Load model
model_path = r"D:\socialbot\face\model.h5"  # Adjust the path as needed
model = tf.keras.models.load_model(model_path)

# Load face cascade detector
face_cascade_path = r"D:\socialbot\face\haarcascade_frontalface_default.xml"  # Adjust the path as needed
face_cascade = cv2.CascadeClassifier(face_cascade_path)

# Emotion classes
class_names = ["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]

# Open webcam
video = cv2.VideoCapture(0)

# List to store detected emotions
detected_emotions = []

# Duration for emotion detection in seconds
detection_duration = 5  # Adjust as needed

# Time at which emotion detection started
start_time = time.time()

while time.time() - start_time < detection_duration:
    # Read frame from the webcam
    ret, frame = video.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    if len(faces) == 0:
        # No faces detected
        emotion_label = "None Face Detected"
    else:
        for (x, y, w, h) in faces:
            # Extract the face region
            face_roi = frame[y:y + h, x:x + w]

            # Resize the face image to the required input size for the model
            face_resized = cv2.resize(face_roi, (48, 48))

            # Normalize and expand dimensions
            face_normalized = face_resized / 255.0
            face_input = np.expand_dims(face_normalized, axis=0)

            # Predict emotion
            predictions = model.predict(face_input)
            emotion_label = class_names[np.argmax(predictions)]

            # Store detected emotion in the list
            detected_emotions.append(emotion_label)

            # Draw rectangle and display emotion label
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, emotion_label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow("Emotion Detection", frame)

    key = cv2.waitKey(1)
    if key == ord('x') or key == 27 or cv2.getWindowProperty("Emotion Detection", cv2.WND_PROP_VISIBLE) < 1:
        break

# Release webcam resources
video.release()

# Close the window
cv2.destroyAllWindows()

# Choose the most frequent emotion as the final output
if len(detected_emotions) == 0:
    final_emotion = "None Face Detected"
else:
    final_emotion = Counter(detected_emotions).most_common(1)[0][0]

# Write the final detected emotion to the output file in D:\1 directory
output_file_path = r"D:\socialbot\emotion.txt"  # Adjust the path as needed
with open(output_file_path, 'a') as output_file:
    output_file.write(f"The user's face is {final_emotion}\n")

output_file_path = r"D:\socialbot\emotion4GPT.txt"  # Adjust the path as needed
with open(output_file_path, 'a') as output_file:
    output_file.write(f"The user's face is detected by the error-prone model as [{final_emotion}]. The face models are pretty reliable, except that it's easy to recognize 'Neural' as 'Surprise'.\n")

print("Final Detected Emotion:", final_emotion)
