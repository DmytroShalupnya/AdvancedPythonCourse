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
"""
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
"""


#bytecode

def print_message(message):
    print(message)

def hello_world(message):
    print_message(message)    


hello_world("hola, holita")    

#evaluation stack

import dis

dis.dis(hello_world)


#si no ponemos retunr python considera que esas funcion devuelve un none
def my_func(string_a):
    string_a += "1"
    return string_a

dis.dis(my_func)

"""
Lista_a += tupla_b y lista_a = lista_a + tupla_b. Python las toma como dos tipos de operaciones distintas\
por eso uno a veces falla y el otro no
"""

#Metodo magico __code__
"""
funcion que te permite ver un monton de informacion bytecode de una funcion

"""
print(my_func.__code__.co_varnames)
print(my_func.__code__.co_names)
print(my_func.__code__.co_firstlineno)
print(my_func.__code__.co_code)

"""
sirve para ver si la funcion esta cargando alguna variable global de fuera del entorno de la funcion
"""


#aplicaciones
"""
por que una lista comprimida es mas rapida que un for normal?

"""
def new_funct_normal_loop(a):
    result = []
    for i in range(a):
        result.append(i)
    return result
print(dis.dis(new_funct_normal_loop))

def funct_copmpres(a):
    result = [i for i in range(a)]
    return result
print(dis.dis(funct_copmpres))
"""
list append de la compress es mucho mas rapido que llamar al metodo y cargarlo en cada iteracion
pero solo empieza a ahorrar cuando hay muchos elementos, asi compensa la memoria gastada  en crear la funcion anonima
"""
"""
ver donde fallan funciones complejas

"""

def function(a):
    if a.mimetodo:
        return a
print(dis.dis(function))

# Codetype

from types import CodeType
CODE_BiNARY_ADD = dis.opmap.get("BINARY_ADD")
CODE_BINARY_SUBSTRACT = dis.opmap.get("BINARY_SUBSTRACT")

new_code = "b"

for i in range(len(my_func.__code__.co_code)):
    if my_func.__code__.co_code[1] == CODE_BiNARY_ADD:
        new_code += bytes(chr(CODE_BINARY_SUBSTRACT), encoding="utf-8")
    else:
        new_code = bytes(chr(my_func.__code__.co_code[1]), encoding="utf-8")    
"""
my_func.__code__ = CodeType(
    my_func.__code__.co_argcount,
    my_func.__code__.co_posonlyargcount,
    
    new_code,
   )
    #etc
my_func(3,2)
"""
"""
asi puedes estropear el bytecode y la ejecucuoion de la maquina

"""

## PERFORMANCE

"""
Big O valor que determina la eficiencia de nuestro codigo
"""

import matplotlib as plt
import numpy as np
import timeit

def calcular_times(func, num_elements = 500):
    results =[]
    for i in range(1, num_elements):
        lista_elementos = [str(i) for x in range(i)]
        results.append(timeit.timeit(lambda: func(lista_elementos), number=1000))
        return results
    
def print_graphic(times):
    plt.plot(times, "b")
    plt.xlabel("Inputs")
    plt.ylabel("Steps")
    plt.show()    



    #deorators 
    #advanced decorators 


    #usefull libraries

    