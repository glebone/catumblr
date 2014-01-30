#!/usr/bin/env python


import gtk
import ntpath
from tumblpy import Tumblpy
import os
import platform
import json
from HTMLParser import HTMLParser
import tumblrListView
import getImage

#  ^..^ CAT(c) 2014 CATumblr - Tumblr client on PyGTK
# --------------------------------------------------------
# 29 Jan 2014 glebone@yandex.ru 




ntpath.basename("a/b/c")
 
entry_name = gtk.Entry()
tag_entry = gtk.Entry()
textview = gtk.TextView() 
image_path = ""


def do_post(path):
  print "Posting..."
  t = Tumblpy("sYKNnjJRqbxWWlg19sY8WYnZyQi6wURbilnE4k3vsyqX4vc4ER","n8mtWzKieR8qgTdwUWNhF3OYZVIsvMZXvVr9DKPlCGI6wE2VLV",
      "PyvcruFPx1YqhdAOkCWjCPWMBIYx3fUJaiFzjhxpkwUwps0VjC","Zjwmi2wYA83rtIdoL82BcWcj5sxm5QrI1MEnZX4DzFQHWydx1C")
  tbuff = textview.get_buffer()
  article_text = tbuff.get_text(tbuff.get_start_iter(), tbuff.get_end_iter())
  blog_url = t.post('user/info')
  blog_url = blog_url['user']['blogs'][1]['url']
  tags = "catumblr , "+ platform.node()
  photo = open(path.get_text(), 'rb')
  post = t.post('post', blog_url=blog_url, params={'type':'photo', 'caption': article_text, 'data': photo, 'tags':tags})
  print post  # returns id if posted successfully

def make_box_labels():

  box = gtk.HBox(True, 1)
 
  # Create a series of buttons with the appropriate settings

  label = gtk.Label("Name of post")
  label.set_alignment(0, 0)
  box.pack_start(label, False, False, 0)
  label.show()
  label = gtk.Label("Tag")
  label.set_alignment(0, 0)
  box.pack_start(label, False, False, 0)
  label.show()
  
  return box

def make_entry_box():

  box = gtk.HBox(True, 1)
  # Create a series of buttons with the appropriate settings
  entry_name.set_max_length(50)
  entry_name.set_text("hello")
  entry_name.insert_text(" world", len(entry_name.get_text()))
  entry_name.select_region(0, len(entry_name.get_text()))
  box.pack_start(entry_name, True, True, 1)
  entry_name.show()
  tag_entry.set_max_length(50)
  tag_entry.set_text("catumblr")
  box.pack_start(tag_entry, True, True, 1)
  tag_entry.show()

  return box


def make_text_area_box():

  box = gtk.HBox(True, 1)
  # Create a series of buttons with the appropriate settings
  sw = gtk.ScrolledWindow()
  sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
  textbuffer = textview.get_buffer()
  sw.add(textview)


  box.pack_start(sw, True, True, 1)
  textview.show()
  sw.show()

  return box    

def show_window():
  window = gtk.Window(gtk.WINDOW_TOPLEVEL)
  window.set_title("Tumblr client")
  #window.connect("delete_event", self.delete_event)
  window.set_border_width(10)

  box1 = gtk.VBox(False, 0)
  label = gtk.Label("^..^ CAT(c) Flipflop blog client ")
  label.set_alignment(0, 0)
  box1.pack_start(label, False, False, 0)
  label.show()

  separator = gtk.HSeparator()
  box1.pack_start(separator, False, True, 5)
  separator.show()

  box2 = make_box_labels()
  box1.pack_start(box2, False, False, 0)
  box2.show()
 
     
  box3 = make_entry_box()
  box1.pack_start(box3, False, False, 0)
  box3.show()
 
  separator = gtk.HSeparator()
  box1.pack_start(separator, False, True, 5)
  separator.show()
 
  box4 = make_text_area_box()
  box1.pack_start(box4, False, False, 0)
  box4.show()
 
  separator = gtk.HSeparator()
  box1.pack_start(separator, False, True, 5)
  separator.show()


  imbox = gtk.HBox(False, 0)
  button = gtk.Button("Add Image")
  imlabel = gtk.Label("No image")
  button.connect("clicked", lambda w: getImage.add_image(imlabel))
  imbox.pack_start(button, True, False, 0)
  imbox.pack_end(imlabel, True, False, 0)
  
  postbox = gtk.HBox(False, 0)
  post_button = gtk.Button("Post")
  post_button.connect("clicked", lambda w: do_post(imlabel))
  postbox.pack_start(post_button, True, False, 0)
  
  
  box1.pack_start(imbox, False, False, 0)
  box1.pack_end(postbox, False, False, 0)
  
  window.add(box1)
  

  button.show()
  post_button.show()
  imlabel.show()
  postbox.show()
  imbox.show()
  box1.show()
  window.show()

 
 
def open_app(data=None):
  show_window()
 
def close_app(data=None):
  message(data)
  gtk.main_quit()
 
def make_menu(event_button, event_time, data=None):
  menu = gtk.Menu()
  open_item = gtk.MenuItem("Open App")
  close_item = gtk.MenuItem("Close App")
  
  #Append the menu items  
  menu.append(open_item)
  menu.append(close_item)
  #add callbacks
  open_item.connect_object("activate", open_app, "Open App")
  close_item.connect_object("activate", close_app, "Close App")
  #Show the menu items
  open_item.show()
  close_item.show()
  
  #Popup the menu
  menu.popup(None, None, None, event_button, event_time)
 
def on_right_click(data, event_button, event_time):
  #make_menu(event_button, event_time)
  tumblrListView.tumblrListView()

def on_left_click(event):
  print "Showww!"
  show_window()
  
 
if __name__ == '__main__':
  file = open("resources/ticon.png", "rb")
  binary = file.read()
  loader = gtk.gdk.PixbufLoader("png")
  loader.write(binary)
  loader.close()
  pixbuf = loader.get_pixbuf()
  #icon = gtk.status_icon_new_from_stock(gtk.STOCK_ABOUT)
  icon  = gtk.status_icon_new_from_pixbuf(pixbuf)
  icon.connect('popup-menu', on_right_click)
  icon.connect('activate', on_left_click)
  gtk.main()