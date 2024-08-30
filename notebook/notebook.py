
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


def main():
    notes = []
    display_menu()
    add_notes(notes)