import socket
import cv2
import numpy as np
from PIL import Image

class Steganography:
	def __init__(self):
		self.image = None
		self.data = None
		self.shape = None
		self.host = None
		self.port = None

	def getimage(self,img,data):
		self.image = cv2.imread(img)
		self.shape = self.image.shape
		self.image = self.image.flatten()		
		self.data = data
	#def getdata(self):
		#self.data = str(input('Enter data to hide:'))
		
	def getbinary(self,num):
		binary = ''
		while num>0:
			binary=str(num%2)+binary
			num//=2
		while len(binary)<8:
			binary ='0'+binary
		return binary


	def fit(self,binary,start,end):
		index = 0
		for j in range(start,end-1):
			if binary[index]=='0' and self.image[j]%2==1:
				self.image[j]+=1
			if binary[index]=='1' and self.image[j]%2==0:
				self.image[j]+=1
			index += 1
		

			
	def encode(self):
		index = 0
		for i in range(len(self.data)):
			binary = self.getbinary(ord(self.data[i]))
			self.fit(binary,index,index+9)
			if i!=len(self.data)-1:
				if self.image[index+8]%2==0:
					self.image[index+8]+=1
			else:
				if self.image[index+8]%2==1:
					self.image[index+8]+=1
				
			index = index + 9		
			
			
	def send(self):
		"""s = socket.socket()
		p = int(input('Enter port : '))
		s.bind((socket.gethostname(),p))
		s.listen(5)
		
		c,addr = s.accept()
		self.getimage()
		self.getdata()"""
		self.encode()
		k = [str(i) for i in self.image]

		st = " ".join(k)
		return st

	

	
