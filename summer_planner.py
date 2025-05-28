class summerplanner:
    def __init__(self):
        self.activities = []

    def show_list(self):
        if len(self.activities) == 0:
            print("\nyou dont have any summer activites!!")
        else:
            print("\n summer activities:")
            for item in self.activities:
                print("- " + item)

    def add_item(self, activity):
        self.activities.append(activity)
        print('"' + activity + '" added to the list.')

    def remove_item(self, activity):
        if activity in self.activities:
            self.activities.remove(activity)
            print('"' + activity + '" removed from the list.')
        else:
            print('"' + activity + '" not found in your list.')

def show_menu():
    print("\nmenu:")
    print("1: view activities")
    print("2: add activity")
    print("3: exit")
    print("4: delete an activity")

def run():
    planner = summerplanner()
    while True:
        show_menu()
        choice = input("choose a number 1-4")

        if choice == "1":
            planner.show_list()
        elif choice == "2":
            new_activity = input("type a new activity: ")
            planner.add_item(new_activity)
        elif choice == "3":
            print("exiting!!")
            break
        elif choice == "4":
            delete_activity = input("type the activity to delete ")
            planner.remove_item(delete_activity)
        else:
            print("invalid try again.")

run()

