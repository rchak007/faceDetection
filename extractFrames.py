import cv2
import os

def extract_frames(video_path, output_dir, interval=30):
    """
    Extract frames from a video at the specified interval.

    Args:
        video_path (str): Path to the video file.
        output_dir (str): Directory to save extracted frames.
        interval (int): Interval in frames to save (e.g., every 30 frames).
    """
    os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():  # Fix 1: Check if the video file is valid
        print(f"Error: Unable to open video file {video_path}")
        return

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break  # End of video

        # Save every `interval`-th frame
        if frame_count % interval == 0:
            frame_name = os.path.join(output_dir, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_name, frame)

        frame_count += 1

    cap.release()
    print(f"Frames extracted from {video_path} to {output_dir}")

# Main script
videos_folder = "dataset"
output_folder = "frames"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

if not os.path.exists(videos_folder):  # Fix 2: Check if the dataset folder exists
    print(f"Error: Dataset folder '{videos_folder}' does not exist. Exiting.")
    exit(1)

# Loop through all videos in the dataset folder
for video_file in os.listdir(videos_folder):
    video_path = os.path.join(videos_folder, video_file)
    if not video_file.lower().endswith(('.mp4', '.mkv', '.avi', '.mov')):  # Fix 3: Check for valid video extensions
        print(f"Skipping non-video file: {video_path}")
        continue

    video_output = os.path.join(output_folder, os.path.splitext(video_file)[0])
    os.makedirs(video_output, exist_ok=True)  # Ensure subfolder for video frames exists
    extract_frames(video_path, video_output, interval=30)
