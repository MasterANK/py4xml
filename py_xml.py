import re
import csv

class XML_Syntax_Error(Exception):
    pass

class XML_Definition_Error(Exception):
    pass

class xml_reader:
    def __init__(self,name = "Root Element"):
        self.root_element = name                            #Name of the root element
        self.element_stack = []                             #Stack which contains name of Elements
        self.main_dict = {}                                 #Nested dict with element->{Sub_element}


    def element_stacker(self,name):                         #A list of all the elements present 
        self.element_stack.append(name)
    
    def add_dict(self,element):                             #Nested Dictionary as Element -> {Sub_elements}
        self.main_dict[element] = {}

    def add_disct_value(self,element,key,value):            #Adding Values to the nested dictionary
        self.main_dict[element][key] = value


def main():
    dic = {"Pika" : {"HP": 100,"Defence" : 50,"Speed": 80 }, "Snorlax":{"HP":100,"Defence":100,"Speed": 0} }
    with open("Tests/XML 2.xml","w") as f:
        dict_write_xml("cards",dic,f)


def read_xml(f):
    data = f.readlines()
    xml_file = xml_reader()
    element_flag = True

    for i in data:
        if a := re.fullmatch(r"<(\w+)>",i.strip("\n")):         #Init Header Check
            header_flag = False
            xml_file.root_element = a.group(1)

        elif a := re.fullmatch(r"<(\w+)>",i.strip()):           #Element Check
            if header_flag != False:
                raise XML_Definition_Error("Root Element not defined")

            if element_flag:                                    #To resolve the Bug where tag closing error never occurs
                element_flag = False
            else:
                raise XML_Syntax_Error(element+" is not closed properly")

            element = a.group(1)
            xml_file.element_stacker(element)
            xml_file.add_dict(element)

        elif a:= re.fullmatch(r"<(\w+)>([^<>]+)</(\w+)>",i.strip()):        #Sub_elements Check + Closing
            if a.group(1) != a.group(3):
                raise XML_Syntax_Error(a.group(1)+" is not closed properly")
            xml_file.add_disct_value(element,a.group(1),a.group(2))
        
        elif a := re.fullmatch(r"</(\w+)>",i.strip()):          #Closing Root_Element,Element Check
            if a.group(1) == xml_file.root_element:
                header_flag = True
            if a.group(1) == element:
                element_flag = True 


    if not header_flag:
        raise XML_Syntax_Error(xml_file.root_element + " is not closed properly")
    if not element_flag:
        raise XML_Syntax_Error(element + " is not closed properly")
    
    return xml_file


def dict_write_xml(root_element ,data : dict,  write_f : object):
    write_f.write("<"+str(root_element)+">\n")
    for i in data:
        write_f.write("  <"+str(i)+">\n")
        element_flag = False
        for j in data[i]:
            exp = "    <"+str(j)+">"+str(data[i][j])+"</"+str(j)+">\n"
            write_f.write(exp)
        else:
            if element_flag == False:
                element_flag == True
                write_f.write("  </"+str(i)+">\n")
    else:
        write_f.write("</"+str(root_element)+">\n")


if __name__ == "__main__":
    main()