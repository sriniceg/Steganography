import socket
import cv2
import numpy as np
from PIL import Image

class Steganography:
	def __init__(self):
		self.image = None
	
		
	
	def getcharacter(self,binary):
		num = 0
		binary = binary[::-1]
		for i in range(len(binary)):
			num += int(binary[i])*(2**i)
		return chr(num)

	
	def defit(self,start,end):
		binary = ''
		for i in range(start,end-1):
			if self.image[i]%2==0:
				binary +='0'
			else:
				binary +='1'
		return binary
			
			
	def decode(self):
		index = 0
		data = ''
		flag = False
		binary = self.defit(index,index+9)
		data += self.getcharacter(binary)
		if self.image[index+8]%2==1:
			flag = True
		while flag:
			index += 9
			binary = self.defit(index,index+9)
			data +=self.getcharacter(binary)
			if self.image[index+8]%2==1:
				flag = True
			else:
				flag = False
		return data
			
				
	def receive(self,st):
		"""s = socket.socket()
		p = int(input('Enter port : '))
		s.connect((socket.gethostname(),p))
		st = s.recv(10000).decode()"""
		k = st.split()
		self.image = [int(i) for i in k]
		return self.decode()

	
