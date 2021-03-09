# Reto Hash

### Reultado del problema

**HASH**: 468484901136871

**PALABRA**: perseverar

**TIEMPO EMPLEADO**: 3 horas

**FUNCIÓN DESCIFRADOR**:

```
function reverse(hash){
    var hash_next = hash;
    var word = '';
    var dictionary = 'acefimoprstuv';
    for(i = 10; i > 0; i--){
        var letter_index = hash_next % 23;
        word = dictionary[letter_index] + word;
        hash_next = (hash_next - letter_index) / 23;
    }
    return word;
}
```

### Análisis y solución del problema

Luego de analizar la función hash, se llego a la conclusión de que para llegar a la solución tendríamos que realizar una prueba con una cadena en la que podamos probar y descifrar el algoritmo que nos conlleve a la solución del problema. Supongamos que la cadena ha probar es “acemospost”, al llamar a la funcion hash con dicha cadena de entrada, nos devuelve el hash “455777525390946”, en la función podemos observar una cadena de caracteres “acefimoprstuv” descrito como “diccionario” y un algoritmo “seed = (seed * 23 + diccionario.indexOf(x[i]))”, entonces dicha función lo traduce a la cadena “acemospost” en el valor “455777525390946” por medio del algoritmo ciclado. Como primer carácter se tiene la letra “a”, en el diccionario podemos observar que se encuentra en el indice ‘0’, si nos enfocamos en la parte del código: diccionario.indexOf(x[i]), esto retorna la posición del carácter de entrada dentro de la cadena “diccionario”, entonces, podemos deducir que en la primera vuelta del ciclo obtendremos la posición del carácter ‘a’ dentro del diccionario que en este caso es el indice ‘0’. Dicho esto nos podemos dar cuenta como la es que la función trabaja: recibe la cadena “acemospost” y devuelve “455777525390946”. La variable “seed” es calculado por el algoritmo y el diccionario “acefimoprstuv”. 
```
Indices ocupados por la cadena “diccionario”: "a   c   e    f    i    m    o    p    r   s     t     u     v"
					       0   1   2    3    4    5    6    7    8   9     10    11   12
```
Tomando las vueltas del ciclo for dentro de la función, se observó detalladamente el comportamiento del algoritmo, en la cual se obtuvo lo siguiente:
```
[a] 11         *  23  +  0   = 253              =  hashresult1
[c] result1    *  23  +  1   = 5820             =  hashresult2
[e] result2    *  23  +  2   = 133862           =  hashresult3
[m] result3    *  23  +  5   = 3078831          =  hashresult4
[o] result4    *  23  +  6   = 70813119         =  hashresult5
[s] result5    *  23  +  9   = 1628701746       =  hashresult6
[p] result6    *  23  +  7   = 37460140165      =  hashresult7
[o] result7    *  23  +  6   = 861583223801     =  hashresult8
[s] result8    *  23  +  9   = 19816414147432   = hashresult9
[t] result9    *  23  +  10  = 455777525390946  =  hashresult10
```
Hecho esto, podemos observar de la forma mas clara los pasos en la cual se formo el hash. El ciclo va incrementándose tomando cada resultado del anterior y multiplicándolo por 23 y luego sumándolo con el valor del indice obtenido del diccionario en conjunto con la cadena de entrada.

Ahora como siguiente paso fue realizar una función en la cual podamos descifrar la cadena a partir de una entrada hash, es decir, tomando la prueba anterior, poder lograr que un valor inicial hash “455777525390946” devuelva la cadena “acemospost”. 

Como podemos observar el valor hash se obtiene multiplicándolo por 23 y sumándole el indice del diccionario coincidente con el carácter de entrada, entonces, aplicando la ingeniería inversa, el algoritmo descifrador, para que pueda obtener el carácter correcto, necesitaría dividir el hash resultante entre 23 y se le restaría el residuo de esa división. En el problema descrito sabemos que la cadena secreta contiene 10 caracteres por lo que ese seria el contador del ciclo for inverso. Dicho esto, se pudo realizar el algoritmo descifrador que estará dentro del ciclo inverso.


De tal manera que en el primer paso del ciclo, al obtener el residuo de la división del hash resultante por 23 se obtiene un indice de la cadena  diccionario “acefimoprstuv” y lo correspondiente a la ultima letra de la cadena ha descifrar, que en este caso seria la letra ‘t’ y tiene como indice en la cadena diccionario el numero 10. Quedando de la siguiente manera:
```
Formula#1: indice_letra_diccionario = n_resultado_hash % 23
```
Tambien es necesario tomar en cuenta los hash inversos resultantes en cada paso hasta tener la cadena completamente descifrada, para obtener dichos valores, se tuvo que ir en el ultimo paso del ciclo de la funcion hash e ir despejando el hash resultante:
```
result9   *  23  +  10 = 455777525390946  =  hashresult10
```
result9 pasa ha ser al hash n-1 y hashresult10 al hash resultante n
el valor entero que se suma (No 10)  es un indice del diccionario y se obtiene de la Formula#1 descrita anteriormente:
```
( n-1_resultado_hash * 23) +  ( n_resultado_hash % 23) =  n_resultado_hash

Formula#2: n-1_resultado_hash = (n_resultado_hash -  ( n_resultado_hash % 23))/23
```
A continuación se muestra un breve ejemplo de como quedaría de principio a fin el algoritmo descifrador:
```
indice_letra_diccionario = n_resultado_hash % 23
palabra = palabra + diccionario[indice_letra_diccionario]
n-1_resultado_hash = (n_resultante_hash  –  indice_letra_diccionario) / 23 
```
Dicho esto, queda ha destacar que se realizo la función en javascript y se hicieron pruebas en la consola del browser de chromium:

```
function reverse(hash){
    var hash_next = hash;
    var word = '';
    var dictionary = 'acefimoprstuv';
    for(i = 10; i > 0; i--){
        var letter_index = hash_next % 23;
        word = dictionary[letter_index] + word;
        hash_next = (hash_next - letter_index) / 23;
    }
    return word;
}

//reverse(468484901136871)
//output: "perseverar"
```
