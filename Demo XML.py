import py4xml

def test_main():
    inp = int(input("""Enter 1 to show all record
Enter 2 to search for a record by element
Enter 3 to check if a record is present in the file
Enter 4 to convert csv to xml file.

Enetr Choice: """))
    if inp == 1:
        read_all()
    elif inp == 2:
        element_search()
    elif inp == 3:
        check_element()
    elif inp == 4:
        convert_csv_xml() 


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


def convert_csv_xml():
    csv_f = open("Tests\csv 1.csv","r")  #input("Enter CSV File path: ")
    xml_f = open("Tests\XML 4.xml","w")  #input("Enter XMl file path: ")
    root_element = "Student_Data"        #input("Enter Root_Element: ")
    key = "name"                         #input("Enter Key: ")
    py4xml.csv_to_xml(root_element,csv_f,key,xml_f)

if __name__ == "__main__":
    test_main()