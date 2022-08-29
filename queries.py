#regresa un diccionario con todas las succursales enn una variable llamada branches
branches = Branch.objects.all() 
print(branches.fisrt())



firstBranch = Branch.objects.first()
lastBranch = Branch.objects.last()


# Retorna un valor por nombre
ba = Branch.objects.get(name="Barceloneta")

# Retorna un valor por id
brID = Branch.objects.get(id=2)



class ParentModel(models.Model):
  name = models.CharField()

class ChildModel(models.Model):
  parent = models.ForeignKey(ParenModel)
  name = models.CharField()

parent = ParentModel.objects.first()
#Retorna todos los child relacionados al parent
parent.childmodel_set.all()