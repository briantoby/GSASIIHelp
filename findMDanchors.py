# find anchors in MD version of Help files
import glob
import os
from html.parser import HTMLParser
dirname = os.path.abspath(os.path.dirname("__file__"))
files = glob.glob(os.path.join(dirname,'site','*.html'))
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a' and 'name' in [i[0] for i in attrs]:
            print('\t',[i[1] for i in attrs if i[0] == 'name'][0])
        elif tag == 'div' and 'id' in [i[0] for i in attrs]:
            print("Encountered a start tag:", tag, attrs)
parser = MyHTMLParser()
for fil in sorted(files):
    print('\n'+os.path.split(fil)[1])
    parser.feed(open(fil,'r').read())
