#from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
#from keras.models import Sequential
#from keras.optimizers import Adam
#from keras.preprocessing.image import ImageDataGenerator 


from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
import numpy as np
import pandas as pd
from tensorflow.keras.applications.resnet import ResNet50


def load_train(path):

    labels = pd.read_csv(path+'labels.csv')

    train_datagen = ImageDataGenerator(validation_split=0.25, 
                                       rescale=1./255,
                                       rotation_range=20,
                                       width_shift_range=0.2,
                                       height_shift_range=0.2,
                                       shear_range=0.2,
                                       zoom_range=0.2,
                                       horizontal_flip=True,
                                       fill_mode='nearest')
    
    train_datagen_flow = train_datagen.flow_from_dataframe(
        dataframe=labels,
        directory=path+"/final_files/",
        x_col="file_name",
        y_col="real_age",
        batch_size=16,
        seed=12345,
        class_mode="raw",
        subset='training',
        target_size=(224,224))

    return train_datagen_flow


def load_test(path):

    labels = pd.read_csv(path+'labels.csv')

    test_datagen = ImageDataGenerator(validation_split=0.25, rescale=1./255)
    test_datagen_flow = test_datagen.flow_from_dataframe(
        dataframe=labels,
        directory=path+"/final_files",
        x_col="file_name",
        y_col="real_age",
        batch_size=16,
        seed=12345,
        class_mode="raw",
        subset='validation',
        target_size=(224,224))

    return test_datagen_flow

def create_model(input_shape):
    optimizer = Adam(lr=0.0001)
    
    backbone = ResNet50(input_shape=input_shape,
                    weights='/datasets/keras_models/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5',
                    include_top=False)

    model = Sequential()
    model.add(backbone)
    model.add(GlobalAveragePooling2D())

    model.add(Dense(256, activation='relu'))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(1))

    model.compile(optimizer=optimizer, loss='mse',
                  metrics=['mae'])

    return model

def train_model(model, train_data, test_data, batch_size=None, epochs=10,
                steps_per_epoch=None, validation_steps=None):
    model.fit(train_data,
        validation_data=test_data,
        epochs=epochs,
        batch_size=batch_size,
        steps_per_epoch=steps_per_epoch,
        validation_steps=validation_steps,
        verbose=2)
    return model
