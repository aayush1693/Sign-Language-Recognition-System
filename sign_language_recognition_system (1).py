# -*- coding: utf-8 -*-
"""Sign-Language-Recognition-System.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z6ejdOOgV-bzU2YYnc6kIU4sAsNgY5sN

# **Sign Language Recognition System using TensorFlow in Python**


---


The first step of any machine learning problem is finding the appropriate dataset. For Sign language recognition let’s use the Sign Language MNIST dataset. It has images of signs corresponding to each alphabet in the English language. Since the sign language of J and Z requires motion, those two classes are not available in the dataset.

Importing Libraries

---


Python libraries make it very easy for us to handle the data and perform typical and complex tasks with a single line of code.




*   Pandas – This library helps to load the data frame in a 2D array format and has multiple functions to perform analysis tasks in one go
*   Numpy – Numpy arrays are very fast and can perform large computations in a very short time.
*   Matplotlib – This library is used to draw visualizations.
*   Tensorflow – This is an open-source library that is used for Machine Learning and Artificial intelligence and provides a range of functions to achieve complex functionalities with single lines of code.
"""

import string
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator

"""Importing Dataset

---


The dataset is available as two CSV files, sign_mnist_train.csv and sign_mnist_test.csv. Each row in the CSV file is a training sample with the 0th index having the labels from 0-25 and the rest of the row containing the 784-pixel values of a 28 x 28 image. Each pixel value will be in the range [0, 255].
"""

df = pd.read_csv('/content/drive/MyDrive/sign_mnist_train.csv')
df.head()

"""Data Loading and Preprocessing

---


The dataset has been provided in two files one is for training and the other one is for testing. We will load this data and then one hot encode the labels considering the fact we are not building the classifier for ‘J’ and ‘Z’ alphabet.
"""

def load_data(path):
	df = pd.read_csv(path)
	y = np.array([label if label < 9
				else label-1 for label in df['label']])
	df = df.drop('label', axis=1)
	x = np.array([df.iloc[i].to_numpy().reshape((28, 28))
				for i in range(len(df))]).astype(float)
	x = np.expand_dims(x, axis=3)
	y = pd.get_dummies(y).values

	return x, y

X_train, Y_train = load_data('/content/drive/MyDrive/sign_mnist_train.csv')
X_test, Y_test = load_data('/content/drive/MyDrive/sign_mnist_test.csv')

"""Now let’s check the shape of the training and the testing data."""

print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

"""Data Visualization

---


In this section, we will try to visualize images for signs of some of the alphabets which have been provided to us to build the classifier for each class.
"""

class_names = list(string.ascii_lowercase[:26].replace(
	'j', '').replace('z', ''))

plt.figure(figsize=(10, 10))
for i in range(10):
	plt.subplot(5, 5, i+1)
	plt.xticks([])
	plt.yticks([])
	plt.grid(False)
	plt.imshow(X_train[i].squeeze(), cmap=plt.cm.binary)
	plt.xlabel(class_names[np.argmax(Y_train, axis=1)[i]])
plt.tight_layout()
plt.show()

"""Model Development

---
From this step onward we will use the TensorFlow library to build our CNN model. Keras framework of the tensor flow library contains all the functionalities that one may need to define the architecture of a Convolutional Neural Network and train it on the data.

Model Architecture

We will implement a Sequential model which will contain the following parts:

*   Three Convolutional Layers followed by MaxPooling Layers.
*   The Flatten layer to flatten the output of the convolutional layer.
*   Then we will have two fully connected layers followed by the output of the flattened layer.
*   We have included some BatchNormalization layers to enable stable and fast training and a Dropout layer before the final layer to avoid any possibility of overfitting.
*   The final layer is the output layer which outputs soft probabilities for the 24 classes.


"""

model = tf.keras.models.Sequential([
	tf.keras.layers.Conv2D(filters=32,
						kernel_size=(3, 3),
						activation='relu',
						input_shape=(28, 28, 1)),
	tf.keras.layers.MaxPooling2D(2, 2),

	tf.keras.layers.Conv2D(filters=64,
						kernel_size=(3, 3),
						activation='relu'),
	tf.keras.layers.MaxPooling2D(2, 2),

	tf.keras.layers.Flatten(),
	tf.keras.layers.BatchNormalization(),
	tf.keras.layers.Dense(256, activation='relu'),
	tf.keras.layers.Dropout(0.3),
	tf.keras.layers.BatchNormalization(),
	tf.keras.layers.Dense(24, activation='softmax')
])

"""Let’s print the summary of the model’s architecture:"""

model.summary()

"""While compiling a model we provide these three essential parameters:
*   optimizer – This is the method that helps to optimize the cost function by using gradient descent.
*   loss – The loss function by which we monitor whether the model is improving with training or not.
*   metrics – This helps to evaluate the model by predicting the training and the validation data.


"""

model.compile(
	optimizer='adam',
	loss='categorical_crossentropy',
	metrics=['accuracy']
)

"""Now we will train our model:"""

from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Create an ImageDataGenerator instance for training data
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

# Create an ImageDataGenerator instance for validation data
val_datagen = ImageDataGenerator(rescale=1./255)

# Define the train generator
train_generator = train_datagen.flow(
    X_train,
    Y_train,
    batch_size=32)

# Define the validation generator
val_generator = val_datagen.flow(
    X_test,
    Y_test,
    batch_size=32)

# Now you can fit the model
history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=5,
    verbose=1)

"""Model Evaluation

Let’s visualize the training and validation accuracy with each epoch.
"""

history_df = pd.DataFrame(history.history)
history_df.loc[:,['loss','val_loss']].plot()
history_df.loc[:,['accuracy','val_accuracy']].plot()
plt.show()

model.evaluate(val_generator)

"""# Conclusion:

---


By using just a simple CNN model we are able to achieve an accuracy of 92% which is really great. This shows that this technology is certainly going to help us build some amazing applications which can be proved a really great tool for people with some special needs.
"""