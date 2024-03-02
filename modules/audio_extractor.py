from colors import Colors
from moviepy.video.io.VideoFileClip import VideoFileClip


def extract_audio_from_video(video_path, output_audio_path):
    """
    Extract audio from a video file and save it as an MP3 file.

    Parameters:
    - video_path (str): The path to the input video file.
    - output_audio_path (str): The desired path for the output MP3 audio file.

    This function uses the 'moviepy' library to load the video clip, extract its
    audio, and save it as an MP3 file. The extracted audio is saved to the specified
    output path.
    """
    try:
        # Load the video clip
        video_clip = VideoFileClip(video_path)
        
        # Extract audio
        audio_clip = video_clip.audio
        
        # Save audio as MP3
        audio_clip.write_audiofile(output_audio_path, codec='mp3')
        
        print(Colors.GREEN + f"Audio successfully extracted and saved to {output_audio_path}" + Colors.RESET)
    except Exception as e:
        print(Colors.RED + f"Error: {e}" + Colors.RESET)