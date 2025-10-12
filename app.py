Monday = True
Tuesday = True
Wednesday = True
Thursday = True
Friday = False


def checkgym(day):
    if day:
        print("You have gym today")
    else:
        print("rest day")

checkgym(Friday)

