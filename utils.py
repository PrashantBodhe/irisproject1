import pickle
import os
import config

model_folder_path = config.MODEL_FOLDER_PATH

if not os.path.exists(model_folder_path):
    os.mkdir(model_folder_path)


def predict_class(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm):

    clf_model = pickle.load(open(f'{model_folder_path}/model.pkl', 'rb'))
    print('clf_model:', clf_model)

    prediction = clf_model.predict([[SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]])
    print('Predicted class is:',prediction[0])
    pred = prediction[0]
    return pred

