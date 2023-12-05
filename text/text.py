import tkinter as tk
from tkinter import scrolledtext, simpledialog
from datetime import datetime
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Load the BERT model and tokenizer
model_path = r"D:\socialbot\text\emotion_model_v1"
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Create a mapping between numerical labels and emotional categories
data_dict = {0: 'happy', 1: 'anger', 2: 'love', 3: 'surprise', 4: 'fear', 5: 'sadness'}
my_dict = {data_dict[k]: k for k in data_dict}

def get_user_input():
    user_input = simpledialog.askstring("Input", "Enter your message:")
    if user_input:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        message = f"{timestamp} {user_input}\n"
        messagenew = f"The user's original text is {user_input}. This is your most reliable source.\n"
        input_entry.insert(tk.END, message)
        save_to_file(message)
        save_to_gptfile(messagenew)
        analyze_sentiment(user_input)
        # Refresh the displayed text in the input_entry widget
        input_entry.update_idletasks()

def save_to_file(message):
    with open(r"D:\socialbot\text\chat.txt", "a") as file:
        file.write(message)

def save_to_gptfile(messagenew):
     with open(r"D:\socialbot\emotion4GPT.txt", 'w') as output:
        output.write(messagenew)

def analyze_sentiment(text):
    emotion = test_model(text)
    print(f"Emotion for '{text}': {emotion}")
    
    # Format the result
    formatted_result = f"The user's text is {emotion}"

    # Save the result to the output file
    with open(r"D:\socialbot\emotion.txt", "a") as output_file:
        output_file.write(formatted_result + "\n")
    
    # Append the result to the input_entry widget
    input_entry.insert(tk.END, formatted_result + "\n")

    with open(r"D:\socialbot\emotion4GPT.txt", 'a') as output_file:
        output_file.write(f"The user's text is detected by the error-prone model as [{emotion}]. Text models are usually the least reliable, and you need to rely more on the [Original text] to judge emotions for yourself\n")
    # Refresh the displayed text in the input_entry widget
    input_entry.update_idletasks()

def test_model(text):
    text = text.lower()
    text = tokenizer(text, return_tensors="pt")
    model.eval()
    with torch.no_grad():
        outputs = model(**text)
    # Use the default labels provided by the model
    pred = outputs.logits.argmax(axis=-1).flatten().tolist()
    # Map the numerical label to emotional category using my_dict
    emotion = data_dict.get(my_dict.get(pred[0], pred[0]), pred[0])
    return emotion

# Create the main window
window = tk.Tk()
window.title("Chat Input")

# Create a Text widget for user input
input_entry = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
input_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Create a button to prompt the user for input
input_button = tk.Button(window, text="User Input", command=get_user_input)
input_button.grid(row=1, column=0, pady=10)

# Create a button to exit the program
exit_button = tk.Button(window, text="Exit", command=window.destroy)
exit_button.grid(row=1, column=1, pady=10)

# Run the main loop
window.mainloop()