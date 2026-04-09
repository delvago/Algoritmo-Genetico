# Algoritmo Genético para Optimización de Funciones

Este repositorio contiene una implementación desde cero de un **Algoritmo Genético (AG)** en Python, diseñado para encontrar el mínimo global de funciones matemáticas complejas. En este caso, el algoritmo está configurado para optimizar la **función Eggholder**.

## 🚀 Descripción del Proyecto

El objetivo es demostrar los principios fundamentales de la computación evolutiva aplicados a la optimización numérica. El código incluye procesos críticos como:
- **Generación de Población:** Creación de individuos aleatorios dentro de un espacio de búsqueda.
- **Codificación Binaria:** Transformación de fenotipos (números enteros) a genotipos (cadenas binarias de 10-11 bits) mediante complemento a dos.
- **Evaluación de Fitness:** Cálculo del desempeño de cada individuo basado en la función objetivo.

### La Función Eggholder
Es una función difícil de optimizar debido a la gran cantidad de mínimos locales que posee.
$$f(x, y) = -(y + 47) \sin\left(\sqrt{|y + \frac{x}{2} + 47|}\right) - x \sin\left(\sqrt{|x - (y + 47)|}\right)$$

## 🛠️ Tecnologías y Dependencias

El proyecto está desarrollado en Python 3 y utiliza las siguientes bibliotecas básicas de ciencia de datos:

*   **NumPy:** Para operaciones matemáticas y manejo de matrices.
*   **Pandas:** Para la gestión de datos de la población.
*   **Matplotlib:** Para la visualización de resultados y convergencia.

Para instalarlas, puedes ejecutar:
```bash
pip install numpy pandas matplotlib
```

## 📂 Estructura del Repositorio

*   `Algoritmo_genetico_ejecutable.py`: Script principal que contiene la lógica de codificación, decodificación y funciones base.
*   `Algoritmo_Genetico.ipynb`: Cuaderno de Jupyter con explicaciones detalladas paso a paso y visualizaciones interactivas.

## 🔧 Funcionamiento Base

El script actualmente implementa la base del algoritmo:
1. **Rango de búsqueda:** $[-512, 512]$.
2. **Codificación:** Los valores se transforman a binario para permitir operaciones genéticas futuras (cruce y mutación) a nivel de bit.
3. **Decodificación:** Permite recuperar el valor numérico original para la evaluación de la función.

## 📝 Notas
Todas las funciones están debidamente comentadas tanto en el script como en el cuaderno para facilitar su comprensión pedagógica.
