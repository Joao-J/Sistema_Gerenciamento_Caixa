import database as db
import sys,os

b_d = db.banco_dados

class main:
	b_d.importar()
	def clear():
		if sys.platform == 'linux':
			os.system('clear')
		else:
			os.system('cls')

	def consultar():
		for i in db.bd:
			print('id: ',(db.bd.index(i)+1),'\tPRODUTO: ',i['Nome'],'   \tQUANTIDADE: ',i['Quantidade'],'\tVALOR: ',i['Valor'])
		input('\nPress ENTER for continue\n')
		print()

	def __init__(self):
		while True:
			main.clear()
			x = '-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-'
			print(x)
			e = ''
			try:
				e = int(input('MENU\n1-consultar\n2-cadastrar\n3-modificar\n0-SAIR\n'+x+'\n'))
			except:
				print('opção invalida')
				input('Press ENTER for continue\n')
				main()
			main.clear()
			if e == 1:
				main.consultar()
			#elif e == 2:

			#elif e == 3:

			#elif e == 4:
			elif e == 0:
				break

	def cadastrar():
		#b = banco_dados
		#b.importar()
		#print(b.update({'Nome':'maria','Quantidade':2,'Valor':2.80}))
		#print(b.update({'Nome':'ana','Quantidade':5,'Valor':5.90}))
		#print(b.update({'Nome':'João','Quantidade':5,'Valor':8.00}))
		#b.delet('*')
		#b.update_values('1,Nome,maria')
		b.update_values('Quantidade,5,9')

main()
