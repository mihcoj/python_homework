#!/usr/bin/env python
"""
Python course EBC 2016
Day 4 - Exercise instructions
Lucas Sinclair <lucas.sinclair@me.com>

* Write a program in a file called "exercise_day4.py"
* You have until the start of the next course at 13h00 tomorrow to finish it.
* Once the program is done, upload it in your github repository "python_homework" in a directory named "day4".

The program should read the file named "lulu_mix_16.csv". This file should be placed in your "home" directory. Your program should use the OS environment variable "$HOME" to find the file.
This file is a comma separated values format. It contains information about different music tracks.

For each line in the file (excluding the header) the program should produce a new "Song" instance. It should place all the Song instances created in a list called "songs".

### Each Song object should have these attributes:

* title
The title of the song as a string.

* artist
The artist of the song as a string.

* duration
The title of the song as an integer in seconds.

When creating new Song instances:

-> If the duration of a song is not a number, set it to 0, but issue a warning.
-> If the duration of a song is negative, raise an Exception and stop the program.

### Each Song object should have these methods:

* pretty_duration(self)
Returns a nice string describing the duration. For instance if the duration is 3611, this methods takes no input and returns "01 hours 00 minutes 11 seconds" as a string.

* play(self)
Automatically opens a webpage on your computer with a youtube search for the title.

Once your program is ready the following four lines of code should run without errors. (After you have removed the negative duration song!).
"""
#
####################################################################################################################################################
# Import sttuff
import os
from os.path import expanduser
import warnings
import datetime
import webbrowser
#
####################################################################################################################################################
#
class Song(object):
	""" A class that describes musical songs """
	good_song = True 
	def __init__(self,title = "alpha", artist = "lambra", duration = None): #constructor
		self.artist = artist
		self.title = title
		self.duration = duration
		''' check duration if it is a positive integer '''
		try: self.duration = int(self.duration)

		except ValueError:
			self.duration = 0
			warnings.warn("duration is not a number")

		if int(self.duration) < 0: raise Exception("duration is negative")

	def description(self):
		''' print basic info about this song '''
		return {"artist": self.artist, "title": self.title ,"duration": self.duration}

	def pretty_duration(self):
		''' Make the duration of the song print in nice format'''
		return str(datetime.timedelta(seconds = self.duration))

	def play(self):
		''' search youtube for the title of the song'''
		webbrowser.open("https://www.youtube.com/results?search_query=%s" % self.title)
#
####################################################################################################################################################
# Set paths and file names 
in_path = expanduser("~")
file_name = "lulu_mix_16.csv"
path_file = ("%s/%s") % (in_path, file_name)
#
####################################################################################################################################################
# Check that the path is valid #
if not os.path.exists(path_file):
	raise Exception("%s can not be found at '%s'." % (file_name, in_path)) 
#
####################################################################################################################################################
#

#
####################################################################################################################################################
# Program doing stuff starts here

parsed = [tuple(l.strip('\n').split(',')) for l in open(path_file)] # Parsing the .csv file into a list a tuples

songs = [Song(*song_tuple) for song_tuple in parsed[1:]] # Unpack tuple and send as argument to create a song

for s in songs: print s.artist
for s in songs: print s.pretty_duration()
print sum(s.duration for s in songs), "seconds in total"
songs[6].play()
