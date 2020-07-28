Names = ['sabhyata','sanskruti','sonu','sabhyata','sabhyata','sanskruti','sonu']
while True:
    print("press 1 for sabhyata")
    print("press 2 for sanskruti")
    print("press 3 for sonu")
    print("press 4 for exit")
    choice = input()
    n=input()
    Names_count = Names.count(n)

    if choice =='1':
        print("the name available is", Names.count("sabhyata"))
    elif choice =='2':
        print("the name available is", Names.count("sanskruti"))
    elif choice =='3':
        print("the name available is", Names.count("sonu"))
    else:
        print("please enter valid number")



