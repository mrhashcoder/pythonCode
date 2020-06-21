# DATA to be used :
data = [
    {"name" : "adam", "age" : 57},
    {"name" : "Batty" , "age" : 21},
    {"name" : "Carlen" , "age" : 42}
]

# Genarating OutPut

for i in range(len(data)):
    print(i+1 , end =" - ")
    print(data[i]["name"], end=" is ")
    print(data[i]["age"])