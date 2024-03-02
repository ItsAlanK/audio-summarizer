from colors import Colors
from openai import OpenAI

class AudioTranscriber:
    def __init__(self, openai_client, audio_source):
        self.client = openai_client
        self.audio_source = audio_source


    def transcribe_audio(self):
        """
        Transcribe audio using OpenAI API.

        This method sends the audio data from the specified source to the OpenAI API
        for transcription. It uses the 'whisper-1' model and expects the response
        in text format. The transcription result is printed, and the raw transcription
        text is returned.

        Returns:
        - str: The transcribed text.
        """
        try:
            print(Colors.YELLOW + "Transcribing audio..." + Colors.RESET)
            audio_file = open(self.audio_source, "rb")
            transcription = self.client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file,
                response_format="text"
                )
            print(Colors.GREEN + "Transcibed text:" + Colors.RESET)
            print(Colors.BLUE + transcription + Colors.RESET)
            return(transcription)
        except Exception as e:
            print(Colors.RED + f"Error during audio transcription: {e}" + Colors.RESET)
            return None
        finally:
            audio_file.close()  # Ensure the file is closed even if an exception occurs

    def write_transcription_to_file(self, transcription, ouptut_file):
        """
        Write the provided transcription to a file.

        Parameters:
        - transcription (str): The transcription to be written to the file.
        - output_file (str): The path to the output file.
        """
        try:
            print(Colors.YELLOW + "Writing transcription to file..." + Colors.RESET)
            with open(ouptut_file, "w") as file:
                file.write(transcription)
            print(Colors.GREEN + f"Transcription written to {ouptut_file}" + Colors.RESET)
        except (FileNotFoundError, PermissionError) as e:
            print(Colors.RED + f"Error writing transcription to file: {e}" + Colors.RESET)