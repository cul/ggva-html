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