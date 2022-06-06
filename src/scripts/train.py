import numpy as np
import os
from sklearn.model_selection import train_test_split
import tensorflow as tf

from model import get_model, compile_model, train_model
from pre_processor import pre_process

np_array_path = os.path.abspath("src/data/np_arrays/")

if not (
    os.path.exists(f"{np_array_path}/X.npy")
    and os.path.exists(f"{np_array_path}/y.npy")
):
    y, X = pre_process()
    X = np.array(X.iloc[:100])
    y = np.array(y.iloc[:100])
    np.save(f"src/data/np_arrays/X.npy", X)
    np.save(f"src/data/np_arrays/y.npy", y)

X = np.load(f"src/data/np_arrays/X.npy")
y = np.load(f"src/data/np_arrays/y.npy")  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 1)

model = get_model(X_train)
model = compile_model(model)
train_model(X_train, X_test, y_train, y_test, model)

loss, Y1_loss ,Y2_loss, Y3_loss, Y4_loss, Y5_loss, Y1_rmse, Y2_rmse, Y3_rmse, Y4_rmse, Y5_rmse = model.evaluate(X_test, y_test)

print() 
print(f'loss: {loss}') 
print() 
print(f'EXT_PER_loss: {Y1_loss}') 
print(f'AGR_PER_loss: {Y2_loss}') 
print(f'CSN_PER_loss: {Y3_loss}') 
print(f'EST_PER_loss: {Y4_loss}') 
print(f'OPN_PER_loss: {Y5_loss}') 
print() 
print(f'EXT_PER_rmse: {Y1_rmse}') 
print(f'AGR_PER_rmse: {Y2_rmse}')
print(f'CSN_PER_rmse: {Y3_rmse}')
print(f'EST_PER_rmse: {Y4_rmse}')
print(f'OPN_PER_rmse: {Y5_rmse}')

model.save("src/data/models/model.h5")
print("Model sucessfully trained!")
