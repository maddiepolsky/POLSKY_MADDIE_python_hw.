#so im not really sure what to do with this
#i was kind of jsut copy and pasting

#i attempted to understand it though

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
import seaborn as sns #chatgpt said i needed to have this for it to work but its not oworking

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/drug200.csv'
my_data = pd.read_csv("drug200.csv", delimiter=",")
my_data[0:5]
#what code am i supposed to write here?

my_data.shape

X = my_data[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']].values
X[0:5]

#did not get an array as the output

from sklearn import preprocessing
le_sex = preprocessing.LabelEncoder()
le_sex.fit(['F','M'])
X[:,1] = le_sex.transform(X[:,1]) 


le_BP = preprocessing.LabelEncoder()
le_BP.fit([ 'LOW', 'NORMAL', 'HIGH'])
X[:,2] = le_BP.transform(X[:,2])


le_Chol = preprocessing.LabelEncoder()
le_Chol.fit([ 'NORMAL', 'HIGH'])
X[:,3] = le_Chol.transform(X[:,3]) 

X[0:5]

y = my_data["Drug"]
y[0:5]

from sklearn.model_selection import train_test_split

X_trainset, X_testset, y_trainset, y_testset = train_test_split(X, y, test_size=0.3, random_state=3)

print("X_trainsetX SHAPE:  " + str(X_trainset.shape))
print("y_trainsetX SHAPE:  " + str(y_trainset.shape))

print("X_testsetX SHAPE:  " + str(X_testset.shape))
print("y_testsetX SHAPE:  " + str(y_testset.shape))

drugTree = DecisionTreeClassifier(criterion="entropy", max_depth = 4)
drugTree

drugTree.fit(X_trainset,y_trainset)

predTree = drugTree.predict(X_testset)


print (predTree [0:5])
print (y_testset [0:5])


from sklearn import metrics
import matplotlib.pyplot as plt
print("DecisionTrees's Accuracy: ", metrics.accuracy_score(y_testset, predTree))

!conda install -c conda-forge pydotplus -y
!conda install -c conda-forge python-graphviz -y

from  io import StringIO
import pydotplus
import matplotlib.image as mpimg
from sklearn import tree
%matplotlib inline 

dot_data = StringIO()
filename = "drugtree.png"
featureNames = my_data.columns[0:5]
out=tree.export_graphviz(drugTree,feature_names=featureNames, out_file=dot_data, class_names= np.unique(y_trainset), filled=True,  special_characters=True,rotate=False)  
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png(filename)
img = mpimg.imread(filename)
plt.figure(figsize=(100, 200))
plt.imshow(img,interpolation='nearest')
