import time

#1 calificaciones

#?luis calificaciones
luis_matrix = 4
luis_frozen = 2

#?Ana calificaciones
ana_matrix = 5
ana_frozen = None
#?Calificaciones conocidas

#! paso#1 calcular la similitud entre Ana(u) y luis(v)
numerador = luis_matrix * ana_matrix
denominador = ((ana_matrix**2)**0.5)*((luis_matrix**2)**0.5)
similitud = numerador/denominador

#! calcular la prediccion para calcular la calificacion de ana para frozen
prediccion = (similitud * luis_frozen) / similitud

#!Mostrar resultados
print("Similitud Ana_Luis: ", (similitud,2)) #!Round redondea valores muy grandes de decimales
print("Prediccion de ana para frozen: ", round(similitud,2))