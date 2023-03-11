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
		print('CONSULTAR\n')
		for i in db.bd:
			print('id: ',(db.bd.index(i)+1),'\tPRODUTO: ',i['Nome'],'   \tQUANTIDADE: ',i['Quantidade'],'   \tVALOR: ',i['Valor'])
		input('\nPress ENTER for continue\n')

	def cadastrar():
		produto = {'Nome':'','Quantidade':0,'Valor':0.0}
		textos = ['informe o nome do produto: ','Informe a quantidade de produto: ','Informe o valor: ']
		tentativas = 3
		infor = []
		print('CADASTRO\n')
		for i, key in enumerate(produto.keys()):
			while True:
				if tentativas == 0:
					break
				try:
					produto[key] = type(produto[key])(input(textos[i]))
					tentativas = 3
					break
				except:
					print('Tipo de dado não condiz com o esperado')
					while True:
						if tentativas == 0:
							break
						try:
							x = int(input('Vamos tentar novamente: 1-Sim 2-Não'))
							if x == 1:
								break
							elif x == 2:
								tentativas = 0
								break
							else:
								print('Opção invalida')
								tentativas -= 1
								if tentativas == 0:
									break
						except:
							if tentativas >= 1:
								print(f'Opção invalida. Tentativas restantes: {tentativas}')
								tentativas -= 1
		if tentativas != 0:
			b_d.update(produto)
			print('Produto Cadastrado')
		else:
			print('Cancelado')

		input('\nPress ENTER for continue\n')


	def delet():
		t = True
		while t:
			try:
				clear()
				print('DELETE\n')
				x = int(input('1- deletar por id 2- deletar onde 3- deletar tudo 0- CANCELAR\n'))
				values = 0
				if 0 > x >= 4:
					print('Opção invalida')
					input('\nPress ENTER for continue\n')
					break
				if x == 1:
					try:
						op = int(input('Listar produtos 1- Sim / 2- Não\n'))
						if op == 1:
							main.consultar()
						elif op == 2:
							break
						else:
							print('Opção invalida')
					except:
						print('Opção invalida')
						t = False
						break
					try:
						values = int(input('Digite o id: '))
					except:
						t = False
						break
					b_d.delet('id,' + str(values))
					print('Item deletado')
					input('\nPress ENTER for continue\n')
					t = False
				elif x == 2: #Não esquecer de terminar 
					b_d.delet()
				elif x == 3:
<<<<<<< HEAD
					b_d.delet()
=======
					b_d.delet('*')
				elif x == 0:
					t = false
					break
>>>>>>> a1becfbd774f7b02ec7f7cebb66502f8878201fd
			except:
				print('')

	def __init__(self):
		while True:
			main.clear()
			x = '-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-'
			print(x)
			e = ''
			try:
				e = int(input(f'MENU\n1-consultar\n2-cadastrar\n3-modificar\n4-deletar\n0-SAIR\n{x}\n'))
				if  0 > e >= 5:
					raise
			except:
				print('opção invalida')
				input('Press ENTER for continue\n')
				main()
			main.clear()
			if e == 1:
				main.consultar()
			elif e == 2:
				main.cadastrar()
			#elif e == 3:

			elif e == 4:
				main.delet()
			elif e == 0:
				break

	def cadastrari():
		'''
		b = banco_dados
		b.importar()
		print(b.update({'Nome':'maria','Quantidade':2,'Valor':2.80}))
		print(b.update({'Nome':'ana','Quantidade':5,'Valor':5.90}))
		print(b.update({'Nome':'João','Quantidade':5,'Valor':8.00}))
		b.delet('*')
		b.update_values('1,Nome,maria')
		b.update_values('Quantidade,5,9')
		'''
		print(':D')
main()
