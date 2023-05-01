from firebase import firebase

firebase = firebase.FirebaseApplication('https://smart-bus-26302-default-rtdb.firebaseio.com/', None)



def realtime():
    result = firebase.put('/output', 'gps' , 1)
    print(result)
    return result





