sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}




# for key in sample_dict:
#  print(f'{key:<10} = {sample_dict[key]:>10}')
# for k, v in sample_dict.items():
#  print(f'{k:<10} = {v:>10}')

L = ['age', 'name']
D={}
i=0
while i<len(L):
    if L[i] in sample_dict.keys():
        D[L[i]]=sample_dict[L[i]]
    i+=1
print(D)

if "Jones" in sample_dict.values():
    print("Wartość Jones występuje")
else:
    print("Nie występuje")


# for k in L:
#     del sample_dict[k]
# print(sample_dict)



# sample_dict = {
#  "name": "Kelly",
#  "surname": "Jones",
#  "age": 25,
#  "salary": 8000,
#  "city": "New york"}
# for key in sample_dict:
#  print(f"{key:<10}={sample_dict[key]:>10}")
# L=['age','name']
# D={}
# for k in L:
#  if k in sample_dict.keys():
#   D[k]=sample_dict[k]
# print(D)