from firebase import firebase

firebase = firebase.FirebaseApplication('https://smart-bus-26302-default-rtdb.firebaseio.com/', None)



def realtime():
    result = firebase.put('/output', 'gps' , 1)
    print(result)
    return result




def get_gsp_lat():
    result = firebase.get('/output/lat' , '')
    #print(result)
    return result


def get_gsp_long():
    result = firebase.get('/output/long' , '')
    #print(result)
    return result
