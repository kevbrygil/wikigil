# Reto Arboles Binarios

```
Decidí usar Java porque es un lenguaje multiplataforma, se puede usar una sola aplicación
que puede ser usada, ya sea Windows, Mac o Linux y no se tendría que usar licencia porque es
Open source. Es facil de aprender gracias a herramientas de desarrollo amplios. Ademas que es
orientado a objetos por lo que es facil crear aplicaciones modulares y reutilizar partes de
la misma
```

### Instalación

Unicamente basta con tener instala Java SDK 11.
En este repositorio contiene 3 archivos con extension .java:

#### BottomViewTreePreOrder.java
#### BottomViewTreeInOrder.java
#### BottomViewTreePostOrder.java

Ambas se corren individualmente y arrojan el resultado de la vista inferios por el tipo de 
recorrido en particular del arbol binario. 
Se compilaron y ejecutaron de la siguiente manera:

```
javac BottomViewTreePreOrder.java
java BottomViewTreePreOrder

OUTPUT: The Bottom View of Binary Tree by Preorder is: 
        0 1 3 6 8 9 
```

```
javac BottomViewTreeInOrder.java
java BottomViewTreeInOrder

OUTPUT: The Bottom View of Binary Tree by Inorder is: 
        0 1 3 6 8 9 
```
```
javac BottomViewTreePostOrder.java
java BottomViewTreePostOrder

OUTPUT: The Bottom View of Binary Tree by Postorder is: 
        0 1 3 5 7 9 
```

### Resultado del problema por tipo de recorrido del Arbol

```
**Inorder** 
Recorrido: 0 1 3 4 5 6 7 8 9
Vista inferior del arbol binario: 0 1 3 6 8 9

**Preorder** 
Recorrido: 0 1 3 4 5 6 7 8 9
Vista inferior del arbol binario: 0 1 3 6 8 9

**Postorder**
Recorrido: 0 1 4 3 6 8 9 7 5
Vista inferior del arbol binario: 0 1 3 5 7 9
```

### Análisis y solución del problema

Tiempo de Complejidad: 
Al analizar la complejidad de tiempo de nuestro enfoque, vemos que el orden de nivel 
transversal de todos los nodos requiere O (n) tiempo. Junto con esto, cada inserción 
en nuestro mapa toma O (log n)  tiempo. Entonces, la Complejidad de tiempo total será 
 O (n * log n) .

Al analizar la complejidad de tiempo, el orden de nivel de recorrido de todos los nodos
requiere **O (n)** de tiempo, sumando con esto, cada insercion de nuestro mapa toma 
**O (log n)**  tiempo, entonces, la complejidad de tiempo total es O ***(n * log n)***.

Complejidad espacial:   
Se usó cola y pila donde se almacenan todos los nodos presentes en los niveles, por lo 
tanto, el espacio requerido por nuestro mapa es menor que la cola o pila usada, entonces,
nuestra complegidad general del espacio es **O (n)**