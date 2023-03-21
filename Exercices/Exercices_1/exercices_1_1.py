#Common Data
other_courses_min = 2.5
other_courses_max = 7
other_courses_med = 4
this_course = 1.5

crud_medium = 5
this_crud = 3.5


#Diferencia porcentual entre el curso actual y:
#El mas rapido de otros cursos
#El mas lento de otros cursos
#El promedio de otros cursos

min_dif = 100 - this_course / other_courses_min * 100
max_dif = 100 - this_course * 1000 // other_courses_max / 10
med_dif = 100 - this_course / other_courses_med * 100

print("--------------------")

print(f'This courses duration is {min_dif}% less than the other faster course')
print(f'This courses duration is {max_dif}% less than the other slower course')
print(f'This courses duration is {med_dif}% less than the other medium course')

print("--------------------")

#Porcentaje de material inservible que se reduce en:
#El promedio de los cursos
#El curso actual

empty_time_medium = 100 - other_courses_med * 1000 // crud_medium / 10
empty_time_this = 100 - this_course * 1000 // this_crud / 10

print(f'Other courses delete {empty_time_medium}% empty time')
print(f'this course delete {empty_time_this}% empty time')

print("--------------------")

#A cuantas horas de otros cursos equivaldria ver 10 horas de este curso
#A cuantas horas de este curso equilvadria ver 10 horas de otros cursos

hours_other_course = other_courses_med / this_course * 10
hours_this_course = this_course / other_courses_med * 10

print(f'See 10 hours of this course equals to see {round(hours_other_course, 2)} of other courses')
print(f'See 10 hours of other courses equals to see {round(hours_this_course, 2)} of this course')

print("--------------------")