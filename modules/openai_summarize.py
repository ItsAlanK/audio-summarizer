from colors import Colors
from openai import OpenAI

class TextSummarizer:
    def __init__(self, openai_client, text):
        self.client = openai_client
        self.text = text

    def summarize_text(self):
        """
        Summarize the input text using the OpenAI GPT-3.5 Turbo model.

        Returns:
        - str: The summarized text.
        """
        try:
            print(Colors.YELLOW + "Summarizing text..." + Colors.RESET)
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Your job is to accept text files which are transcripts of audio files \
                        from online classes and summarize them."},
                    {"role": "user", "content": self.text},
                ]
            )
            summarized_text = response.choices[0].message.content
            print("Summarized text: " + summarized_text)
        except Exception as e:
            print(Colors.RED + f"Error during text summarization: {e}" + Colors.RESET)
            return None
        return summarized_text

    def write_summary_to_file(self, summary, output_file):
        """
        Write the provided summary to a file.

        Parameters:
        - summary (str): The summarized text to be written to the file.
        - output_file (str): The path to the output file.
        """
        try:
            if summary is not None:
                print(Colors.YELLOW + "Writing summary to file..." + Colors.RESET)
                with open(output_file, "w") as file:
                    file.write(summary)
                print(Colors.GREEN + f"Summary written to {output_file}" + Colors.RESET)
            else:
                print(Colors.RED + "Summary is None. Cannot write to file." + Colors.RESET)
        except (FileNotFoundError, PermissionError) as e:
            print(Colors.RED + f"Error writing summary to file: {e}" + Colors.RESET)
            return None
        return output_file
