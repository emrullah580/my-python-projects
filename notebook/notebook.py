
def display_menu():
    print("--Notebook Application--")
    print("1-Add new notes")
    print("2-See notes")
    print("3-Delete notes")
    print("4-Exit")


def add_notes(notes):
    new_note = input("Enter your note here: ")
    notes.append(new_note)
    print("New note added successfully!")


def view_notes(notes):
    if notes:
        for index, note in enumerate(notes, start=1):
            print(f"{index-{note}}")
    else:
        print("There no any notes, let's add some!")

def main():
    notes = []
    display_menu()
    

