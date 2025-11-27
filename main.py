var = ["hola","adios"]

varMod = var.reverse()

print(varMod)

#### Reference and value

#Paso por referencia

def add_list(my_list,new_value):
    my_list.append(new_value)


the_list =[1,2,3]
add_list(the_list, 4)
add_list(the_list,5)
print(the_list)


list1 = []
list2 =[]
list3 = list1

print(list1 == list2)
print(list1 is list2)
print(list1 is list3)


print("ID lista 1" ,  id(list1))
print("ID lista 1" , id(list2))
print("ID lista 1" , id(list3))

#List 1 and list 3 have the same ID because list 3 its a reference of list 1

#Secuences (lists)

mi_lista= ["primer elemento","segundo elemento", "rtercer elemento","cuarto elemento"]


mi_lista.insert(2,"elemnto pos 3")

mi_lista.remove("rtercer elemento")

print(mi_lista)


##Secuences (tuples)

#namedtuple
import collections

Server = collections.namedtuple("server", ("ip","hostname"))
my_server = Server(ip="192.186.1.1", hostname="mi_servidor")
print(my_server.ip)
print(my_server.hostname)

Yo = collections.namedtuple("Apellidos",("primer","segundo"))
yo_completo = Yo(primer="Shalupnya",segundo="Polishchuk")
print(yo_completo.primer+ " " + yo_completo.segundo)
print(repr(yo_completo))


# Secuences (Sets)


set1 = {1,2,3,4,5,6,7,8,9}
set2 = {4,5,7,9,3,10}
print(set1.intersection(set2))
print(set1 & set2)
print(set1.union(set2))
print(set1.difference(set2))

#decorators



#Dicts
#HASHABLE 

dic = {"primero":"primer elemento", "segundo": "segundo elemento"}

print(dic.get("primer elemento", "default")) # if the element is not found, return none or in this case defautl
dic["tercero"] = "tercer elemento"
print(dic)

deleted = dic.pop("tercero")
print(deleted, dic)
# suma de diccionarios

dic2 = {"cuarto":"cuarto elemento", "quinto":"quinto elemento"}
dic3 = dic.update(dic2)
print(dic3)  
# or

print({**dic, **dic2})

#default dic
from collections import defaultdict
d1 = {}
d1["a"] = 0
d1["a"] += 1
d1["a"] += 1

dic_default = defaultdict(int)
dic_default["c"]
print(dic_default)

#Counter(contador)

from collections import Counter

l = [1,2,3,4,5,6,7,6,7,5,7,8,65]

cont = Counter(l)
print(cont)


#Dict como atributos

class MyDict():
    data = {}
    def __setattr__(self, name, value):
        self.data[name] = value
    def __getattribute__(self, name):
        return self.data[name]

    
my_dict = MyDict()    

my_dict.dima = 5
my_dict.perro = 10
print(my_dict.dima)
