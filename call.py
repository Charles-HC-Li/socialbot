import openai

openai.api_key = 'YOUR_API_KEY'

emotion_file_path = r'D:\socialbot\emotion4GPT.txt'
with open(emotion_file_path, 'r', encoding='utf-8') as emotion_file:
    emotion_content = emotion_file.read()

messages = [
    {"role": "system", "content": "Based on the emotion identified by the error-prone low model, you need to give the most likely final emotion in [happy, sad, angery, fear, love, disappointed, neutral, disgust] . You only need to give a one-word reply."},
    {"role": "user", "content": "Keep in mind that the previous low-end model is error-prone, you can not completely beliece those detect results made by error-prone model. And you'll need to rely most on the original text of the user himself (if it exists). Common errors include the face model often identifying neutral as surprise, and the word model often identifying emotions based only on the presence of words, even when a sentence like 'I am not happy' is obviously sad"},
    {"role": "user", "content": "For Example:'When the original text is [I am not happy], the result for face model is [sad],  for the speech model is [natural], and for the text model is [happy], obviously the text model is wrong again, and your output should be ```sad```'"}, 
    {"role": "user", "content": f"{emotion_content}"},  
]

def generate_text(max_tokens=2):
    response = openai.Completion.create(
        engine="GPT-4",
        messages=messages,
        max_tokens=max_tokens
    )
    return response.choices[0].text.strip()

def save_to_file(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

generated_text = generate_text()

file_path = r'D:\socialbot\GPT.txt'
save_to_file(file_path, generated_text)

print(f"Emotion saved: {file_path}")
