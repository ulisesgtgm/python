"""
Comentarios e impresión en Python

Comentarios:
Los comentarios son texto que Python ignora al ejecutar el programa.
Se usan para documentar, explicar o desactivar código.

Tipos de comentarios:
1. Comentarios de una línea → usan #
2. Comentarios multilínea → varias líneas con #
3. Docstrings → usan triple comillas (""" """ o ''' ''')
   Se usan para documentar funciones, clases o módulos.

Impresión:
La función print() muestra información en la consola.
Permite imprimir texto, variables, resultados y formatos.
"""

# -----------------------------
# Comentarios de una línea
# -----------------------------
# Este es un comentario simple
# Sirve para explicar instrucciones específicas

x = 10  # También se puede comentar al final de una línea


# -----------------------------
# Comentarios multilínea
# -----------------------------
# Se usan varios símbolos #
# cuando queremos explicar
# algo más largo sin usar docstrings


# -----------------------------
# Docstrings (comentarios formales)
# -----------------------------
"""
Este es un docstring.
Se usa en funciones, clases o módulos.
Python sí lo reconoce como documentación interna.
"""


# -----------------------------
# Impresión básica
# -----------------------------
print("Hola mundo")  # Imprime texto

nombre = "Ulises"
print(nombre)  # Imprime una variable


# -----------------------------
# Imprimir múltiples valores
# -----------------------------
edad = 25
print("Nombre:", nombre, "Edad:", edad)


# -----------------------------
# Imprimir resultados
# -----------------------------
a = 5
b = 3
print("Suma:", a + b)


# -----------------------------
# Separadores y formato simple
# -----------------------------
print("Python", "es", "genial", sep="-")  # Cambia el separador
print("Linea 1\nLinea 2")  # Salto de línea