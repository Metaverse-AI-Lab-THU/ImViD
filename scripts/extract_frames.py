import os
import argparse
import subprocess
import logging


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    return parser.parse_args()


def run_ffmpeg(input_file, video_output_path):
    os.makedirs(video_output_path, exist_ok=True)
    cmd = [
        "ffmpeg",
        "-i",
        input_file,
        "-start_number",
        "0",
        "-loglevel",
        "error",
        os.path.join(video_output_path, f"%05d.png"),
    ]
    try:
        logging.info(f"Running command: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        return False
    return True


def main():
    logging.basicConfig(level=logging.INFO)
    args = parse_arguments()
    input_path = os.path.abspath(args.input)
    output_path = os.path.abspath(args.output)

    if not os.path.exists(input_path):
        logging.error(f"Input path {input_path} does not exist.")
        return
    videos = [
        video for video in os.listdir(input_path) if video.lower().endswith(".mp4")
    ]
    if not videos:
        logging.error(f"No video files found in {input_path}.")
        return
    os.makedirs(output_path, exist_ok=True)

    sorted_videos = sorted(videos)
    for video in sorted_videos:
        video_path = os.path.join(input_path, video)
        cam_name = os.path.splitext(video)[0]
        video_output_path = os.path.join(output_path, cam_name)
        success = run_ffmpeg(video_path, video_output_path)
        if not success:
            logging.error(f"Skipping {video_path} due to errors.")


if __name__ == "__main__":
    main()
