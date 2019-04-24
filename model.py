import pandas as pd
from classifier import Classifier

df_train = pd.read_csv('train', header=None)
df_test = pd.read_csv('test', header=None)
df_train.columns = ['col0','col1','col2','col3','col4','col5','decision']
df_test.columns = ['col0','col1','col2','col3','col4','col5','decision']
labels = Classifier(df_train, df_test)

d_labels=list(df_test['decision'])
correct = 0
for i in range(len(labels)):
    if labels[i] == d_labels[i]:
        correct += 1

accuracy = correct/len(labels)