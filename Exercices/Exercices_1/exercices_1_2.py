#Teniendo en cuenta que una persona dice aproximadamente 2 palabras por segundo

words_per_sec = 2

flash_words_per_sec = round(words_per_sec + (words_per_sec * 0.3))

# Pedirle al usuario que diga cualuqer texto real y calcular cuanto tardaria en decir esa frase
#Calcular cuantas palabras dijo

message = input("Por favor, introduce una mensaje que quieras calcular: ")

breaking_message = message.split(" ")

count_words_message = len(breaking_message)

time_spend_to_say = float(count_words_message / words_per_sec)

input(f'Your phrase has {count_words_message} words. You will spend {time_spend_to_say} secs on say it.')

#Si se tarda mas de 1 minuto (60 secs) mostrar un mensaje diciendo que el texto es demasiado largo

if(time_spend_to_say > 60.0):
    print("Your text is too long, please, try again with something smaller")
else:
    print("Your message will be send succesfully!")

#Si Flash habla un 30% mas deprisa, cuanto tardaria en decir el mismo mensaje

time_spend_by_flash = float(count_words_message / flash_words_per_sec)

print(f"You took {time_spend_to_say} secs on said something that flash would take {round(time_spend_by_flash, 2)} secs. So sadge")
