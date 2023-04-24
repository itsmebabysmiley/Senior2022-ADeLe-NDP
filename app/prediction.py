import tensorflow as tf
import numpy as np 
import gdown
import os
binary = ['healthy','unhealthy']
multi = ['c0','c1','c2','c3','c4','c5']

class AdelePrediction:
    def __init__(self,model_name,model_path=None,model_url=None) -> None:
        
        self.model_path = model_path
        self.model_name = model_name
        self.model_path = './app/models/'
        self.model_url = model_url
        self.class_names = multi
        
        if not os.path.exists('./app/models/'):
                os.mkdir('./app/models/')
                
        # if self.model_path == None:
        #     print("[INFO] Downloading model ..... from default base model ")
        #     self.model_name = "InceptionV3.h5"
        #     print('[INFO] Download model completed')
        # elif self.model_url != None:
        #     print("[INFO] Downloading model ..... from url",self.model_url)
        #     self.download_model(url=self.model_url)
        #     print('[INFO] Download model completed')
        
        print('[INFO] Loading model.....',self.model_name)
        # if self.model_path != None:
        #     self.model = tf.keras.models.load_model(self.model_path)
        # else:
        #     path_to_load_model = os.path.join(self.model_path,self.model_name)
        #     self.model = tf.keras.models.load_model(path_to_load_model)

        self.model = tf.keras.models.load_model('./app/models/model.h5')
        self.model.load_weights('./app/models/InceptionV3-Synthesize-Multiple.h5')
        
        print('[INFO] Loading done......')
    
    
    def download_model(self, url):
        save_path_model = os.path.join(self.model_path,self.model_name)
        gdown.download(url,output=save_path_model, quiet=False, fuzzy=True)


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
        pre_class = str(self.class_names[np.argmax(score)])
        print(
            '[INFO] Prediction: {} with {:.2f}%'
            .format(self.class_names[np.argmax(score)], 100*np.max(score))
            )
        
        return {'class': pre_class, 'prob' : str(100*np.max(score)) }