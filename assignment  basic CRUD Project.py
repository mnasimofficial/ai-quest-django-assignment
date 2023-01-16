#CRUD PROJECT:

bd_cricket_team = ["Sakib","Tamim","Mash","Musfiq","Riyad","Fizz","Mirazz","Summo","Liton","Taskin","Rubel"]
while True:
    user_command = input("What You Want? (view/add/remove/change)Player or exit: ")
    if user_command == "exit":
        print("You are Sucessfully Exit this Programe()")
        break

    elif user_command == "view":
        print("Thank You! This is Your Team",bd_cricket_team)

    elif user_command == "add":
        bd_cricket_team.append(input("Add Your New Team Member: "))
        print("New Team Member list",bd_cricket_team)

    elif user_command == "remove":
        remove_item = input("Which Player Do You Want to Remove: ")
        if remove_item in bd_cricket_team:
            bd_cricket_team.remove(remove_item)
            print("New List After Player Removed",bd_cricket_team)
        else:
            print("This Player Dosen't Exist in this Team. Sorry!")

    elif user_command == "change":
        wrong_player = input("Which Player Do You Want to Change?: ")
        right_player = input("Enter the New Player Name: ")
        if wrong_player in bd_cricket_team:
            w_p_i = bd_cricket_team.index(wrong_player)
            bd_cricket_team[w_p_i] = right_player
            print("New Team After Exchange", bd_cricket_team)
        else:
            print("Sorry to Say that,We can't find your exchange Player.")

    else:
        print("Enter Valid Value Please")
