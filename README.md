# Face Detection MTCNN (Multi-Task Cascaded Convolutional Networks)



![image-20250225162255237](./Images/image-20250225162255237.png)





This repository contains two Python scripts for extracting frames from videos and detecting faces in those frames using MTCNN.

## Overview

1. **`extractFrames.py`**: Extracts frames from video files at a specified interval.
2. **`detectFaces.py`**: Detects faces in extracted frames and saves cropped face images.

## Requirements

Ensure you have Python installed and the following dependencies:

```bash
pip install opencv-python mtcnn numpy
```



## Usage

### 1. Extract Frames from Videos

Place your video files in a directory named `dataset/`, then run:

```
bash


CopyEdit
python extractFrames.py
```

- Extracted frames will be saved in `frames/` under subdirectories named after the video files.
- By default, frames are extracted every 30 frames.

### 2. Detect Faces in Frames

After extracting frames, detect faces by running:

```
bash


CopyEdit
python detectFaces.py
```

- It scans `frames/` for images and detects faces using MTCNN.
- Cropped face images are saved in `faces/` under subdirectories corresponding to the video files.

## Folder Structure

```
bashCopyEdit/repo_root
│── dataset/         # Place video files here
│── frames/          # Extracted frames are stored here
│── faces/           # Cropped face images are saved here
│── extractFrames.py # Script to extract frames from videos
│── detectFaces.py   # Script to detect faces in extracted frames
│── README.md        # Project documentation
```

## Customization

- Change the 

  frame extraction interval

   in 

  ```
  extractFrames.py
  ```

  :

  ```
  python
  
  
  CopyEdit
  extract_frames(video_path, video_output, interval=30)
  ```

- Adjust the **face detection model** in `detectFaces.py` if needed.

## Notes

- Ensure `dataset/` exists and contains video files before running `extractFrames.py`.
- `detectFaces.py` expects `frames/` to be populated before running.

## License

This project is licensed under the MIT License.

```
yamlCopyEdit
---

This README provides clear instructions and an easy-to-follow workflow. Let me know if you need modifications! 🚀
```







##### You said:

also give me description for Githib repo -  i am calling it - faceDetection



###### ChatGPT said:

Here's a concise and engaging **GitHub repository description** for your **`faceDetection`** repo:

**Short Description (For GitHub Repo Summary):**
🖼️🎥 A Python project for extracting frames from videos and detecting faces using MTCNN. Automatically processes videos, detects faces, and saves cropped images. 🚀

**Longer Description (For GitHub Repo About Section):**
`faceDetection` is a Python-based tool for detecting faces in videos. It first extracts frames from video files at a specified interval and then applies MTCNN (Multi-Task Cascaded Convolutional Networks) to detect and crop faces from those frames. This project is useful for preprocessing videos for facial recognition, AI model training, and dataset creation.

Let me know if you'd like to tweak the wording! 🚀