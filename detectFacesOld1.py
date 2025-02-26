import cv2
import os

def detect_faces(image_path, output_dir, face_cascade_path='haarcascade_frontalface_default.xml'):
    """
    Detect faces in an image and save the cropped face regions.

    Args:
        image_path (str): Path to the image file.
        output_dir (str): Directory to save cropped faces.
        face_cascade_path (str): Path to Haar Cascade XML file for face detection.
    """
    os.makedirs(output_dir, exist_ok=True)  # Ensure the output directory exists
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + face_cascade_path)

    # Read the image
    img = cv2.imread(image_path)
    if img is None:  # Handle missing or invalid images
        print(f"Warning: Unable to read image {image_path}")
        return

    # Convert to grayscale for face detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for i, (x, y, w, h) in enumerate(faces):
        face = img[y:y+h, x:x+w]
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
