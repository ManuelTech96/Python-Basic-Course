# "w" -> write -> overwritting the txt with new text given
# "a" -> append -> add the text to the existing text
with open("archives\\manuel_text.txt", "w", encoding="UTF-8") as archivo:
    #Overwriting the archive
    #archivo.write("Jajajaja te culee")
    
    #aggregating multiple lines with writelines
    archivo.writelines(["Hola manuel que tal estas\n", "Pedo"])