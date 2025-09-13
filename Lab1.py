#!1 calificaciones de usuarios

#1.1 PEPITO
pepito_shrek = 5
pepito_jackass = 5

#1.2 Ramona
ramona_shrek = 1
ramona_jackass = None

#1.3 ALVIN YAKIROTY
alvin_shrek = 4
alvin_jackass = 2

#2 calcular similitud (U,V,W)
numerador = pepito_shrek * ramona_shrek * alvin_shrek
denominador = ((pepito_shrek**2)**0.5)*((ramona_shrek**2)**0.5)*((alvin_shrek**2)**0.5)
similitud = numerador/denominador