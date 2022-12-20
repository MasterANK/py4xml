import re
from xml_rectifier import Closing_Error

class xml_reader:
    def __init__(self,name):
        self.root_element = name

def main():
    with open("XML 1.xml","r") as f:
        readit(f)

def readit(f):
    data = f.readlines()

    for i in data:
        if a := re.fullmatch(r"<(\w+)>",i.strip("\n")):
            header_flag = False
            xml_file = xml_reader(a.group(1))
            
        elif a := re.fullmatch(r"</(\w+)>",i.strip("\n")):
            header_flag = True


    if not header_flag:
        raise Closing_Error("Header is not closed")

    print(xml_file.root_element)

if __name__ == "__main__":
    main()
