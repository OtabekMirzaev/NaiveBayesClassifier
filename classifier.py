# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:28:50 2019

@author: Otabek
"""

def Classifier(df_train, df_test):
    unique_decision = df_train.decision.unique()
    decision = []
    for i in range(len(df_test)):
#        print(df_train.iloc[i,:-1])
        prop_table = []
        for j in unique_decision:
            probability = 1
            result = df_train.query('decision=="%s"'%j)
            for b in range(len(df_test.iloc[i,:-1])):
                col_temp = result.query('col{}=="{}"'.format(b,df_test.iloc[i,b]))
                probability *= (len(col_temp)+1)/(len(result)+len(df_train["col{}".format(b)].unique()))
            
            probability *= len(result)/len(unique_decision)
            prop_table.append(probability)
#            print(str(probability)+" "+j)
        decision.append(unique_decision[prop_table.index(max(prop_table))])
#        print("==============")    
        
    return decision