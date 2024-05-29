# -ALGORITMOS_ORDINARIA_Alfonso_CPC


# **Bubble sort:** [41,33,17,80,61]

LO primero que hace e codigo sera mirar por pares la lista anterior.
Donde, 41>31 se intercambiaran de posiciones(indices).
Siendo [33,41,17,80,61]
Luego comparan 41>17 como 41 sigue siendo mayor que 17 entonces se cambian de posicion.
Siendo [33,17,41,80,61]
Despues comparamos la siguiente iteracion 41<80. Como aqui el mayor ya esta en un indice mayor se queda igual la lista.
Siendo [33,17,41,80,61]
Por ultimo, comparamos los ultimos dos indices 80>61 como 81 es mayor que 60 permulamos los valores.
Ya terminado la primera iteracion se vuelve a repetir la lista para seguir comparando como dicho anteriormente.
Los que esten en un indice menor y sean mayores que el indice i+1 entonces los cambiamos de posicion.
Si no los dejamos en su posicion y pasamos al siguiente par.
Esto hasta lllegar a ordenarlo así: [17,33,41,61,80]


