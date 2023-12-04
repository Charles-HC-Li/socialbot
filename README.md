# Socialbot
## Code for socialbot‘s prototype

## As for prototype, it is only the most basic model such as BERT. Users can retrain complex models in train.ipynb under each folder according to requirements, or directly download SOTA model and import it into corresponding folders, and then use python files with the same name in each folder to directly use it

## README

Welcome to the SocialBot project! This repository contains the source code for a social bot that incorporates multiple modalities (face, speech, text) and uses a Language Model (LLM) Agent for making judgments. Follow the instructions below to set up and use the SocialBot.

## Table of Contents
- [Training](#training)
  - [Face Modality](#face-modality)
  - [Speech Modality](#speech-modality)
  - [Text Modality](#text-modality)
- [Recording](#recording)
- [Data Input and Emotion Recognition](#data-input-and-emotion-recognition)
- [Using LLM Agent](#using-llm-agent)
- [Building Social Bot](#building-social-bot)
- [Future Work](#future-work)

## Training

### Face Modality

1. Navigate to the `face` directory:
   ```bash
   cd face
   ```

2. Run the training script:
   ```bash
   python train.py
   ```

### Speech Modality

1. Navigate to the `speech` directory:
   ```bash
   cd speech
   ```

2. Run the training script:
   ```bash
   python train.py
   ```

### Text Modality

1. Navigate to the `text` directory:
   ```bash
   cd text
   ```

2. Run the training script:
   ```bash
   python train.py
   ```

## Recording

1. Run the recording script:
   ```bash
   python speech/recording.py
   ```

## Data Input and Emotion Recognition

1. Run the following scripts for data input and emotion recognition:
   ```bash
   python face/face.py
   python speech/speech.py
   python text/text.py
   ```

## Using LLM Agent

1. Run the LLM Agent script:
   ```bash
   python call.py
   ```

   Note: This step uses the LLM Agent for making judgments based on individual modalities(This step can be omitted if you want to use a multimodal model to obtain the emotion, or use the original model emotion or the emotion of a single mode).

## Building Social Bot

1. Navigate to the `LLM` directory:
   ```bash
   cd LLM
   ```

2. Implement the necessary operations to build the social bot using the provided outputs.

3. Customize the `call.py` script to call external APIs and compile the final results.

## Future Work

- **Multi-Agent System Optimization:** Explore the use of a Multi-Agent system to optimize decision-making instead of a single Agent.
- **LLM Personalization:** Enhance the LLM with more personalized operations to improve social bot interactions.
- **Graphical User Interface (GUI):** Develop a user-friendly GUI to run all operations in a graphical environment.

Congratulations! You have successfully set up and trained the SocialBot. Feel free to experiment and enhance the functionality as needed.
