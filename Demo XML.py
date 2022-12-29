'''
Note:- If you have pip installed the py4xml, Then change the import statement to "import py4xml"
Else if you have forked it from github then leave the import statement or change it accordingly with the py4xml.py file path
'''
try:
    import py4xml
except :
    import src.py4xml.py4xml as py4xml

def test_main():
    inp = int(input("""Enter 1 to show all record.
Enter 2 to search for a record by element.
Enter 3 to check if a record is present in the file.
Enter 4 to extend data in the xml file.
Enter 5 to convert csv to xml file.
Enter 6 to convert xml to csv file.

Enetr Choice: """))
    if inp == 1:
        read_all()
    elif inp == 2:
        element_search()
    elif inp == 3:
        check_element()
    elif inp == 4:
        extend_file()
    elif inp == 5:
        convert_csv_xml() 
    elif inp == 6:
        convert_xml_csv()


def open_xml():
    f = open("Tests\XML 2.xml","r")
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

def extend_file():
    data = {"Arceus":{"HP":100,"Defence":100,"Speed":100},
    "Gratina":{"HP":99,"Defence":99,"Speed":99}}

    write_f = open("Tests\XML 2.xml","r+")
    py4xml.extend_xml(data,write_f)
    
    write_f.close()


def convert_csv_xml():
    csv_f = open("Tests\csv 1.csv","r")  #input("Enter CSV File path: ")
    xml_f = open("Tests\XML 4.xml","w")  #input("Enter XMl file path: ")
    root_element = "Student_Data"        #input("Enter Root_Element: ")
    key = "name"                         #input("Enter Key: ")
    py4xml.csv_to_xml(root_element,csv_f,key,xml_f)

    csv_f.close(); xml_f.close()

def convert_xml_csv():
    csv_f = open("Tests\csv 1.csv","w",newline="")  #input("Enter CSV File path: ")
    xml_f = open("Tests\XML 4.xml","r")             #input("Enter XMl file path: ")
    elementcol = "name"                             #input("Enter Element Column Name: ")

    py4xml.xml_to_csv(xml_f,csv_f,elementcol)

    csv_f.close(); xml_f.close()

if __name__ == "__main__":
    test_main()