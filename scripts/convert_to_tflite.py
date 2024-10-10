import tensorflow as tf

# Load the trained model
model = tf.keras.models.load_model('../models/trained_model.h5')

# Convert to TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]  # Apply optimization for smaller size
tflite_model = converter.convert()

# Save the TFLite model
with open('../models/tflite_model.tflite', 'wb') as f:
    f.write(tflite_model)
