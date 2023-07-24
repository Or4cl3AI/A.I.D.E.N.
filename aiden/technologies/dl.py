```python
import tensorflow as tf
from tensorflow import keras

class DL:
    def __init__(self):
        self.model = None

    def create_model(self, input_shape, output_shape):
        self.model = keras.Sequential([
            keras.layers.Dense(128, activation='relu', input_shape=input_shape),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(output_shape, activation='softmax')
        ])

        self.model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

    def train_model(self, train_data, train_labels, epochs=5):
        if self.model is None:
            raise Exception("Model not created. Call create_model first.")
        self.model.fit(train_data, train_labels, epochs=epochs)

    def predict(self, data):
        if self.model is None:
            raise Exception("Model not created. Call create_model first.")
        return self.model.predict(data)

    def save_model(self, filepath):
        if self.model is None:
            raise Exception("Model not created. Call create_model first.")
        self.model.save(filepath)

    def load_model(self, filepath):
        self.model = keras.models.load_model(filepath)
```