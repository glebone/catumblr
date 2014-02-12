import pygtk
pygtk.require('2.0')
import gtk
import urllib2

class catImageBox:

    
    def __init__(self, image_url, width, height):
        self.image=gtk.Image()
        response=urllib2.urlopen(image_url)
        loader=gtk.gdk.PixbufLoader()
        loader.write(response.read())
        loader.close()        
        pixbuf = loader.get_pixbuf()
        pixbuf = pixbuf.scale_simple(width, height, gtk.gdk.INTERP_BILINEAR)
        self.image.set_from_pixbuf(pixbuf)
        # This does the same thing, but by saving to a file
        # fname='/tmp/planet_x.jpg'
        # with open(fname,'w') as f:
        #     f.write(response.read())
        # self.image.set_from_file(fname)
     
    