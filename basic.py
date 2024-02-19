a = 33
b = 11
if b>a:
    #print ("I am here")
    pass
else:
    print("Hello")

#the pass keyword can be used in empty function
    



#http error code
def http_error(status):
    match status:
        case 400:
            return "Bad Network"
        case 401 | 403:
            return "Not allowed"
        case 404:
            return "Not Found"