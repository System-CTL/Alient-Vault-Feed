import os

path_to_script = os.path.dirname(os.path.abspath(__file__))
clean_fullpath=path_to_script+"\\Your_Company_Env_Hashes.txt"

with open(clean_fullpath, 'rt') as clean_hashes:
    clean_array=[]
    lines=clean_hashes.readlines()
    for line in lines: 
        sline=line.strip()
        clean_array.append(sline)

print("==========================================================================================================")
print("==========================================================================================================")
print("==========================================================================================================")
mali_fullpath=path_to_script+"\\Malicious_Feed_From_OTX.txt"

with open(mali_fullpath, 'rt') as malcious_hashes:
    mali_array=[]
    lines=malcious_hashes.readlines()
    for line in lines: 
        sline=line.strip()
        mali_array.append(sline)
#print(mali_array)
print("==========================================================================================================")
print("==========================================================================================================")
print("==========================================================================================================")
print("==========================================================================================================")
print("==========================================================================================================")
print("==========================================================================================================")
#set intersection for comparing common-one from two sets(two files)
print(list(set(clean_array) & set(mali_array)))

find=[a for a, b in zip(clean_array, mali_array) if a==b ]
print("Print Only Common hashes in both file - if it return empty then your enviroment is safe notthing match with OTX feed")
print(find)


print("===========================================================================================================")
print("For Surety we reverse the order of files ")

#in opposite direction
print(list(set(mali_array) & set(clean_array)))

find=[a for a, b in zip(mali_array, clean_array) if a==b ]
print(find)


