# Document Verification System

## Project Overview

This project uses deep learning models to verify documents such as driving licenses and passports.

### TDLR;

## Project Structure

- `config.json`: Configuration for document types and verification criteria.
- `dataset/`: Contains document images and labels.
- `models/`: Contains trained models and converted TFLite models.
- `scripts/`: Python scripts for loading data, training, conversion, and OCR.
- `requirements.txt`: Project dependencies.

## How to Run

1. Install dependencies: `pip install -r requirements.txt`
2. Load Config: `python scripts/config_loader.py`
3. Load and Augment Data: `python scripts/load_data.py`
4. Train the Model: `python scripts/train_model.py`
5. Convert to TFLite: `python scripts/convert_to_tflite.py`
6. OCR Processing: `python scripts/ocr_processing.py`

### TABLE OF CONTENTS

```bash
document_verification/
│
├── config.json # Configuration for document types and criteria
├── dataset/ # Folder containing images of documents
│ ├── images/ # Sub-folder for document images
│ └── labels.csv # CSV file with labels for each document image
│
├── models/ # Folder for storing trained models
│ ├── trained_model.h5 # Trained Keras model
│ └── tflite_model.tflite # Converted TensorFlow Lite model
│
├── scripts/ # Folder for all Python scripts
│ ├── config_loader.py # Script for loading configurations
│ ├── load_data.py # Script for loading and augmenting data
│ ├── train_model.py # Script for training and evaluating the model
│ ├── convert_to_tflite.py # Script for converting the model to TFLite
│ └── ocr_processing.py # Script for OCR processing
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```
