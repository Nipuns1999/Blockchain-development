
import json
import datetime


def inputFloat(prompt):

    while True:
        try:
            user = float(input(prompt))
            break

        except:
            print('Invalid input')
            continue
    return user



def savedata(file):
    f = open('data.txt', 'w')
    json.dump(file, f, indent=4)
    f.close()




#transaction recordimg program
try:
    f = open('data.txt', 'r')
    data = json.load(f)
    f.close()
except:
    data = []

while True:

        name = str(input("Do you want to make a new transaction (Type YES to continue and type NO to exist)\n: ")).lower()
        if name == "yes":
            name = {}
            user1 = str(input("From (username of the sender): ").lower())
            name['From'] = user1
            user2 = str(input("To (username of the receiver): ").lower())
            name['To'] = user2
            user3 = inputFloat("Enter the amount: ")
            name['Amount'] = user3
            user4 = str(datetime.datetime.today())
            name["Timestamp"] = user4
            data.append(name)
            savedata(data)
            continue

        elif name == "no":
            print("You have successfully exited the program")
            break
        else:
            print("Incorrect Input!.Please Try again")
            continue
exit()


