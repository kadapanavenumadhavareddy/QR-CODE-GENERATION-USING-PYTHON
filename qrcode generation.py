#first we need install the pyqrcode and pypng packages
#------------commands for installing the above packages in windows--------------
#pip install pyqrcode
#pip install pypng
import pyqrcode#this command is used to import the pyqrcode package 
number = pyqrcode.create("type the message which you want")#this command is used to create a qrcode and assign to variable name number
number.png('venu2.png',scale=8)#this command is used to save the qrcode with name venu and save on the folder where this program source code is saved



