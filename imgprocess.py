import tensorflow as tf
from tensorflow.keras.models import load_model, Model
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt

# Load your pre-trained model
model = load_model('models/plantae_resnet.h5')

# Print model summary to see layer names and indices
model.summary()

# Load and preprocess a sample image
img_path = 'alismatales.png'  # Replace with the path to your image
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = tf.keras.applications.resnet50.preprocess_input(img_array)  # Preprocess for ResNet50

# Extract intermediate layers to visualize
layer_names = [layer.name for layer in model.layers if 'conv' in layer.name or 'block' in layer.name]  # Adjusted for ResNet-like models

outputs = [model.get_layer(name).output for name in layer_names]
visualization_model = Model(inputs=model.input, outputs=outputs)

# Get intermediate layer outputs for the input image
activations = visualization_model.predict(img_array)

# Plotting the activations
def display_activation(activation_maps, num_rows=1):
    for layer_activation in activation_maps:
        num_filters = layer_activation.shape[-1]  # Number of filters in the layer
        size = layer_activation.shape[1]  # Assuming square feature maps
        num_cols = num_filters // num_rows

        plt.figure(figsize=(2 * num_cols, 2 * num_rows))
        for i in range(num_filters):
            plt.subplot(num_rows, num_cols, i + 1)
            plt.imshow(layer_activation[0, :, :, i], cmap='viridis')
            plt.axis('off')

    plt.tight_layout()
    plt.show()

# Display intermediate activations
display_activation(activations, num_rows=4)
