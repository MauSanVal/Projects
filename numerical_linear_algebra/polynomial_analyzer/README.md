# Polynomial Analyzer

Una suite modular desarrollada en Python para el análisis cuantitativo, cualitativo y gráfico de funciones polinómicas.

##  Funcionalidades

- **Parseo de expresiones:** Procesamiento y validación de expresiones polinomiales en formato texto.
- **Análisis de dominio:** Evaluación del dominio de definición en el conjunto de los números reales ($\mathbb{R}$).
- **Cálculo de derivadas:** Obtención explícita de la primera y segunda derivada ($f'(x)$ y $f''(x)$).
- **Cálculo de raíces:** Determinación numérica de las raíces o ceros del polinomio ($f(x) = 0$).
- **Estudio de monotonía:** Análisis de los signos de $f'(x)$ para clasificar intervalos de crecimiento y decrecimiento.
- **Localización de extremos:** Identificación y clasificación de puntos críticos (máximos y mínimos locales/absolutos).
- **Análisis de concavidad:** Evaluación de $f''(x)$ para determinar concavidad hacia arriba, concavidad hacia abajo y puntos de inflexión.
- **Cálculo integral:** Integración definida y cálculo del área bajo la curva en intervalos específicos.
- **Visualización gráfica:** Trazado interactivo de la función resaltando raíces, extremos, inflexiones y regiones de integración.

---

##  Algoritmo QR Implementado y Limitaciones

El cálculo de las raíces en `raices.py` se realiza mediante una **implementación propia del algoritmo QR** aplicado a la matriz compañera del polinomio.

- **Implementación propia:** El método numérico de descomposición QR e iteración para encontrar autovalores fue programado de forma explícita sin recurrir a solucionadores externos de caja negra.
- **Reconocimiento de limitaciones:** Cuando el algoritmo QR no logra converger (debido a raíces múltiples, pares conjugados o mal acondicionamiento numérico), el programa **no converge al cálculo de las raíces**, lo cual se reconoce como una limitación del método numérico seleccionado en esta versión del proyecto.

---

##  Estructura del Repositorio

```text
polynomial_analyzer/
├── main.py          # Orquestador y punto de entrada principal
├── parser_poly.py   # Parseo y sintaxis de expresiones polinomiales
├── dominio.py       # Evaluación del dominio en R
├── derivadas.py     # Cálculo de primera y segunda derivada
├── raices.py        # Implementación del algoritmo QR para raíces
├── crecimiento.py   # Intervalos de monotonía (creciente/decreciente)
├── extremos.py      # Identificación de máximos y mínimos
├── concavidad.py    # Estudio de concavidad y puntos de inflexión
├── integral.py      # Integración definida y áreas
└── grafica.py       # Renderizado gráfico interactivo
