import json 

my_list = ["this","is","a","simple","list",96] 

with open("storage.txt", "w") as fs: 

    my_json_object = json.dump(my_list, fs) 

with open("storage.txt", "r") as fds: 

    my_second_list = json.load(fds) 

print(my_second_list) 