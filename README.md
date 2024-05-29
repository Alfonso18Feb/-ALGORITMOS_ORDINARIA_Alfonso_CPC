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


# **Sucesión de Fibonacci:** Se trata en sumar los primeros dos digitos anteriores.
Por ejemplo, si tenemos una sucesion de 1,2 el siguiente numero seria las suma de ambos que serai 3
por ejemplo si queremos hacer una lista pues empezariamos con el indice 0 donde te devolveria el 0
El indice 1 que te devolveria el 1
Pero en el indice 2 como es mayor de uno tenemos que sumar 1+0: (2-1)+(2-2)
Esto seguria siendo 3: 2+1:(3-1)+1+0=3
En este progrma podemos ver que esta sucesion se cumple en todos los valores aunque hay un error de recursividad si  superas n=30
## El programa coje un numero entero  n que luego lo pasamos por la funcion recursiva Fibonacci que si es n>1 te devuelve una funcion recursiva que es: fibonacci(n-1) + fibonacci(n-2)
