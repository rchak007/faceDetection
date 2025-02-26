from mtcnn import MTCNN
import cv2
import os

def detect_faces(image_path, output_dir):
    """
    Detect faces in an image using MTCNN and save the cropped face regions.

    Args:
        image_path (str): Path to the image file.
        output_dir (str): Directory to save cropped faces.
    """
    os.makedirs(output_dir, exist_ok=True)  # Ensure the output directory exists
    detector = MTCNN()

    # Read the image
    img = cv2.imread(image_path)
    if img is None:  # Handle missing or invalid images
        print(f"Warning: Unable to read image {image_path}")
        return

    # Convert image to RGB (required by MTCNN)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Detect faces using MTCNN
    detections = detector.detect_faces(img_rgb)

    for i, detection in enumerate(detections):
        x, y, width, height = detection['box']
        # Ensure coordinates are within image bounds
        x, y = max(0, x), max(0, y)

        # Crop the detected face
        face = img[y:y+height, x:x+width]
        face_path = os.path.join(output_dir, f"{os.path.basename(image_path).split('.')[0]}_face_{i}.jpg")
        cv2.imwrite(face_path, face)
        print(f"Saved face to {face_path}")

# Main script
frames_folder = "frames"
faces_output = "faces"

# Check if the frames folder exists
if not os.path.exists(frames_folder):
    print(f"Error: Frames folder '{frames_folder}' does not exist. Exiting.")
    exit(1)

# Create the output directory for faces
os.makedirs(faces_output, exist_ok=True)

# Loop through subfolders in the frames folder
for video_folder in os.listdir(frames_folder):
    video_frames = os.path.join(frames_folder, video_folder)
    if not os.path.isdir(video_frames):  # Skip non-directory items
        print(f"Skipping non-directory item: {video_frames}")
        continue

    video_faces = os.path.join(faces_output, video_folder)
    os.makedirs(video_faces, exist_ok=True)

    # Process each frame in the subfolder
    for frame_file in os.listdir(video_frames):
        frame_path = os.path.join(video_frames, frame_file)
        if not frame_file.lower().endswith(('.jpg', '.jpeg', '.png')):  # Ensure valid image files
            print(f"Skipping non-image file: {frame_path}")
            continue

        # Detect faces in the frame and save them
        detect_faces(frame_path, video_faces)
