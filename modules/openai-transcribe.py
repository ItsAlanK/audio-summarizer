from openai import OpenAI
client = OpenAI()

audio_file= open("resources/harvard.wav", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file,
  response_format="text"
)
print(transcription)