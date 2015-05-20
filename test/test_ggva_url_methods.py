import unittest
import difflib
import ggva_urls
class TestGGVAUrlMethods(unittest.TestCase):
  HAS_JPEG = "http://www.columbia.edu/cgi-bin/cul/mrsid/image_jpeg.pl?client=ggva&amp;image=NYDA.1960.001.00870.sid&amp;x=1200&amp;y=800&amp;level=2&amp;width=800&amp;height=600"
  NO_JPEG = "NYDA89-F748.html"
  HAS_SID = "http://www.columbia.edu/cgi-bin/cul/mrsid/image_sid.pl?client=ggva&amp;image=NYDA.1960.001.00871.sid"
  NO_SID = "NYDA89-F748.html"
  DLC_DETAILS = "https://dlc.library.columbia.edu/catalog/ldpd:289436/details"
  IIIF_LINK = "https://repository-cache.cul.columbia.edu/iiif/ldpd:288341/full/1200,/0/default.png"
  ID_MAP = {
  'NYDA.1960.001.00870' : 'ldpd:288341',
  'NYDA.1960.001.00871' : 'ldpd:289436',
  'NYDA.1960.001.00872' : 'ldpd:289341',
  'NYDA.1960.001.00873' : 'ldpd:286821'
  }

  def assertMultiLineEqual(self, expected, actual, msg=None):
    """Assert that two multi-line strings are equal or fail with a diff

    """
    self.assertTrue(isinstance(expected, str),
            'Expected argument is not a string')
    self.assertTrue(isinstance(actual, str),
            'Actual argument is not a string')
    expected = open(expected, 'r').readlines()
    actual = open(actual,'r').readlines()
    diff = difflib.ndiff(expected,actual)
    if diff:
      message = '' + reduce(lambda x, y: x+y, diff)
      if msg:
        message += " : " + msg
      self.fail("Multi-line strings are unequal:\n" + message)

  def test_detect_sid(self):
    self.assertEqual(ggva_urls.detect_sid(self.HAS_SID), True)
    self.assertEqual(ggva_urls.detect_sid(self.HAS_JPEG), False)
    self.assertEqual(ggva_urls.detect_sid(self.NO_SID), False)

  def test_detect_jpeg(self):
    self.assertEqual(ggva_urls.detect_jpeg(self.HAS_JPEG), True)
    self.assertEqual(ggva_urls.detect_jpeg(self.HAS_SID), False)
    self.assertEqual(ggva_urls.detect_jpeg(self.NO_JPEG), False)

  def test_parse_id(self):
    self.assertEqual(ggva_urls.parse_id(self.HAS_SID), 'NYDA.1960.001.00871')
    self.assertEqual(ggva_urls.parse_id(self.HAS_JPEG), 'NYDA.1960.001.00870')

  def test_transform_url(self):
    self.assertEqual(ggva_urls.transform_url(self.HAS_SID,self.ID_MAP), self.DLC_DETAILS)
    self.assertEqual(ggva_urls.transform_url(self.HAS_JPEG,self.ID_MAP), self.IIIF_LINK)

  def test_Transformer(self):
    t = ggva_urls.Transformer(self.ID_MAP)
    fixture = "fixtures/test/input/NYDA89-F301.html"
    expected = "fixtures/test/expected/NYDA89-F301.html"
    actual = "tmp/NYDA89-F301.html"
    t.transform(fixture,actual)
    self.assertMultiLineEqual(expected,actual)
if __name__ == '__main__':
  unittest.main()