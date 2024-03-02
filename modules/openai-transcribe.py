from openai import OpenAI
from colors import Colors


client = OpenAI()
audio_source = "resources/harvard.wav"

# GET AUDIO AND SEND TO OPENAI FOR TRANSCRIPTION
print(Colors.YELLOW + "Transcribing audio..." + Colors.RESET)
audio_file= open(audio_source, "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file,
  response_format="text"
)
print(transcription)

# WRITE TRANSCRIBED AUDIO TO FILE
print(Colors.YELLOW + "Writing transcription to file..." + Colors.RESET)
with open("resources/transcribed-audio.txt", "w") as file:
    # Write text to the file
    file.write(transcription)