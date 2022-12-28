
# **Py4XML**
**Under-Construction*
### Author: Ankit Aggarwal (@MasterANK)
### Language Used : Python
### Github Link : [Py4XML Github](https://github.com/MasterANK/py4xml/tree/main)
#
# ***Introduction to XML***
XML stands for extensible markdown language, An XML file is a file which is used to store data in both computer and human readable. XML is a markup language much like HTML but was designed to store data, transport data and was designed to be self-descriptive. XML is a World Wide Web Consortium (W3C) recommendation while World Wide Web Consortium (W3C) is an organization whose mission is to lead the World Wide Web to its full potential by developing protocols and guidelines that ensure the long-term growth of the Web.

## Features XML File
+ XML Does Not Use Predefined Tags
+ XML was designed to carry data - with focus on what data is
+ XML is Extensible as XML applications will work as expected even if new data is added (or removed).

## Difference between XML and HTML
| XML                               | HTML                           |
| --------------------------------- | -------------------------------|
|HTML tags are predefined tags.     | XML tags are user defined tags.|
|HTML is not Case sensitive.        | 	XML is Case sensitive.       |
|HTML tags are used for displaying the data.|XML tags are used for describing the data not for displaying |
|HTML document size is relatively small.|XML document size is relatively large as the approach of formatting|

## Structure of XML File
![alt text](https://github.com/MasterANK/py4xml/blob/main/XML%20tree.jpg "XML Tree")

## Example File:
``` 
<bookstore>
  <book>
    <title>Everyday Italian</title>
    <author>Giada De Laurentiis</author>
    <year>2005</year>
    <price>30.00</price>
  </book>
  <book2>
    <title>Harry Potter and the Goblet of Fire</title>
    <author>J. K. Rowling</author>
    <year>2000</year>
    <price>30.00</price>
  </book2>
</bookstore>
```

## Uses of XML:

+ **Used in XML AJAX:** AJAX allows web pages to be updated asynchronously by exchanging data with a web server behind the scenes. This means that it is possible to update parts of a web page, without reloading the whole page.  *AJAX applications might use XML to transport data*

+ **Used in XPath:** XPath stands for XML Path Language. XPath uses path expressions to select nodes or node-sets in an XML document. These path expressions look very much like the path expressions you use with traditional computer file systems.

+ **Used in XSL:** XSL (eXtensible Stylesheet Language) is a styling language for XML.

+ **Used in XQuery:** XQuery is a language for finding and extracting elements and attributes from XML documents. XQuery is to XML what SQL is to databases.


#
# ***What is Py4XML?***
Py4xml is the module created in order to interpret these XML file in python using python just like csv module which interpret CSV or pickle modules which interpret Binary files. Py4xml has the ability to read and write an .xml file. Py4xml can also convert the xml file into csv file or SQL table. 

#
# ***Installation***
The Project file can be found on Github: [Py4XML Github](https://github.com/MasterANK/py4xml/tree/main)

#
# ***Reading an XML File***
Py4xml has a function called **read_xml()** which requires *file_object as a parameter* and *returns an xml_reader class object* which contains all the extracted data from the given xml file.

### Example:
```
import py4xml

# The xml file to read is "xml 1.xml"
f = open("xml 1.xml","r") #Opening the file in read mode

# read_xml() function will read the file and extract the data
xml_file = py4xml.read_xml(f) # it takes file_object and return xml object

# Now with the help of multiple functions inside the xml object in xml_file we can extract the required data as shown in below example

```
## 1. Getting reading the Root Element:
By accessing the **root_element** variable in the xml file object returned by read_xml() function. It will return the **root_element**
```
print(xml_file.root_element)
#It will return the root element
```

## 2. Getting list of all Element:
By accessing the **element_stack** variable in the xml file object returned by read_xml() function. It will return the **element_stack**

```
print(xml_file.element_stack)
#It will return the list of element present in the xml file
```

## 3. Getting the Dictionary of elements in xml file
By accessing the **main_dict** variable in the xml file object returned by read_xml() function. It will return the **nested dictionary** of element where key will be elements and its value will be another dictionary where the key this time is sub element and its value will be the value of the sub element.

Sample Structure of the nested dictionary:

{element1 : {sub_element1 : value, sub_element2 : value}, element2 : {sub_element1: value}}

```
print(xml_file.main_dict)
#It will return the nested dictionary of elements of structure as shown above
```

## 4.  Getting the Dictionary of selected element in xml file
By accessing the **find_element()** function in the xml file object returned by read_xml() function. It requires one required parameter which is the element you need to find in the xml file and it will return the **dictionary** of sub element of the supplied element.

```
print(xml_file.find_element("element"))
#It will return the dictionary of sub elements of the given element 
```

#
# ***Reading an XML File with Attributes***
Although it is not recomended but xml file can sometimes have an attribute defined in the element tag. As shown in the example below-
```
<messages>
  <note id="501">
    <to>Tove</to>
    <from>Jani</from>
    <heading>Reminder</heading>
    <body>Don't forget me this weekend!</body>
  </note>
  <note id="502">
    <to>Jani</to>
    <from>Tove</from>
    <heading>Re: Reminder</heading>
    <body>I will not</body>
  </note>
</messages>
```
in the given example, it can we concluded that id is category and is defined as *\<element category="Value">* 

While iterating over such xml files with py4xml, the structure of main dictionary is slightly changed to accompany the category tag. The keys of the ***main_dict*** will be changed as ***element_value*** where value is the value of the category and a new sub_element will be added for category as ***\<Category_category\>Value\</Category_category\>*** 

Sample New Structure of the nested dictionary:

{element1_value : {category_category1 : value, sub_element1 : value, sub_element2 : value}, element2_value : {category_category1 : value, sub_element1: value}}


#
# ***Writing Dictionary in XML File***
Py4xml has a function called **dict_write_xml()** and it has 3 required parameters. The first parameter is for the *root_element* which will commonly be in string format. The secound parameter is *data* or the elements and sub_element which should be provided in the nested dictionary format as described below. The third and last parameter is the *write_f* or file_object where everything is supposed to be written. This functions dosen't return anything.

Sample Structure of the nested dictionary:

{element1 : {sub_element1 : value, sub_element2 : value}, element2 : {sub_element1: value}}

*Note - The file must be opened in  write mode only. If you wish to append data there is another function for that.

### Example:
```
import py4xml

root_element = "Cards" 

#Nested dictionary of Sample Data
data = {"Pika" : {"HP": 100,"Defence" : 50,"Speed": 80 }, "Snorlax":{"HP":100,"Defence":100,"Speed": 0} }

#The xml file to write is "xml 2.xml"
f = open("xml 2.xml","w") #Opening the file in write mode

# dict_write_xml() will write the data in file
dict_write_xml(root_element,data,f)

```
### Output in File:
```
<cards>
  <Pika>
    <HP>100</HP>
    <Defence>50</Defence>
    <Speed>80</Speed>
  </Pika>
  <Snorlax>
    <HP>100</HP>
    <Defence>100</Defence>
    <Speed>0</Speed>
  </Snorlax>
</cards>
```



