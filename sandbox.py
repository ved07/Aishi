import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical


dataset = pd.read_csv("data.csv")
y_val = dataset["Disease"].tolist()
def one_hot_encode(y_to_enc):
    check_arr = []
    encode_val_arr = []
    return_arr = []
    for i in range(0,len(y_to_enc)):
        if(y_to_enc[i] in check_arr):
            return_arr.append(encode_val_arr[check_arr.index(y_to_enc[i])])
        else:
            check_arr.append(y_to_enc[i])
            one_hot = [0]*len(y_to_enc)
            one_hot[i] = 1
            encode_val_arr.append(one_hot)
            return_arr.append(one_hot)
    return return_arr



dataset = dataset.drop(columns=["Disease"])
x_val = []
for row in dataset.index:
    l = len(dataset.loc[row].tolist())
    x_val.append(dataset.loc[row].tolist())
feature_vector_length = 184
x_val = tf.convert_to_tensor(
    x_val, dtype=tf.float32, dtype_hint=None, name=None
)
y_val = tf.convert_to_tensor(
    y_val, dtype_hint=None, name=None,
)
x_val= tf.reshape(x_val,shape=[29,184])
print(y_val)
model= Sequential([Dense(184,input_shape=[184,], activation="relu", name="layer1")])
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
def fit():
    model.fit(x=x_val,y= y_val, epochs=10, batch_size=29)

fit()