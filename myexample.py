my_dict = {"key1":200, "Key2":"Hello", "Key3":{"InKey1":150, "InKey2":"Bye"}}
print(my_dict["key1"])
print(my_dict["Key3"]["InKey2"])

my_dict["key4"] = "New_value"
print(my_dict)
# my_dict.values() ##Comprobar que funciona en otro entorno
my_dict2 = {"keyA": 150, "keyB": "Bye"}
print(my_dict2["keyA"])

#Suma de dos valores del diccionario 1 y 2
suma = my_dict["key1"] + my_dict2["keyA"]
print("la suma es ", suma)