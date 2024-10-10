import os
import numpy as np
import pandas as pd
import tensorflow as tf

def load_data(data_dir, labels_file):
    labels_df = pd.read_csv(labels_file)
    images = []
    labels = []
    for idx, row in labels_df.iterrows():
        image_path = os.path.join(data_dir, row['filename'])
        image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
        image = tf.keras.preprocessing.image.img_to_array(image) / 255.0
        images.append(image)
        labels.append(row['is_authentic'])
    return np.array(images), np.array(labels)

def augment_data(images):
    datagen = tf.keras.preprocessing.image.ImageDataGenerator(
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.2,
        zoom_range=0.1,
        horizontal_flip=True,
        fill_mode='nearest'
    )
    return datagen

# Load and augment data
if __name__ == "__main__":
    data_dir = '../dataset/images'
    labels_file = '../dataset/labels.csv'
    images, labels = load_data(data_dir, labels_file)
    datagen = augment_data(images)
