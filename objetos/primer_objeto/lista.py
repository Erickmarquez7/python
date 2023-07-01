cosa = list()
cosa.append('python')
cosa.append('Chunk')
cosa.sort()
print(cosa[0])
print(cosa.__getitem__(0))
#Es lo mismo ya que como tal la clase lo invoca y 
#se pasa asi mismo como parametro
print(list.__getitem__(cosa, 0))