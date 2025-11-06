#CMPT120IntrotoProgramming
#Lab#5–WorkingwithStringsandFunctions
#Author:Tyler
#Created:2023-02-18
def username():
        first=input("Enter your first name:")
        last=input("Enter your last name:")
        uname=(first + "." + last)
        print(uname.lower())
        return uname
def password():
    passwd=input("Createanewpassword:")
    while True:
            if len(passwd)< 8:
                        print("Make sure your password is at least 8 characters long")
                        passwd = input("Create new password")
            elif passwd.lower() == passwd:
                 print("Make sure your password is has at least one uppercase")
                 passwd = input("Create new password")
            else:
                 print("the force is strong in this one…")
                 break
                

                
def main():
   user_name = username()
   password()
   print("Account configured. Your new email address is", user_name.lower()+"@marist.edu")
  
main()

 
