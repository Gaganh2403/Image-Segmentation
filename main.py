import cv2
import numpy as np
import os
from sklearn.cluster import KMeans

input_folder = "input"
output_folder = "output"

# Check input folder
images = os.listdir(input_folder)
if not images:
    print("No input images found!")
    exit()

for image_name in images:
    image_path = os.path.join(input_folder, image_name)
    img = cv2.imread(image_path)

    # Resize for faster processing
    img = cv2.resize(img, (512, 512))

    # Convert to LAB for better clustering
    lab_image = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    pixels = lab_image.reshape(-1, 3)

    # Apply K-Means Clustering
    k = 5  # Number of clusters (can be changed)
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(pixels)

    segmented_img = kmeans.labels_.reshape(img.shape[:2])

    # Create empty mask
    mask = np.zeros_like(img)

    # Assign random colors to each cluster (object)
    for cluster in range(k):
        random_color = np.random.randint(0, 255, 3)
        mask[segmented_img == cluster] = random_color

    # Optional: Remove Background
    gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
    final_result = cv2.bitwise_and(mask, mask, mask=binary)

    output_path = os.path.join(output_folder, f"output_{image_name}")
    cv2.imwrite(output_path, final_result)

print("Segmentation Completed Successfully!")
