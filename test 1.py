import main

def test_main():
    inp = int(input("""Enter 1 to show all record
Enter 2 to search for a record by element
Enter 3 to search for a record by sub elements

Enetr Choice: """))
    if inp == 1:
        read_all()
    elif inp == 2:
        element_search()
    elif inp == 3:
        pass

def open_xml():
    f = open("XML 1.xml","r")
    data = main.read_xml(f)
    return data

def read_all():
    file = open_xml()
    data = file.main_dict
    for i in data:
        print(i)
        for j in data[i]:
            print("     ",j,":",data[i][j])

def element_search():
    file = open_xml()
    data = file.main_dict
    var = input("Enter Element: ")
    for i in data:
        if var == i:
            print("Data for",var)
            for j in data[i]:
                print("     ",j,":",data[i][j])

if __name__ == "__main__":
    test_main()