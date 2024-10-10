import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.models import Sequential
from sklearn.model_selection import train_test_split

# Load data from the data loading script
from load_data import load_data, augment_data

# Load dataset and augment
data_dir = '../dataset/images'
labels_file = '../dataset/labels.csv'
images, labels = load_data(data_dir, labels_file)
datagen = augment_data(images)

# Split dataset
x_train, x_val, y_train, y_val = train_test_split(images, labels, test_size=0.2, random_state=42)

# Define and compile the model
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
base_model.trainable = False
model = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
batch_size = 32
epochs = 10
train_generator = datagen.flow(x_train, y_train, batch_size=batch_size)
model.fit(train_generator, epochs=epochs, validation_data=(x_val, y_val))

# Save the model
model.save('../models/trained_model.h5')
