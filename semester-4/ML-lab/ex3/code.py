import tensorflow as tf
import numpy as np

X = np.array([
    [0, 0, 0],  # 0 (even)
    [0, 0, 1],  # 1 (odd)
    [0, 1, 0],  # 2 (even)
    [0, 1, 1],  # 3 (odd)
    [1, 0, 0],  # 4 (even)
    [1, 0, 1],  # 5 (odd)
    [1, 1, 0],  # 6 (even)
    [1, 1, 1]   # 7 (odd)
])
y = np.array([[0], [1], [0], [1], [0], [1], [0], [1]])

model = tf.keras.Sequential([
    tf.keras.layers.Dense(3, activation='sigmoid', input_shape=(3,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X, y, epochs=1000, verbose=0)

predictions = model.predict(X)
rounded_predictions = np.round(predictions).astype(int)
print("Predictions:", rounded_predictions)

'''
OUTPUT:

1/1 [==============================] - 0s 63ms/step
Predictions: [[0]
 [1]
 [0]
 [1]
 [0]
 [1]
 [0]
 [1]]

'''