import tensorflow as tf
import numpy as np 

model_path = './app/models/InceptionV3.h5'
class_names = ['healthy', 'unhealthy']

def load_my_model():
    model = tf.keras.models.load_model(model_path)
    return model

def prediction(image_path):
    """Just my prediction function

    Args:
        image_path (str): path to your image.

    Returns:
        dict: including class and prob.
    """
    img = tf.keras.utils.load_img(image_path, target_size=(229,229))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    print('[INFO] Loading model.....')
    model = load_my_model()
    print('[INFO] Predicting........')
    
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    print(
        '[INFO] Prediction: {} with {:.2f}%'
        .format(class_names[np.argmax(score)], 100*np.max(score))
        )
    
    return {'class': str(class_names[np.argmax(score)]), 'prob' : str(100*np.max(score)) }