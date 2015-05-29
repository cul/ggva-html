Content originally drawn from, and redeployable to:
/www/data/cu/lweb/eresources/archives/avery/greene/html/subs
/www/data/cu/lweb/eresources/archives/avery/greene/images

Given an image PID, the DLC iframe URL is:
https://dlc.library.columbia.edu/catalog/${PID}/details

The PIDs can be mapped from the image IDs in the HTML. The JPEG source URL:

http://www.columbia.edu/cgi-bin/cul/mrsid/image_jpeg.pl?client=ggva&amp;image=NYDA.1960.001.00870.sid&amp;x=1200&amp;y=800&amp;level=2&amp;width=800&amp;height=600


... should be replaced with a link to the IIIF cache:

https://repository-cache.cul.columbia.edu/iiif/${PID}/full/1200,/0/default.png

In the example above, the ID NYDA.1960.001.00870 maps to the PID ldpd:288341, so the image link source would be:

https://repository-cache.cul.columbia.edu/iiif/ldpd:288341/full/1200,/0/default.png

These links open in a new window in the pages in the images directory, but not in the html/subs directory. 

The MrSID URL:

http://www.columbia.edu/cgi-bin/cul/mrsid/image_sid.pl?client=ggva&amp;image=NYDA.1960.001.00871.sid

... should be replaced with a link to the IIIF/OpenSeaDragon iFrame source in the DLC:

https://dlc.library.columbia.edu/catalog/${PID}/details

... or in the case of NYDA.1960.001.00871:

https://dlc.library.columbia.edu/catalog/ldpd:289436/details

These links open in a new window in the pages in the images directory, but not in the html/subs directory.

SAMPLE DATA MAP:

NYDA.1960.001.00870 ldpd:288341
NYDA.1960.001.00871 ldpd:289436
NYDA.1960.001.00872 ldpd:289341
NYDA.1960.001.00873 ldpd:286821

RUNNING TESTS:

* include lib on PYTHONPATH ENV variable
* python -m unittest discover -s test

FOLLOW UP:
WARNING: MISSING ID NYDA.1987.003.00128
WARNING: MISSING ID NYDA.1960.001.00143
WARNING: MISSING ID NYDA.1960.001.00144
WARNING: MISSING ID NYDA.1960.001.02004

WARNING: MISSING ID 3302050102 (missing in exhibit)
WARNING: MISSING ID 3302050202 (missing in exhibit)
WARNING: MISSING ID 3326010101 (missing in exhibit)
WARNING: MISSING ID 3328031102 (missing in exhibit)
WARNING: MISSING ID 3353071201 (present in exhibit, identical to 3438042901 in SCV as ldpd:156161)
WARNING: MISSING ID 3353071202 (present in exhibit, identical to 3438042902 in SCV as ldpd:156281)
WARNING: MISSING ID 3353071203 (present in exhibit, identical to 3438042903 in SCV as ldpd:155837)
WARNING: MISSING ID 3353071204 (present in exhibit, identical to 3438042904 in SCV as ldpd:155937)
WARNING: MISSING ID 3353071205 (present in exhibit, identical to 3438042905 in SCV as ldpd:155939)
WARNING: MISSING ID 3401010101 (missing in exhibit)
WARNING: MISSING ID 3407040110 (missing in exhibit)
WARNING: MISSING ID 5201030101 (missing in exhibit, sub-631/proj-13712 also missing)
WARNING: MISSING ID 5201030201 (missing in exhibit, sub-631/proj-13712 also missing)
