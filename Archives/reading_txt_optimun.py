#More optimun, less exception errors, more simplyfied, less line codes
#Same, but cheaper

#opening archive
with open("archives\\manuel_text.txt", encoding="UTF-8") as archivo:
    
    #reading and showing the archive
    print(archivo.read())
    
#Not needed it to close the file due to use with open