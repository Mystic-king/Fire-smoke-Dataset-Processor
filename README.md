# 🔥 Fire and Smoke Detection Dataset Processor

This repository contains scripts and notebooks for processing, analyzing, and balancing a fire and smoke detection dataset. The dataset consists of images and YOLOv8-style label files for `fire` and `smoke` detection.

---

## 📁 Project Structure

project/
│
├── images/ # Original training images
├── labels/ # YOLOv8 label files corresponding to each image
├── train/ # Alias for original dataset location
│ ├── images/
│ ├── labels/
│ └── labels.csv # CSV with columns: filename, fire, smoke
│
├── train_balanced/ # Balanced dataset created via L1-style downsampling
│ ├── images/
│ ├── labels/
│ └── labels.csv # Balanced CSV with same format
│
├── test/ # Test images and labels
├── valid/ # Validation images and labels
│
├── Fire_detection.ipynb # Jupyter Notebook for EDA and plotting class distributions
├── Labels_classifier.py # Script to convert YOLOv8 annotations into structured CSV format
├── balance_dataset.py # Script to rebalance the dataset using L1-style logic (optional)
└── data.yaml # YOLOv8-style config file defining dataset structure

---

## 🧪 Files & Their Purpose

### ✅ `Fire_detection.ipynb`
- Performs **Exploratory Data Analysis (EDA)** on the `labels.csv`.
- Shows **class distribution** for `fire` and `smoke`.
- Plots bar charts.
- Can be extended for sample visualization.

### ✅ `Labels_classifier.py`
- Parses YOLOv8 `.txt` annotation files.
- Converts them into a **CSV format** with the following structure:
                                                                        filename, fire, smoke
                                                                        img_001.jpg, 1, 0
- Used to prepare data for analysis and training.


### ✅ `Rebalancing_dataset.py` *(optional – create this if not already made)*
- Applies **L1-style regularization** logic by balancing the dataset:
- **Undersamples** the `fire=1` class.
- Keeps equal samples of `fire=0` and `fire=1`.
- Copies selected image and label files into a new directory: `train_balanced/`.

### ✅ `data.yaml`
- Configuration file used by **YOLOv8** to define paths for training, validation, and test datasets.

---

## ⚙️ How to Use

### 1. Generate `labels.csv`
python Labels_classifier.py

### 2. Run EDA
Open and execute Fire_detection.ipynb to view distributions.

3. Balance the dataset 
python Rebalancing_dataset.py

This will create a balanced version of your dataset in train_balanced/.# Fire-smoke-Dataset-Processor
