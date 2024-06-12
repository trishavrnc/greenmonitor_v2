import os
import tensorflow as tf
import numpy as np

data_dir = 'data'
family_names = [folder_name for folder_name in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, folder_name))]

model_path = 'models/plantae.h5'
model = tf.keras.models.load_model(model_path)

def classify_images(image_path): # RUN THROUGH MODEL
    input_image = tf.keras.utils.load_img(image_path, target_size=(128, 128))
    input_image_array = tf.keras.utils.img_to_array(input_image)
    input_image_exp_dim = tf.expand_dims(input_image_array, 0)

    predictions = model.predict(input_image_exp_dim)
    result = tf.nn.softmax(predictions[0]).numpy()  # Convert tensor to NumPy array
    
    top_3_indices = np.argsort(result)[-3:][::-1]
    top_3_scores = result[top_3_indices]
    
    outcome = "Top 3 matches:\n"
    for i in range(3):
        outcome += f"{i+1}. {family_names[top_3_indices[i]]} with a score of {top_3_scores[i] * 100:.2f}%\n"
    
    return outcome

image_path = "ebenaceae_test.jpg"
result = classify_images(image_path)
print(result)