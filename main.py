import pandas as pd
import numpy as np
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
import streamlit as st
st.write("# Rcharge Card Classifier")
rc=pd.read_csv('rc.txt')
X=rc[['pin1', 'pin2', 'pin3', 'pin4']]
Y=rc['network']
x_train, x_test, y_train, y_test=train_test_split(X,Y, test_size=0.3)
knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train, y_train)
knn_pred=knn.predict(x_test)

#print(y_test.values, '\n', knn_pred)
#print(confusion_matrix(y_test.values, knn_pred))
#print('accuracy= ',accuracy_score(y_test.values, knn_pred)*100)
def scat(pinn):
    l=len(pinn)
    if l == 15 :
        p1,p2,p3,p4= pinn[0:5], pinn[5:10], pinn[10:],0
        if int(p1[0])==0:
            p1=int(p1[1:])
        if int(p2[0])==0:
            p2=int(p2[1:])
        if int(p3[0])==0 :
            p3=int(p3[1:])
    elif l== 16 or l==17 :
        p1,p2,p3,p4= pinn[0:4], pinn[4:8], pinn[8:12], pinn[12:]
        if int(p1[0])==0:
            p1=int(p1[1:])
        if int(p2[0])==0:
            p2=int(p2[1:])
        if int(p3[0])==0 :
            p3=int(p3[1:])
        if int(p4[0])==0 :
            p4=int(p4[1:])
    return int(p1), int(p2), int(p3), int(p4)
text=st.text_area(label='Paste The Pin Withot Spaces e.g 213434212342127')
if st.button('Submit'):
    try :
        user=text
        num1, num2, num3, num4= scat(user)
        ans = knn.predict(np.array([[num1, num2, num3, num4]]))[0]
    except :
        ans='Invalid Pin'
    st.write('## '+ans)
st.write('\n\n\n\n\n\n')
st.write('### Contact Developer : ')
st.write('[Facebook](https://www.facebook.com/profile.php?id=100005064735483)')
st.write('[Github ](https://github.com/sire-ambrose)')
st.write('[Linkedin](https://www.linkedin.com/in/ambrose-ikpele-61643419a)')