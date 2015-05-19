Content originally drawn from, and redeployable to:
/www/data/cu/lweb/eresources/archives/avery/greene/html/subs
/www/data/cu/lweb/eresources/archives/avery/greene/images

Given an image PID, the DLC iframe URL is:
https://dlc.library.columbia.edu/catalog/${PID}/details

The PIDs can be mapped from the image IDs in the HTML. The JPEG source URL:

http://www.columbia.edu/cgi-bin/cul/mrsid/image_jpeg.pl?client=ggva&amp;image=NYDA.1960.001.00870.sid&amp;x=1200&amp;y=800&amp;level=2&amp;width=800&amp;height=600


... should be replaced with a link to the IIIF cache:

https://repository-cache.cul.columbia.edu/images/${PID}/scaled/1200.png

These links open in a new window.

The MrSID URL:

http://www.columbia.edu/cgi-bin/cul/mrsid/image_sid.pl?client=ggva&amp;image=NYDA.1960.001.00871.sid

... should be replaced with a link to the IIIF/OpenSeaDragon iFrame source in the DLC:

https://dlc.library.columbia.edu/catalog/${PID}/details

These links open in a new window.