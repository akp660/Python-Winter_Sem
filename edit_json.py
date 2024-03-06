students = { 

  'Student 1': { 

        'Name': "Alice", 'Age' :10, 'Grade':4, 

    }, 

    'Student 2': { 

        'Name':'Bob', 'Age':11, 'Grade':5 

    }, 

    'Student 3': { 

        'Name':'Elena', 'Age':14, 'Grade':8 

    } 

} 

 
 

type(students) 

 
 
 

with open('student_info.txt','w') as data: 

      data.write(str(students)) 

 
 

with open("student_info.txt", 'r') as f: 

    for students in f: 

        print(students) 

 
 

type(students) 