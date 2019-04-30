#How to make a password controlled dictionary

mydict = {
        "hello":"world",
        "password1":"frankie",
        "password2":"Bobby",
        "password3":"gertrude",
        "password4":"berlin",
        "password5":"germany"
        }

#Now, this is the password controller. But before we do anything, we need to make sure the password the user enters is the same one we want. For added "security" we can even
#make our .py file a hidden file so these dictionaries are not accessible!

controller_password = "nutella" #that's what I was eating when I was making this
input_list = input("Enter password to see all passwords-->  ") 

if input_list == controller_password:
	print(mydict)
	
else:
	print("Wrong password. Close the window and try again.")