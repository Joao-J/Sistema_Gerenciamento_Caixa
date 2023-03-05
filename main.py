import yaml

bd = []

class banco_dados:

	global bd

	def importar():
		try:
			with open('bd.yml','r') as file:
				bd = yaml.safe_load(file)
		except:
			open('bd.yml','x')
		print('banco de dados: OK')

	def update(value):
		bd.append(value)
		print(bd)
		with open('bd.yml','w') as file:
			yaml.dump(bd,file)
		print('banco de dados: Atualizado')
		return(bd)


class main:
	def __init__(self):
		b = banco_dados
		b.importar()
		print(b.update({'Nome':'maria','Quantidade':2,'Valor':2.80}))


main()
