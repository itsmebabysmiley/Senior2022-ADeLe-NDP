import tensorflow as tf
import numpy as np 
import gdown
import os

class_names = ['healthy', 'unhealthy']

class AdelePrediction:
    def __init__(self,model=None) -> None:
        
        self.model_path = './app/models/InceptionV3.h5'
        self.model = model
        
        if self.model == None:
            if not os.path.exists(self.model_path):
                print("[INFO] Downloading InceptionV3.h5 .....")
                self.download_model(url="https://drive.google.com/file/d/1-8EgaAi6KLHUt31n-OQCA5Z5GjyxI1wH/view?usp=sharing")
                print('[INFO] Download completed')
        
        print('[INFO] Loading model.....')
        self.model = tf.keras.models.load_model(self.model_path)
        print('[INFO] Loading done......')
    
    
    def download_model(self, url):
        gdown.download(url, self.model_path, quiet=False, fuzzy=True)


    def prediction(self,image_path):
        """Just my prediction function

        Args:
            image_path (str): path to your image.

        Returns:
            dict: including class and prob.
        """
        img = tf.keras.utils.load_img(image_path, target_size=(229,229))
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        
        predictions = self.model.predict(img_array)
        score = tf.nn.softmax(predictions[0])
        print(
            '[INFO] Prediction: {} with {:.2f}%'
            .format(class_names[np.argmax(score)], 100*np.max(score))
            )
        
        return {'class': str(class_names[np.argmax(score)]), 'prob' : str(100*np.max(score)) }