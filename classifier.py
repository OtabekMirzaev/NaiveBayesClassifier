

def Classifier(df_train, df_test):
    unique_decision = df_train.decision.unique()
    decision = []
    for i in range(len(df_test)):
        prop_table = []
        for j in unique_decision:
            probability = 1
            result = df_train.query('decision=="%s"'%j)
            for b in range(len(df_test.iloc[i,:-1])):
                col_temp = result.query('col{}=="{}"'.format(b,df_test.iloc[i,b]))
                probability *= (len(col_temp)+1)/(len(result)+len(df_train["col{}".format(b)].unique()))
            
            probability *= len(result)/len(unique_decision)
            prop_table.append(probability)
        decision.append(unique_decision[prop_table.index(max(prop_table))])   
        
    return decision
