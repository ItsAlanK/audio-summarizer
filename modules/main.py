from openai import OpenAI
from colors import Colors
from openai_transcribe import AudioTranscriber

openai_client = OpenAI()
audio_source = "resources/harvard.wav"
output_file_path = "resources/transcribed-audio.txt"

transcriber = AudioTranscriber(openai_client, audio_source)
transcription_result = transcriber.transcribe_audio()

transcriber.write_transcription_to_file(transcription_result, output_file_path)