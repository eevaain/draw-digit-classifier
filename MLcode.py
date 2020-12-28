from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from PIL import Image
import numpy as np
import os

digits = datasets.load_digits()
print(digits.keys())


X = digits.data
y = digits.target

print(X.shape)
print(y.shape)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1, stratify = y)

model = KNeighborsClassifier(n_neighbors = 7)

model.fit(X_train, y_train)

print('Training accuracy: ', model.score(X_train, y_train))
print('Testing accuracy: ', model.score(X_test, y_test))

#Image processing

im = np.array(Image.open('HandWrittenImages\image.png').convert('L')) #you can pass multiple arguments in single line
print(type(im))

gr_im= Image.fromarray(im).save('ConvertedHandWrittenData\converted.png')
print(type(gr_im))

load_img_rz = np.array(Image.open('ConvertedHandWrittenData\converted.png').resize((8,8)))
Image.fromarray(load_img_rz).save('FinalDownScaling\Final.jpeg')
print("After resizing:",load_img_rz.shape)

imgToArray = Image.open('FinalDownScaling\Final.jpeg')
array = np.asarray(imgToArray)
print(type(array))
print(array.shape) 
print(array) # its gonna be multi dimensional but now we need a 1d array

oneDArray = array.flatten()

print("I think that the number you drew is:", model.predict([oneDArray]))

