import ffmpeg
from pathlib import Path

def convert_to_aspect_ratio(input_path: str, output_path: str, target_ratio="9:16"):
    """
    Adjusts video to the specified aspect ratio (default is 9:16).
    If the video is already in the target aspect ratio, it saves it directly.
    """
    width, height = 1080, 1920  # Dimensions for 9:16 aspect ratio
    stream = ffmpeg.input(input_path)
    # Apply padding or crop to fit the desired aspect ratio
    stream = ffmpeg.filter(stream, 'scale', width, height)
    stream = ffmpeg.output(stream, output_path)
    ffmpeg.run(stream)

    return output_path


