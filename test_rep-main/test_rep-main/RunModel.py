import joblib
from bait_extract import feat_ex
import numpy as np

# the first value will give the class/label , the second one will be the a pair of values with 1st value of the list is non-virus probability and the 2nd value is the virus probability

def predicto(s):
    xy=joblib.load("column_names.pkl")
    print(xy)


    maha_dicto=feat_ex(s)

    my_model=joblib.load("first_model.pkl")
    feats=[]

    for i in xy:
        try:
            feats.append(maha_dicto[i])
        except:
            pass

    probs=my_model.predict_proba(np.array([feats]))

    maino=[]
    maino.append(my_model.predict(np.array([feats])))
    maino.append(probs)
    return maino

