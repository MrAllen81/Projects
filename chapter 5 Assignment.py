#This program will give the date in proper format
#Tyler Allen
#10/6/23

def date():
    today = input("Enter the todays date in mm/dd/yyyy format")
    x, y, z = map(int, today.split('/'))

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    x = months[x-1]
    print("The date selected is", str(x),str(y)+","+str(z))

date()
                  
