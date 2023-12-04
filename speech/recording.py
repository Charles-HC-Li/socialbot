import sounddevice as sd
import numpy as np
import wave

# Parameters
duration = 5  # Recording duration in seconds
sample_rate = 44100  # Sample rate

try:
    # Record audio
    print("Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
    print("Recording complete.")

    # Save audio to a WAV file in D:\1 directory
    output_file_path = r"D:\socialbot\speech\recorded_audio.wav"  # Adjust the path as needed

    with wave.open(output_file_path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(np.int16(audio_data).tobytes())

    print(f"Audio saved to {output_file_path}")

except Exception as e:
    print(f"Error: {e}")
