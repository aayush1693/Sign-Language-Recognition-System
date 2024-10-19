# Sign-Language-Recognition-System

This project aims to recognize sign language gestures using advanced machine learning techniques. It is primarily written in Jupyter Notebook and Python. The system utilizes deep learning models to detect and interpret sign language in real-time, providing an invaluable tool for communication with hearing-impaired individuals.

## Features

- Real-time sign language detection
- High accuracy with deep learning models
- User-friendly interface
- Extensive dataset for training and testing

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/aayush1693/Sign-Language-Recognition-System.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Sign-Language-Recognition-System
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Open the Jupyter Notebook:
   ```sh
   jupyter notebook
   ```
2. Run the cells in the notebook to start the sign language recognition system.

## Project Structure

- `sign_language_recognition_system (1).py`: Main Python script containing the implementation of data loading, preprocessing, model development, training, and evaluation.
- `Sign_Language_Recognition_System.ipynb`: Jupyter Notebook with the same functionality as the Python script, useful for interactive exploration and visualization.

## Data Loading and Preprocessing

The dataset is provided in two CSV files: `sign_mnist_train.csv` and `sign_mnist_test.csv`. Each row in the CSV file is a training sample with the label at the 0th index and the rest of the entries being pixel values of the image.

## Model Architecture

The model is a Sequential Convolutional Neural Network (CNN) consisting of:
- Three Convolutional Layers followed by MaxPooling Layers.
- A Flatten layer to convert the matrix output into a vector.
- Two Fully Connected (Dense) layers.
- BatchNormalization layers for stable and fast training.
- A Dropout layer to avoid overfitting.
- The final layer outputs soft probabilities for the 24 classes.

## Training and Evaluation

The model is compiled using the Adam optimizer and categorical cross-entropy loss function. The training process includes data augmentation techniques like rescaling, shearing, zooming, and horizontal flipping to improve the model's robustness.

After training, the model achieves an accuracy of approximately 92%, indicating its effectiveness in recognizing sign language gestures.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Special thanks to all contributors.
- Inspired by various sign language recognition systems.

## Conclusion
By using a simple CNN model, we achieve an accuracy of 92%, demonstrating the potential of this technology to aid in building applications that help bridge communication gaps for the hearing-impaired community.
