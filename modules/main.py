import os
from openai import OpenAI
from colors import Colors
from openai_transcribe import AudioTranscriber
from audio_extractor import extract_audio_from_video
from openai_summarize import TextSummarizer


openai_api_key = os.environ.get('OPENAI_API_KEY')
openai_client = OpenAI(api_key=openai_api_key)
video_file_path = "resources/video.mp4"
output_audio_file_path = audio_source = "resources/audio.mp3"
output_transcription_file_path = "resources/transcribed-audio.txt"
output_summary_file_path = "resources/summarized-audio.txt"

# # Extract audio from video
# extract_audio_from_video(video_file_path, output_audio_file_path)

# # Transcribe audio
# transcriber = AudioTranscriber(openai_client, audio_source)
# transcription_result = transcriber.transcribe_audio()
# transcriber.write_transcription_to_file(transcription_result, output_transcription_file_path)

# Temp opens transcription file without needing to run the above code
with open ("resources/transcribed-audio.txt", "r") as file:
    transcription_result = file.read()

# Summarize text
summarizer = TextSummarizer(openai_client, transcription_result)
summarized_text = summarizer.summarize_text()
summarizer.write_summary_to_file(summarized_text, output_summary_file_path)