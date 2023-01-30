# SHARK ATTACKS 
![hola](/images/tiburon-salta-agua.jpg)

## Un proyecto sobre Pandas realizado en la escuela Ironhack en el que analizamos los ataques de tiburones partiendo de una base de datos de [Kaggle][Kaggle].

#### Procedimiento:

##### 1. Limpieza de datos.
##### 2. Hipótesis
##### 3. Conclusiones

A continuación, se detalla el procedimiento que se ha seguido para llevar a cabo ambos objetivos:

##### 1. Limpieza de datos.

En primer lugar, se ha realizado una exploración de los datos para obtener una vision general sobre el dataframe con la dimension y la información sobre el mismo e identificando nulos y duplicados.
Después se procede a la limpieza de esos datos, creando una homogeneidad de los diferentes valores y relacionando algunas columnas comunes, para poder completar aquellos datos ausentes que pueden ser relevantes para la investigación final.

##### 2. Hipótesis.

En el caso de las hipótesis, han sido dos la base de esta investigación:

1. El lugar con mas ataques de tiburones.
2. EL tipo de ataque más frecuente.

##### 3.Conclusiones

Para alcanzar las hipótesis planteadas, se ha procedido a analizar las columnas de mayor interés, que en este caso han sido:

- Tipo de ataque
- País, area y localizaicón
- Actividad acuática realizada
- Tipo de lesión
- Si el daño era mortal o no.

Para alcanzar el primer objetivo de este análisis se han obtenido las frecuencias de las columnas relaciondas con la localización de los ataques.

El lugar con más ataques ha resultado ser USA , Florida, New Smyrna Beach, que tras una breve investigación resulta ser conocido como "la capital de los tiburones", donde se concentra una gran cantidad de especies y además es un lugar donde se practican muchos deportes actuaticos como el surf.

En relación al segundo objetivo, se han dividido los datos en tres parámetros: provocado, no provocado e inválido. 
EL dato con mas frecuencia fue el no provocado, relacionado directamente con la moda de la columna actividad acúatica, que sería la práctica del surf.
Y por último como extra, se ha observado que la mayoría de los daños no suelen ser mortales y que las partes del cuerpo más perjudicadas de las víctimas suelen ser las piernas.







[Kaggle]: https://www.kaggle.com/datasets/teajay/global-shark-attacks
