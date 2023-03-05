import yaml

bd = []

class banco_dados:

	def importar():
		global bd
		try:
			with open('bd.yml','r') as file:
				bd = yaml.safe_load(file)
		except:
			open('bd.yml','x')
		print('banco de dados: OK')

	def update(value):
		global bd
		if value != None:
			bd.append(value)
		with open('bd.yml','w') as file:
			yaml.dump(bd,file)
		print('banco de dados: Atualizado')
		return(bd)

	def delet(value):
		global bd
		if value == '*':
			bd = []
		else:
			onde,valor = value.split(',')
			for i in bd:
				if i[onde] == valor:
					bd.remove(i)
		print(banco_dados.update(None))

	def update_values(value):
		global bd
		if  value.count(',') == 2:
			onde,valor,nvalue = value.split(',')
			try:
				bd[int(onde)-1][valor] = nvalue
			except:
				for i in bd:
					if str(i[onde]) == valor:
						bd[bd.index(i)][onde] = type(i[onde])(nvalue)
		print(banco_dados.update(None))
