#! /usr/bin/env python2

import easygui
import wave
import pyaudio
import sys



class Audio():
	chunk = 1024
	def __init__(self, file):
		self.w = wave.open(file, "rb")
		self.p = pyaudio.PyAudio()
		self.stream = self.p.open(
			format = self.p.get_format_from_width(self.w.getsampwidth()),
            		channels = self.w.getnchannels(),
            		rate = self.w.getframerate(),
            		output = True
		)
	
	def play(self):
        	data = self.w.readframes(self.chunk)
        	while data != '':
            		self.stream.write(data)
            		data = self.w.readframes(self.chunk)
	def close(self):
        	self.stream.close()
        	self.p.terminate()

class startgui():
	audio = Audio("alert.wav")
	audio.play()
	easygui.msgbox("Warning! ARP-Issues detected. You may have been comprimised via Man-in-the-middle-Attack.", title="Warning!", image = "pic.gif")
	audio.close()

startgui()