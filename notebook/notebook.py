notes=[]
def display_menu():
    print("--Notebook Application--")
    print("1-Add new notes")
    print("2-See notes")
    print("3-Delete notes")
    print("4-Exit")
    
def New_Notes():
    new_notes=input("Add new notes: ")
    notes.append(new_notes)

