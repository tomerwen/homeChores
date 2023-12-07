listOfChores={
    "Dusting study",
    "Organizing study",
    "Empty garbage cans",
    "Put shoes back in place",
    "Clean Fridge",
    "Clean Coffee machine",
    "Clean air fryer",
    "Clean Tami4",
    "Clean stove",
    "Clean kitchen table",
    "Wipe cabinet exterior",
    "Clean cabinet interior",
    "Clean oven",
    "Scrub kitchen surfaces",
    "Declutter dining table",
    "Wipe brown consule",
    "Wipe dining table",
    "Wipe tv console",
    "Clean living room tables",
    "Organize couch",
    "Dust liquer cabinet",
    "Fold laundry",
    "Clean mirrors",
    "Clean guest toilet",
    "Clean guest bathroom sink",
    "Clean guest bathroom shower",
    "Clean makeup table",
    "Clean bedside tables",
    "Clean dryer and washing machine exterior",
    "Scrub kitchen floor",
    "Scrub entrance floor",
    "Clean bedroom toilet",
    "Clean bedroom sink",
    "Clean bedroom shower",
    "Setup environment and activate herbert",
    "Clean balcony fridge exterior",
    "Clean study window",
    "Clean kitchen window",
    "Clean living room window",
    "Clean guestroom window",
    "Clean bedroom window",
    "Clean bedroom bathroom window"
}
activeList={}

def fillTasks():
    global activeList
    if not activeList:
        activeList = listOfChores.copy()

def main():
    fillTasks()

    print("=== List of Chores ===")
    for chore in listOfChores:
        print(chore)

    print("\n=== Active List ===")
    for active_chore in activeList:
        print(active_chore)

if __name__ == "__main__":
    main()