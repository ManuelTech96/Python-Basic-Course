#if module is in the same package
#import Good_modules.say_hi as m_say_hi

import sys
#To add modules just for this sesion
sys.path.append("F:\\CursoPython\\Good_modules")

import say_hi as m_say_hi

print(m_say_hi.saludar("Pedro"))