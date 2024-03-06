with open('inputfile.txt',  encoding="utf-8") as f:
    while True:
        line = f.readline()
        if not line :
            break
        print(line)