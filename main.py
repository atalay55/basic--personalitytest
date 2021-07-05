import Question
import User

f2 = open("output.txt","w")

user1= User.User(None,None,None,None,None,None)

def is_digit(check_input):
    if check_input.isdigit():
        return True
    return False

#name must be string
name=input("please enter your name:  ")
if(is_digit(name)== False):
    user1.set_name(name)
else:
    print("please enter strings arguments")
    raise TypeError("Only strings are allowed")

# surname must be string
surname=input("please enter your surname: ")
if(is_digit(surname)== False):
    user1.set_surname(surname)
else:
    print("please enter strings arguments")
    raise TypeError("Only strings are allowed")

# age must be integer
age=input("please enter your age: ")
if(is_digit(age)):
    user1.set_age(age)
else:
    print("please enter integar arguments")
    raise TypeError("Only integar are allowed")

# gander must be string
gander = input("please enter your gender: W or M : ") 
if(is_digit(gander)== False):
    if(gander in ("W","w","M","m","Woman","Man","woman","man")):
        user1.set_gender(gander)
    else:
         raise ValueError("please check your input")
else:
    print("please enter strings arguments")
    raise TypeError("Only integar are allowed")

# personelNumber must be integar and its must be 11 digit
personelNumber= input("please enter personelNumber: ")
if(is_digit(personelNumber)):
    if(len(personelNumber)==11):
        user1.set_personelNumbers(personelNumber)
    else:
        raise ValueError("personel number lenght must be eleven parts")
            
else:
    print("please enter strings arguments")
    raise TypeError("Only strings are allowed")
    





question1 =Question.Question("Do you usually take energy from other people, easily communicate with the environment, like to be social, think broadly, be lively and talkative?")
question2 =Question.Question("Are perception in the literal sense, going step by step with precise knowledge, details, reality, concrete thinking, experiences, practicality important to you?")
question3 =Question.Question("Are you a person with compassion, appreciation and understanding, who behaves according to personal perspective and values with the ability of compatibility in your relations with people?")
question4 =Question.Question("Open-minded, changeable as you progress, behaving naturally without thinking, flexible, thoughtful, relaxed, adaptable, acting according to the moment and mood. Can you say that these features show me exactly?")

questions=[question1,question2,question3,question4]

for i in questions:
    if( i== question1):
        print(question1.get_question())
        answer1 = input("yes or  no :")
        if(str(answer1) in ("yes", "yep", "ye","y")):
            question1.set_answer(True)
            user1.set_status("Extravert/")
        elif(str(answer1) in ("no", "nope", "n")):
            question1.set_answer(False)
            user1.set_status("Introvert/")
        else:
            print("check your words")
            break
          
           
    elif(i == question2):
        print(question2.get_question())
        answer2 = input("yes or  no : ")
        if((answer2) in ("yes", "yep", "ye","y")):
            question2.set_answer(True)
            user1.set_status("Sensing/ ")
       
        elif(str(answer2) in ("no", "nope", "n")):

            question1.set_answer(False)
            user1.set_status("iNtuition/  ")

        else:
            print("check your words")
            break

    elif(i == question3):
        print(question3.get_question())
        answer3 =  input("yes or  no : ")
        if((answer3) in ("yes", "yep", "ye","y")):
            question3.set_answer(True)
            user1.set_status("Feeling/ ")
           

        elif(str(answer3) in ("no", "nope", "n")): 
            question3.set_answer(False)
            user1.set_status("Thinking/  ")
              

        else:
            print("check your words")
            break

            
    elif(i== question4):
        print(question4.get_question())
        answer4 =  input("yes or  no: ")
        if((answer4) in ("yes", "yep", "ye","y")):
            question4.set_answer(True)
            user1.set_status("Perceiving")
           
        
        elif(str(answer4) in ("no", "nope", "n")): 
            question4.set_answer(False)
            user1.set_status("Judging")
        

        else:
            print("check your words")   
            break


point = input("please enter your point (1,10): ")

if(is_digit(point)):
    point=int(point)
    if(0<=point and point<=10):
        user1.set_point(point)
    else:
        raise ValueError("your point must be between 1 and 10")
            
else:
    print("please enter integer arguments")
    raise TypeError("Only integar are allowed")
    



userList=[]

userList.append(user1.get_name()+ " " +user1.get_surname()+",")
userList.append(user1.get_age()+",")
userList.append(user1.get_gender()+",")
userList.append(user1.get_personelNumbers()+",")
userList.append(user1.get_point())



def yazdır():

    for i in userList:
        
        f2.write(str(i))
    
    print("Name :",user1.get_name(),"Surname: ",user1.get_surname(),"Age: ",user1.get_age(),"Gander: ",user1.get_gender(),"Point :",user1.get_point())
    
    f2.write("\n")
    for i in user1.get_status():
        f2.write(str(i))
        print(i)
    f2.close()






yazdır()