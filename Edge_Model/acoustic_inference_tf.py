
import json
import numpy as np
from tensorflow import keras
import soundfile as sf
import sys
import os

if __name__ == "__main__":

    # hides tensorflow message logs
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

    # reads file
    file, _ = sf.read(sys.argv[1])

    # pre-process file for prediction
    x = []
    x.append(file)

    x = np.array(x) 

    if len(x.shape) == 2:

        x = np.reshape(x, (x.shape[0],x.shape[1],1))

    x = x.astype(np.float16)
    
    # load models
    models = []
    for i in range(4):
        # path is what team model used to store models. NOTE FOR EDGE TEAM: YOU CAN CHANGE PATH based on location on edge device just make sure
        # model naming convention is ../../../temp{i} i: 0-3
        models.append(keras.models.load_model(f'./gryphon_group_data/collection_2_2022/models/temp{i}'))

    # dict of dict to help map prediction label to index of max value from prediction tensor
    label_maps = {  
        0: {0: '0', 1: '30', 2: '60', 3: '90', 4: '120', 5: '150', 6: '180'},
        1: {0: '20', 1: '50', 2: '100', 3: '175', 4: '250'},
        2: {0: 'pistol', 1: 'rifle'},
        3: {0: '45', 1: '90', 2: '135', 3: '180', 4: '225', 5: '270', 6: '315', 7: '360'}
    }
    
    # getting prediction from each model
    predictions = []
    for i in range(4):

        # returns list 
        prediction = models[i].predict(x, verbose=0)

        # max value in list is the prediction, get its index
        max_index = np.argmax(prediction[0])

        # adding to predictions list, i = getting current model dict, max_index is the current model key to get prediction value
        predictions.append(label_maps.get(i).get(max_index))
    
    # putting everything in a dict
    predictions = {
        'Angle': predictions[0],
        'Distance': predictions[1],
        'Weapon': predictions[2],
        'Azimuth': predictions[3]
    }

    # json dumps for edge
    sys.stdout.write(json.dumps(predictions))


 

