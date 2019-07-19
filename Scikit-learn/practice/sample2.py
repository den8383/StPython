from sklearn import datasets
from sklearn import svm
import matplotlib.pyplot as plt
digits = datasets.load_digits()
model = svm.SVC(gamma=0.001, C=100.)
model.fit(digits.data[3:],digits.target[3:])
print(model.predict(digits.data[:3]))
print(digits.target[:3])
plt.imshow(digits.images[2],cmap=plt.cm.gray_r,interpolation='nearest')
plt.savefig('./output_digit2.png')
