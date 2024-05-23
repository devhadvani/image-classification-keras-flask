from flask import Flask, request, render_template, redirect, url_for
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from collections import defaultdict

app = Flask(__name__)

# Load the trained model -
model = load_model('cifar10_model2.h5')

# Define the classes
classes = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]

# Ensure the uploads directory exists
UPLOAD_FOLDER = 'static/uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(url_for('index'))

    files = request.files.getlist('file')

    if not files or files[0].filename == '':
        return redirect(url_for('index'))

    predictions = defaultdict(list)

    for file in files:
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            
            img = image.load_img(filepath, target_size=(32, 32))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0) / 255.0
            
            preds = model.predict(img_array)
            class_idx = np.argmax(preds[0])
            class_name = classes[class_idx]
            
            predictions[class_name].append(filepath)
    
    return render_template('index.html', predictions=predictions)

if __name__ == "__main__":
    app.run(debug=True)
