from tkinter import Tk, Label, Button, Frame, LEFT
from PIL import Image, ImageTk
import pyttsx3
import threading
import subprocess
import webbrowser



def text_to_speech(text):
    engine = pyttsx3.init()
    set_english_voice(engine)
    engine.say(text)
    engine.runAndWait()

def set_english_voice(engine):
    for voice in engine.getProperty('voices'):
        if 'english' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

def conversation(text):
    t = threading.Thread(target=text_to_speech, args=(text,))
    t.start()

def run_app(app_name):
    subprocess.run([app_name])

def run_browser(search_word):
    webbrowser.open(f"https://www.google.com/search?q={search_word}")

def activate_button(buttons, commands, active_index, commands_state):
    for i, button in enumerate(buttons):
        if i == active_index:
            button['text'] = commands[i] + ' - Activated'
            action = commands_state[i].split()[-1]
            if action == 'app':
                app_name = commands_state[i].replace(' app', '')
                run_app(app_name)
            elif action == 'search_word':
                search_word = commands_state[i].replace(' search_word', '')
                run_browser(search_word)
        else:
            button['text'] = commands[i]

# Function to create the GUI
def create_gui(commands, commands_state):
    tk = Tk()
    tk.title('Proposed Activities')
    tk.geometry("1100x400")

    frame = Frame(tk)
    frame.pack(padx=10, pady=10, fill='both', expand=True)

    try:
        # Load the image
        image_path = '/home/smartlab-rio/codes/robot.jpg'
        image = Image.open(image_path)
        #image = image.resize((300, 300), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        label = Label(frame, text='Please select the activity you want.', image=photo, compound='top')
        label.image = photo
        label.pack(pady=(0, 20))

    except Exception as e:
        print(f"Error loading image: {e}")
        label = Label(frame, text='Please select the activity you want.')
        label.pack(pady=(0, 20))

    buttons = []
    button_width = 35
    for i, command in enumerate(commands):
        button = Button(frame, text=command, width=button_width, command=lambda i=i: activate_button(buttons, commands, i, commands_state))
        button.pack(side=LEFT, padx=10, expand=True)
        buttons.append(button)

    tk.mainloop()

# Main function
def main():
    conversation("It's completely normal to feel sad at times. Would you like to talk about what's causing you to feel this way?")
    activities = ["listening to classical music", "practicing meditation", "writing in a journal"]
    search_word_or_app_for_activities = ["rhythmbox app", "meditation search_word", "gedit app"]
    create_gui(activities, search_word_or_app_for_activities)

if __name__ == '__main__':
    main()
