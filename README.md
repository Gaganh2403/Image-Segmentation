# Image-Segmentation
<h1 align="center" style="color:#2E86C1">🎯 Color-Based Image Segmentation using K-Means Clustering 🎯</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/OpenCV-4.x-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Scikit--Learn-yellow?style=for-the-badge">
</p>

---

##  Overview

This project focuses on **segmenting objects in images based on color** using the **K-Means Clustering** algorithm combined with the **LAB color space** for enhanced perceptual performance. It takes all images from an `input/` folder, segments them into color-based regions, and saves the final segmented results in an `output/` folder.

---

##  Why LAB Color Space?

Unlike RGB, the **LAB color space** separates the luminance (lightness) from color information, making clustering results more perceptually accurate. This allows for better segmentation of objects based on color differences!

---

##  Features

-  Color-based segmentation with K-Means Clustering  
-  Automatic folder-wise image processing  
-  Optional background removal  
-  Random color mask generation per cluster  
-  Resized images for faster processing  
-  Easy integration with future ML-based enhancements

---

##  Technologies Used

| Tool         | Purpose                         |
|--------------|---------------------------------|
| Python 🐍     | Core programming language       |
| OpenCV 📷     | Image handling and processing   |
| NumPy 🔢      | Numerical operations            |
| Scikit-Learn 🤖 | K-Means Clustering algorithm   |
| OS 📂         | File management                 |

---

##  Sample Output

| Original Image | Segmented Output |
|----------------|------------------|
| ![](input/img4.jpg) | ![](output/output_img4.jpg) |

---

##  How It Works

1. 🗂️ Reads all images from the `input/` folder  
2. 📏 Resizes each image to 512x512 pixels  
3. 🌈 Converts image from BGR to LAB color space  
4. 📊 Flattens and feeds pixels into the **K-Means** clustering model  
5. 🎨 Assigns a **random color** to each cluster  
6. 🧽 Removes unwanted background noise  
7. 💾 Saves the segmented result in the `output/` folder

---

## 🛠️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# Install dependencies
pip install opencv-python numpy scikit-learn

# Place your images in the input folder
mkdir input output
# Add your .jpg or .png images to the input folder

# Run the script
python segment.py
