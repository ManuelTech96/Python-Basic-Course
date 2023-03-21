#2 lists, one with names, other with surnames
names = ["Manuel", "Pelayo", "Sergio", "Daniel", "Alfonso"]
surnames = ["Lolo", "Pela", "Mendo", "Colo", "Fonso"]

#Register this information in a TXT in optimun way

with open("Simple_file_problems\\names_surnames.txt", "w") as arch:
    arch.writelines("Data is:\n")
    [arch.writelines(f"Name: {n}\nSurname: {a}\n------------\n") for n, a in zip(names, surnames)]