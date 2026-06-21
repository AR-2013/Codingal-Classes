import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np

# 1. Load Data
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize pixel values to be between 0 and 1
x_train, x_test = x_train / 255.0, x_test / 255.0

# CNNs require a channel dimension (28x28x1 for grayscale)
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

# 2. Implement Data Augmentation (As requested by the prompt)
# This adds random rotations and zooms to make the model robust
data_augmentation = models.Sequential([
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1),
])

# 3. Build a Better Neural Network Structure (CNN)
# Swapping 'delu' typo to standard 'relu' or advanced 'leaky_relu'
model = models.Sequential([
    layers.Input(shape=(28, 28, 1)),
    data_augmentation,  # Applies augmentation only during training
    
    # Convolutional layers pull out structural features from digits
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    # Flatten and Dense Classification Head
    layers.Flatten(),
    layers.Dense(128, activation='relu'), 
    layers.Dropout(0.2), # Prevents overfitting
    layers.Dense(10, activation='softmax')
])

# 4. Compile Model (Fixed missing comma and typo in loss name)
model.compile(
    optimizer='adam', # Experiment here! Try 'rmsprop' or 'sgd'
    loss='sparse_categorical_crossentropy', 
    metrics=['accuracy']
)

# 5. Train Model
print("Training model...")
model.fit(x_train, y_train, epochs=5, batch_size=64, validation_split=0.1)

# 6. Evaluate
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"\n🚀 Test accuracy: {test_acc:.4f}")

# 7. Predict and Plot (Fixed binary map typo)
predictions = model.predict(x_test)

# Squeeze dimensions back out to (28,28) just for plotting
plt.imshow(np.squeeze(x_test[0]), cmap=plt.cm.binary) 
plt.title(f"Predicted Label: {np.argmax(predictions[0])} | True Label: {y_test[0]}")
plt.axis('off')
plt.show()