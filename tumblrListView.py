#!/usr/bin/env python


import pygtk
pygtk.require('2.0')
import gtk
from tumblpy import Tumblpy
import os
import platform
import json
from HTMLParser import HTMLParser


#  ^..^ CAT(c) 2014 CATumblr - Tumblr client on PyGTK
# --------------------------------------------------------
# 29 Jan 2014 glebone@yandex.ru 


class MLStripper(HTMLParser):
	def __init__(self):
		self.reset()
		self.fed = []
	def handle_data(self, d):
		self.fed.append(d)
	def get_data(self):
		return ''.join(self.fed)





class tumblrListView:
	
	
	def destroy(self, widget):
		gtk.main_quit()
		
	def remove_table(self, widget):
		self.scrolled_window.remove(self.scrolled_window.get_child())	
		self.table = self.get_tumblr_table()
		self.table.show()
		self.scrolled_window.add_with_viewport(self.table)
		
	def get_tumblr_table(self):
	    t = Tumblpy("sYKNnjJRqbxWWlg19sY8WYnZyQi6wURbilnE4k3vsyqX4vc4ER","n8mtWzKieR8qgTdwUWNhF3OYZVIsvMZXvVr9DKPlCGI6wE2VLV",
	    "PyvcruFPx1YqhdAOkCWjCPWMBIYx3fUJaiFzjhxpkwUwps0VjC","Zjwmi2wYA83rtIdoL82BcWcj5sxm5QrI1MEnZX4DzFQHWydx1C")
	    
	    blog_url = t.post('user/info')
	    blog_url = blog_url['user']['blogs'][0]['url']
	    
	    posts = t.get('posts', blog_url=blog_url)
	    posts_count = posts["total_posts"]
	    #print posts
	    table = gtk.Table(posts_count, 1, False)
	    
	    # set the spacing to 10 on x and 10 on y
	    table.set_row_spacings(10)
	    table.set_col_spacings(10)
	    
	    # pack the table into the scrolled window
	    i = 0
	    for cur_post in posts["posts"]:
			buffer = ""
			if cur_post["type"] == "text":
				buffer = cur_post["body"]
			if cur_post["type"] == "photo":
				print cur_post["caption"]
				buffer = cur_post["caption"]
				
			s = MLStripper()
			s.feed(buffer)	
			label = gtk.Label(s.get_data())
			label.set_line_wrap(True)
			label.set_justify(gtk.JUSTIFY_LEFT)
			label.set_width_chars(30)
			label.show()
			
			#date box
			date_box = gtk.HBox(True, 1)
			date_icon = gtk.Image()
			date_icon.set_from_file("resources/cal.png")
			date_icon.show()
			fdate = cur_post["date"]
			date_label = gtk.Label(fdate.split(" ")[0])
			date_label.set_line_wrap(True)
			date_label.show()
			date_box.pack_start(date_icon, True, True, 1)
			date_box.pack_end(date_label, True, True, 1)
			date_box.show()
			
			#tag box
			tag_box = gtk.HBox(True, 1)
			tag_icon = gtk.Image()
			tag_icon.set_from_file("resources/tag.png")
			tag_icon.show()
			ftags = ""
			for cur_tag in cur_post["tags"]:
				ftags += cur_tag + " "
				
			
			tag_label = gtk.Label(ftags)
			tag_label.set_line_wrap(True)
			tag_label.show()
			tag_box.pack_start(tag_icon, True, True, 1)
			tag_box.pack_end(tag_label, True, True, 1)
			tag_box.show()
			
			separator = gtk.HSeparator()
			separator.show()
			
			box = gtk.VBox(True, 1)
			box.pack_start(date_box, True, True, 1)
			if cur_post["tags"].count > 0:
				box.pack_start(tag_box, True, True, 1)
			box.pack_start(label, True, True, 0)
			box.pack_end(separator, True,  True, 0)
			box.show()
			table.attach(box, 1, 2, i, i+1)
			i = i+1
	    return  table
		

	    
    
        		
	def __init__(self):
		# Create a new dialog window for the scrolled window to be
		# packed into. 
				
		self.window = gtk.Dialog()
		self.window.connect("destroy", self.destroy)
		self.window.set_title("^..^ CATumblr 0.0.1")
		self.window.set_border_width(0)
		self.window.set_size_request(300, 500)

		# create a new scrolled window.
		self.scrolled_window = gtk.ScrolledWindow()
		self.scrolled_window.set_border_width(10)

		self.scrolled_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)

		# The dialog window is created with a vbox packed into it.
		self.window.vbox.pack_start(self.scrolled_window, True, True, 0)
		self.scrolled_window.show()

		# create a table of 10 by 10 squares.
		self.table = self.get_tumblr_table()
		self.scrolled_window.add_with_viewport(self.table)
		self.table.show()

		# this simply creates a grid of toggle buttons on the table
		# to demonstrate the scrolled window.
		
		
		
#		for i in range(10):
#			buffer = "button (%d)" % (i)
#			label = gtk.Label(buffer)
#			table.attach(label, 1, 2, i, i+1)
#			label.show()

		# Add a "close" button to the bottom of the dialog
		image = gtk.Image()
		image.set_from_file("resources/delete.png")
		rimage = gtk.Image()
		rimage.set_from_file("resources/trackback.png")
		rimage.show()
        
        
		button = gtk.Button()
		image.show()
		button.add(image)
		button.connect_object("clicked", self.destroy, self.window)
		rbutton = gtk.Button()
		rbutton.add(rimage)
		rbutton.show();
		
		
		rbutton.connect_object("clicked", self.remove_table, self.window)

		# this makes it so the button is the default.
		button.set_flags(gtk.CAN_DEFAULT)
		
		self.window.action_area.pack_start( rbutton, True, True, 0)
		self.window.action_area.pack_end( button, True, True, 0)

		# This grabs this button to be the default button. Simply hitting
		# the "Enter" key will cause this button to activate.
		button.grab_default()
		button.show()
		self.window.show()

