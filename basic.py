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
        case 418:
            return "'I'm a teapot"
        case _:
            return "Something's wrong with the internet"
error_code = 404      
http_error(error_code)    


#relational operator
# Comparision between 3 number.
a = 10
b = 15
c = 20
if(a>=b and a>=c):
    print("A is greater")
elif(b>=a and b>=c):
    print("B is greater")  
else:
    print("C is greater")


# Logical Operator
skills = ["Python","ML","DL","Power BI","Azure"]

mlEngineer = ["Python","ML","DL"]
dataAnalyst = ["Python","ML","DL","Power BI"]
dataScientist = ["Python","ML","DL","Power BI","Azure"]

ajay = ["Python", "ML"]
vinayak = ["Python", "ML", "DL", "Power BI"]
aswin = ["Python", "ML", "DL", "Power BI", "Azure"]

def check_skills(person_skills, role_skills):
    return set(role_skills).issubset(set(person_skills))

def find_role(person_skills):
    if set(person_skills) == set(mlEngineer):
        if set(person_skills) == set(dataAnalyst):
            if set(person_skills) == set(dataScientist):
                return "Data Scientist"
            else:
                return "Data Analyst"
        else:
            return "ML Engineer"
    else:
        return "Not Defined"



ajay_role = find_role(ajay)
vinayak_role = find_role(vinayak)
aswin_role = find_role(aswin)

print("Ajay's role:", ajay_role)
print("Vinayak's role:", vinayak_role)
print("Aswin's role:", aswin_role)

