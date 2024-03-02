# audio-summarizer
AI script to summarize audio files. Hopefully I can get the cliffnotes from classes this way.

## Modules

- audio_extractor
    - Takes a video.mp4 file in the resources folder
    - Extracts audio to resources/audio.mp3
- openai_transcribe
    - Takes audio and feeds it to OpenAI Whisper
    - Recieves transcript and writes to a resources/transcribed-audio.txt

- openai_summarize
    - Takes transcript text and sends to OpenAI GPT3.5
    - Receives summary of text and writes to resources/summarized-audio.txt

## Env Setup Steps

- `source openai-env/bin/activate`
- `source ~/.zshrc`
- Test with `echo $OPENAI_API_KEY`