archive_not_reading = open("archives\\manuel_text.txt", encoding="UTF-8")

#reading complete archive
#archive = archive_not_reading.read()

#reading archive line by line
#lines = archive_not_reading.readlines()

#reading one line of the archive
line = archive_not_reading.readline()

#Closing archive
archive_not_reading.close()

print(line)
