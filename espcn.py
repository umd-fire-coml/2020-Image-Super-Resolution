import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, Model

# 6-layer ESPCN SISR model
def espcn_model(r, channels = 3):
    # Arguments for Conv2D
    conv_args = {
      "activation": "relu",
      "padding" : "same",
    }
    # Input
    inputs = keras.Input(shape=(None, None, channels))
    # Feature Maps Extraction
    conv1 = layers.Conv2D(64, 5, **conv_args)(inputs)
    conv2 = layers.Conv2D(64, 3, **conv_args)(conv1)
    conv3 = layers.Conv2D(32, 3, **conv_args)(conv2)
    conv4 = layers.Conv2D(32, 3, **conv_args)(conv3)
    conv5 = layers.Conv2D(32, 3, **conv_args)(conv4)
    conv6 = layers.Conv2D(channels*(r*r), 3, **conv_args)(conv5)
    # Efficient Sub-Pixel Convolutional Layer
    outputs = tf.nn.depth_to_space(conv6, r)
    return Model(inputs, outputs)