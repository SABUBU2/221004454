import random
number_of_friends= int(input("enter the number of friends joining(including you):\n "))
print()
if number_of_friends <=0:
    print("no one is joining for the party ")
else:
    friends={}
    print("enter the name of every friend (including you),each on a new line:")
    for num in range (number_of_friends):
        friend_name= input()
        friends[friend_name]=0
        print()
        bill =float(input("enter the total bill value:\n"))
        print()
        choice =input('do you want to use the "who is lucky?"feature write yes/no:')
        
        if choice == 'yes':
            chance= []
            for key in friends:
                chance.append(key)
                card=random.choice(chance)
                print()
                print(card,"is the lucky one!")
                print()
                bill_part = round(bill/(number_of_friends-1),2)
for friend_name in friends:
    friends[friend_name]=bill_part 
    friends.update({card:0})
    print(friends)
else:
    print()
    print("no one is going to be lucky\n")
    bill_part = round(bill/number_of_friends,2)
    for friend_name in friends:
        friends[friend_name] =bill_part
        print(friends)               
