import random
#import hashlib
import plivo
from .constant import Constant

def get_random_number():
	characters2='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	otp=''
 	n2=5
	for i in range(0,n2):
		num2=random.randint(0,len(characters2)-1)
		otp=otp+characters2[num2]
	#otp_first=hashlib.sha1(otp).hexdigest()
	#random_number=hashlib.md5(otp_first).hexdigest()
	return otp

def send_sms(text, phone_number):
	#print(Constant.plivo_auth_id)
	#return Constant.plivo_auth_id
	p = plivo.RestAPI('MAMZRJZMMWM2RLNTG2MD','ZWZlZTA2YTZkZjEzNmJjZmFmYjQyYTc3NGY0NDU4')
	params = {
		'src': 'KIET-ERP',
		'dst': '+91' + str(phone_number),
		'text': text
	}
	p.send_message(params)