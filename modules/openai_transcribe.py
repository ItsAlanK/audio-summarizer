from colors import Colors
from openai import OpenAI

class AudioTranscriber:
    def __init__(self, openai_client, audio_source):
        self.client = openai_client
        self.audio_source = audio_source


    def transcribe_audio(self):
        # GET AUDIO AND SEND TO OPENAI FOR TRANSCRIPTION
        print(Colors.YELLOW + "Transcribing audio..." + Colors.RESET)
        audio_file = open(self.audio_source, "rb")
        transcription = self.client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file,
            response_format="text"
            )
        print(transcription)
        return(transcription)

    def write_transcription_to_file(self, transcription, ouptut_file):
        # WRITE TRANSCRIBED AUDIO TO FILE
        print(Colors.YELLOW + "Writing transcription to file..." + Colors.RESET)
        with open(ouptut_file, "w") as file:
            file.write(transcription)