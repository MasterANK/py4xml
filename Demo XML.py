import py4xml

def test_main():
    inp = int(input("""Enter 1 to show all record
Enter 2 to search for a record by element
Enter 3 to check if a record is present in the file

Enetr Choice: """))
    if inp == 1:
        read_all()
    elif inp == 2:
        element_search()
    elif inp == 3:
        check_element()


def open_xml():
    f = open("Tests/XML 2.xml","r")
    data = py4xml.read_xml(f)
    return data

def read_all():
    file = open_xml()
    data = file.main_dict
    for i in data:
        print(i)
        for j in data[i]:
            print("     ",j,":",data[i][j])

def element_search():
    var = input("\nEnter Element: ")
    file = open_xml()
    data = file.find_element(var)
    print(var+"-")
    for i in data:
        print("  ",i,":",data[i])

def check_element():
    var = input("\nEnter Element: ")
    file = open_xml()
    data = file.element_stack
    flag = False
    if var in data:
        flag = True
        print("The element is present in the XML file")
    if not flag:
        print("Element is not present in the XML file")


if __name__ == "__main__":
    test_main()