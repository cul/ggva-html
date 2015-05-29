#!python
from optparse import OptionParser
import sys
import mrsid
if __name__ == '__main__':
  m = sys.argv[1]
  i = sys.argv[2]
  o = sys.argv[3]
  m = mrsid.read_map(sys.argv[1])
  mrsid.Transformer(m).transform(i,o)