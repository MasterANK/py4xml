import main

f = open("XML 1.xml","r")
data = main.read_xml(f)
print(data.main_dict)