#!python
from urlparse import urlparse, parse_qs
import re
from xml.etree.ElementTree import ElementTree
DLC_DETAILS = "https://dlc.library.columbia.edu/catalog/%(pid)s/details"
IIIF_LINK = "https://repository-cache.cul.columbia.edu/iiif/%(pid)s/full/1200,/0/default.png"

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
class Transformer:
  def __init__(self,id_map):
    self.id_map = id_map
  def transform(self, input, output):
    tree = ElementTree()
    tree.parse(input)
    links = tree.getiterator("a")
    for a in links:

      repl = transform_url(a.attrib['href'], self.id_map) if a.attrib.has_key('href') else False
      if repl:
        a.attrib['href'] = repl
        if detect_sid(a.attrib['href']):
          a.text = 'Zoom'
#       parse out ID
#       lookup PID
#       replace URL
#       replace text 'MrSID' with 'Zoom'
#     elsif a matches jpeg pattern:
#       parse out ID
#       lookup PID
#       replace URL
    tree.write(output)