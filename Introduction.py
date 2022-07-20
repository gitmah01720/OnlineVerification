from asyncore import write
from cgitb import handler
from csv import reader
import string
import requests
from bs4 import BeautifulSoup, NavigableString, Tag
url = "https://codewithharry.com"

class files:
    pth="";
    
    def __init__(self,pAth):
        try :
           reder = open(pAth,"r");
        except :
            print("File Does NOT exixt!\n");
            return
        self.pth = pAth;
        

    def readfile(self):
        reder = open(self.pth,"r");
        st = reder.read();
        print(st)
        reder.close()
        return st

    def writeinfile(self,tx):
        writer = open(self.pth,"w");
        writer.write(tx)
        writer.close();
    def appendinfile(self,tx):
            writer = open(self.pth,"a");
            writer.write(tx)
            writer.close();

        
#*  1. getting HTML code


r = requests.get(url); #getttting html code.
htmlcodeRaw = r.content;  
handle = files("index.html")


# print(htmlcode);
# handle.writeinfile(str(htmlcodeRaw));
# handle.readfile();

# * 2. HTML parsing
soup = BeautifulSoup(htmlcodeRaw,'html.parser')
# print(soup.prettify());
handle.writeinfile(str(soup.prettify()));
# handle.readfile()



#* 3. HTML tree traversal;
title = soup.title;  # returns tytle tag in BeautiFulSoup form.
# print(type(title.string)) // 
# print(title.get_text());   ===  print(title.string); 
# exit()

# * type of objects in soup.
# 1. Tag                 print(type(soup.title));
# 2. NavigableString    print(type(title.string));
                    #this navigable string(text content of tag ) if tag contains no child.
                    #if tag contains more than one child then use OBJ.strings = list of all texts
                    
# 3. BeautifulSoup  object   print(type(soup));  
# 4. comments    #  Making soup with HTML code
        # markupLanguage = '<p><!-- This is ca comment --></p>';
        # soup2 = BeautifulSoup(markupLanguage,'html.parser');
        # print(type(soup2.p.string));


# get all paragraphs:
allParas = soup.findAll('p');
# print(allParas)

#  Print all Links( anchor tags)
alllinks = soup.findAll('a');
# print(alllinks)

# Get first paragrah of tag.
firstPara = soup.find('p');
# print(firstPara['class']);  # Prints class of given tag.

#  Find all tags with given class name.
# print(soup.findAll(class_ = 'text-gray-500'));  #list of element.

#  Get text from first paragraph.
# print(soup.find('p').get_text());

#  print all the links of page.
# basLink = url;
# for linkTag in soup.findAll('a'):
    # linksHref = linkTag.get('href');
    # if(linksHref!= '#'):
        # print(basLink+linksHref,'\n')


#  * 4. Now Tree travarsal.
# selecting tag with id
# navbar = soup.find('div',id='nav-content');
# we can also use this wey.
navbar = soup.select_one('#nav-content')  

# print(navbar.prettify())
# print(type(navbar.strings));  // list of text of all childs inside a tag.

#  getting all childerns of a given tag.
    # OBJ.children gives generator ( reference to NodeList of childrens );
    # OBL.contents gives static List of Nodes which requires memory to store.


# for child in  navbar.children:
    # print(child,'\n');

#  find list items.
allLitags = navbar.find('ul').findAll('li');
# for l in allLitags:
#     print(l,'\n');


# for l in navbar.find('ul').children:
    # print(l);

fl = allLitags[0]; # first list.  
print(fl)

for prnt in fl.parents:
    print(prnt.name);


#  Note when we use next sibling and prev-siblings then 
# beautiful soup travers on all HTML-Elements and Text-Nodes.

# Selectors == find(id="....");
allScripts = soup.select('script');
print(allScripts );

 
