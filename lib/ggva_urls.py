#!python
from urlparse import urlparse, parse_qs
import re
from xml.etree.ElementTree import ElementTree
from bs4 import BeautifulSoup
DLC_DETAILS = "https://dlc.library.columbia.edu/catalog/%(pid)s/details"
IIIF_LINK = "https://repository-cache.cul.columbia.edu/iiif/%(pid)s/full/1200,/0/default.jpg"

def detect_sid(input):
  path = urlparse(input).path
  return re.search(r'\/image_sid\.pl$',path) != None
def detect_jpeg(input):
  path = urlparse(input).path
  return re.search(r'\/image_jpeg\.pl$',path) != None
def parse_id(input):
  if detect_jpeg(input) or detect_sid(input):
    q = parse_qs(urlparse(input).query)
    if 'image' in q:
      return re.sub(r'\.sid$','',q['image'][0])
    else:
      return q
  return False
def transform_url(input,map):
  _id = parse_id(input)
  if _id:
    format = IIIF_LINK if detect_jpeg(input) else DLC_DETAILS
    return format % {'pid' : map[_id]}
  return False
class Whitespace(BeautifulSoup):
  def pushTag(self, tag):
    #print "Push", tag.name
    if self.currentTag:
        self.currentTag.contents.append(tag)
    self.tagStack.append(tag)
    self.currentTag = self.tagStack[-1]
    self.preserve_whitespace_tag_stack.append(tag)

class Transformer:
  def __init__(self,id_map):
    self.id_map = id_map
  def transform(self, input, output):
    input = open(input,'r')
    src = input.read()
    soup = Whitespace(src, 'html.parser')
    soup.convertHTMLEntities = False
    input.close()
    for a in soup.find_all('a'):

      repl = transform_url(a.get('href'), self.id_map) if a.get('href') else False
      if repl:
        was_sid = detect_sid(a.get('href')) if a.get('href') else False
        a['href'] = repl
        if was_sid:
          a.string.replace_with('Zoom')
#       parse out ID
#       lookup PID
#       replace URL
#       replace text 'MrSID' with 'Zoom'
#     elsif a matches jpeg pattern:
#       parse out ID
#       lookup PID
#       replace URL
#    open(output,'w').write(soup.prettify(formatter="html").encode("utf8"))
    new_src = soup.encode("utf8",formatter="html")
    open(output,'w').write(new_src)