#!python
from urlparse import urlparse, parse_qs
from os import listdir
from os.path import exists, isdir, basename, join
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
  """Parse out the MrSID file identifier in a url"""
  if detect_jpeg(input) or detect_sid(input):
    q = parse_qs(urlparse(input).query)
    if 'image' in q:
      # there are some input files that have mistakenly encoded sid identifiers
      return re.sub(r'\.sid(\.sid)?$','',q['image'][0])
    else:
      return q
  return False
def transform_url(path,id_map):
  _id = parse_id(path)
  if _id:
    if _id not in id_map: return False
#       replace URL
    format = IIIF_LINK if detect_jpeg(path) else DLC_DETAILS
    return format % {'pid' : id_map[_id]}
  return False
def read_map(path):
  m = {}
  with open(path) as f:
    line = f.readline()
    p = map(lambda x: x.strip(' \n\t\r'), line.split(','))
    if (p[0] == 'pid'):
      pid_first = True
    else:
      pid_first = False
      if (p[0] != 'id'):
        m[p[0]] = p[1]
    for line in f:
      p = map(lambda x: x.strip(' \n\t\r'), line.split(','))
      if (len(p) != 2): continue
      if pid_first:
        m[p[1]] = p[0]
      else:
        m[p[0]] = p[1]
  return m
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
  def pid_for(self, path):
    return self.id_map[path]
  def transform_file(self,input,output):
    if isdir(output):
      output = join(output,basename(input))
    input = open(input,'r')
    src = input.read()
    soup = Whitespace(src, 'html.parser')
    soup.convertHTMLEntities = False
    input.close()
    delta = False
    for a in soup.find_all('a'):

      repl = transform_url(a.get('href'), self.id_map) if a.get('href') else False
      if repl:
        delta = True
        was_sid = detect_sid(a.get('href')) if a.get('href') else False
        a['href'] = repl
        if was_sid:
#       replace text 'MrSID' with 'Zoom'
          a.string.replace_with('Zoom')
    if delta:
      src = soup.encode("utf8",formatter="html")
    open(output,'w').write(src)
  def transform(self, input, output):
    if isdir(input):
      for file in listdir(input):
        if not isdir(file):
          self.transform_file(join(input,file),output)
    else:
      self.transform_file(input,output)
