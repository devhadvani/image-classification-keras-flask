# CIFAR-10 Image Classification Web App

This project demonstrates how to build an image classification web application using the CIFAR-10 dataset, TensorFlow, and Flask. The web application allows users to upload images and classify them into one of 10 categories.

## Features

- Train a Convolutional Neural Network (CNN) on the CIFAR-10 dataset.
- Evaluate the model on test data.
- Save and load the trained model.
- Upload images through a web interface and classify them.
- Display classification results with corresponding images.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/devhadvani/image-classification-keras-flask.git
    cd image-classification-keras-flask
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Train the Model

Run the script to train the CNN model on the CIFAR-10 dataset:

    ```bash
    python train_model.py
    ```

The trained model will be saved as `cifar10_model.h5`.

### Run the Web Application

1. Start the Flask web application:

    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. Use the web interface to upload images and classify them.

## Directory Structure

    ```plaintext
    cifar10-image-classification-web-app/
    │
    ├── app.py                 # Flask web application
    ├── train_model.py         # Script to train the CNN model
    ├── requirements.txt       # Python dependencies
    ├── templates/
    │   └── index.html         # HTML template for the web interface
    └── static/
        └── uploads/           # Directory to save uploaded images
    ```

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License.