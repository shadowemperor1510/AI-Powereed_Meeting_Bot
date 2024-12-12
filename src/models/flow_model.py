import tensorflow as tf

def create_flow_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(128,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(3, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model
