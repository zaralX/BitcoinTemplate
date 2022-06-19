import math
import random
from time import sleep

##############################################################################
#                           SETTINGS                                         #

__rule_btc_pos_count = 100 # count points for connect
__rule_btc_size = 16 # len point
__rule_btc_count_max = 1.0 # ONLY IN FLOAT (.0) # max bitcoin in point
__rule_btc_pass_count = 16 # count of passwords in point (hard < __rule_btc_pass_count < easy)
__rule_btc_pass_size = 3 # size of password in point
pas_chars = '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ' # all characters for point name and password

#                                                                            #
##############################################################################

btc_positions = {} # idk why me added this :D

def Generate_btc(_r_max, _r_scatter, _r_count_max, _r_pass_count, _r_pass_size): # function for generate points
	generated_positions = []
	generated_output = {}
	for position in range(_r_max):
		generated_pos = ''
		for new_pos in range(_r_scatter):
			generated_pos += random.choice(list(pas_chars))
		stop = False # просто создание переменной
		for i in generated_positions:
			if generated_pos == i:
				stop = True
			else:
				stop = False
		if stop == False:
			generated_positions.append(generated_pos)
			passwords = []
			for i in range(_r_pass_count):
				addpass = ''
				for a in range(_r_pass_size):
					addpass += random.choice(list(pas_chars))
				stop = False # просто создание переменной
				for i in passwords:
					if generated_pos == i:
						stop = True
					else:
						stop = False
				if stop == False:
					passwords.append(addpass)

			generated_output[generated_pos] = {'passwords' : passwords, 'count' : random.uniform(0.0, _r_count_max)} # проблема тут, это добавлени е в словарь
			a+=1
			print(f'Генерация точек [{a}/{_r_max}]')
	return generated_output
	

out = Generate_btc(__rule_btc_pos_count, __rule_btc_size, __rule_btc_count_max, __rule_btc_pass_count, __rule_btc_pass_size)
input('Нажмите для выравнивания')
for i in out:
	print(f'\n\n   Подключена точка: {i}')
	print(f'   Баланс          ')
	print('                 '+str(out[i]['count']))
	print(f'   Пароли          ')
	for x in out[i]['passwords']:
		print(f'                 {x}          ')

login = input('Введите логин: ')
login_balance = 0

while True:
	gen_connect = ''
	for connect_pos in range(__rule_btc_size):
		gen_connect += random.choice(list(pas_chars))
	print(f'Подключаемся к {gen_connect}..')
	sleep(1)
	finded=False
	for i in out:
		if i == gen_connect:
			finded=True
	if finded == True:
		print('  Статус: True')
		print('  Подбираем пароль..')
		sleep(1)
		gen_connect_pass = ''
		for connect_pas in range(__rule_btc_size):
			gen_connect_pass += random.choice(list(pas_chars))
		for i in out[gen_connect]['passwords']:
			if i == gen_connect_pass:
				finded_pass=True
		if finded_pass == True:
			print('    Статус: True')
			print('    Добываем..')
			sleep(2)
			balance = out[gen_connect]['count']
			give = random.uniform(0.0, balance/2)
			print(f'      Добыто {give} из ячейки {gen_connect}')
			login_balance += give
		else:
			print('    Статус: False')
	else:
		print('  Статус: False')
	print("\nReloading..")
	sleep(5)
