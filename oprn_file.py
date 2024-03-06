with open('inputfile.txt',  encoding="utf-8") as f:
    while True:
        line = f.readline()
        if not line :
            break
        print(line)



#Methods of File Objects 

with open('inputfile.txt', encoding="utf-8") as f: 

    for line in f: 

        print(line, end='') 

 
 

with open('inputfile.txt', 'w+', encoding="utf-8") as f: 

    f.write('This is a test\n') 



