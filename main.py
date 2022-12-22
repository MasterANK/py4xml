import re
from xml_rectifier import *

class xml_reader:
    def __init__(self,name = None):
        self.root_element = name
        self.element_stack = []                             #Stack which contains name of Elements
        self.main_dict = {}                                 #Nested dict with element->{Sub_element}


    def element_stacker(self,name):
        self.element_stack.append(name)
    
    def add_dict(self,element):                             #test change
        self.main_dict[element] = {}


def main():
    with open("XML 1.xml","r") as f:
        readit(f)

def readit(f):
    data = f.readlines()
    xml_file = xml_reader()
    print(data)

    for i in data:
        if a := re.fullmatch(r"<(\w+)>",i.strip("\n")):         #Init Header Check
            header_flag = False
            xml_file.root_element = a.group(1)

        elif a := re.fullmatch(r"<(\w+)>",i.strip()):           #Element Check
            print("Flag raised")
            if header_flag != False:
                raise XML_Definition_Error("Root Element not defined")
            element_flag = False
            element = a.group(1)
            xml_file.element_stacker(element)
            xml_file.add_dict(element)

        
        elif a := re.fullmatch(r"</(\w+)>",i.strip()):          #Closing Root_Element,Element Check
            print("flag Down")
            print(a.group(1),element)
            if a.group(1) == xml_file.root_element:
                header_flag = True
            if a.group(1) == element:
                element_flag = True 


    if not header_flag:
        raise XML_Syntax_Error(xml_file.root_element + " is not closed properly")
    if not element_flag:
        raise XML_Syntax_Error(element + " is not closed properly")
    print(xml_file.root_element)
    print(xml_file.element_stack)

if __name__ == "__main__":
    main()