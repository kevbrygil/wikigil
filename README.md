# Reto Arboles Binarios

```
Decidí usar Java porque es un lenguaje multiplataforma, se puede tener una sola aplicación y
ser usada en diferentes sistemas operativos, ya sea Windows, Mac o Linux y no se tendría que 
usar licencia porque es Open source. Es facil de aprender gracias a sus herramientas de 
desarrollo muy amplios. Ademas que es orientado a objetos por lo que es facil de crear 
aplicaciones modulares y reutilizar partes de la misma.
```

### Instalación

Tener instalado Java SDK 11.
El sistema operativo empleado fue Linux Ubuntu, aunque puede ser cualquier sistema operativo, 
ya que como comentamos anteriormente, java tiene la caracteristica de ser multiplataforma.
En este repositorio github se almacenan 3 archivos con extension .java:

**TreePreOrder.java**
**TreeInOrder.java**
**TreePostOrder.java**

Ambas se corren individualmente y arrojan el resultado de la vista inferior separados por el 
tipo de recorrido del arbol binario(Inorder,Preorder y Postorder).
Se compilaron, ejecutaron y se probaron de la siguiente manera:

```
javac TreePreOrder.java
java TreePreOrder

OUTPUT: The Bottom View of Binary Tree by Preorder is: 
        0 1 3 6 8 9 
```

```
javac TreeInOrder.java
java TreeInOrder

OUTPUT: The Bottom View of Binary Tree by Inorder is: 
        0 1 3 6 8 9 
```
```
javac TreePostOrder.java
java TreePostOrder

OUTPUT: The Bottom View of Binary Tree by Postorder is: 
        0 1 3 5 7 9 
```

### Resultado del problema por tipo de recorrido del Arbol

```
**Inorder** 
Recorrido: 0 1 3 4 5 6 7 8 9
Vista inferior del arbol binario: 0 1 3 6 8 9

**Preorder** 
Recorrido: 5 3 1 0 4 7 6 9 8
Vista inferior del arbol binario: 0 1 3 6 8 9

**Postorder**
Recorrido: 0 1 4 3 6 8 9 7 5
Vista inferior del arbol binario: 0 1 3 5 7 9
```

### Análisis y solución del problema

**Tiempo de Complejidad:**
Al analizar la complejidad de tiempo, el orden de nivel de recorrido de todos los nodos
requiere **O (n)** de tiempo, sumando con esto, cada insercion de nuestro mapa toma 
**O (log n)**  tiempo, entonces, la complejidad de tiempo total es O ***(n * log n)***.

**Complejidad espacial:**
Se usan colas y pilas donde se almacenan todos los nodos presentes en los niveles, por lo 
lo cual, el espacio requerido por nuestro mapa es menor que dicha cola o pila usada, entonces,
nuestra complegidad general del espacio será **O (n)**.