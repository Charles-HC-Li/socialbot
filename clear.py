# Import necessary libraries
import os

# Specify the path to the emotion.txt file
file_paths = [r"D:\socialbot\emotion.txt", r"D:\socialbot\text\chat.txt", r"D:\socialbot\emotion4GPT.txt"]

def clear_emotion_file():
    for file_path in file_paths:
        with open(file_path, "w") as file:
            # Clear the contents of the file
            file.truncate(0)

if __name__ == "__main__":
    # Run the function to clear the emotion.txt file
    clear_emotion_file()
    print(f"The contents have been cleared.")
