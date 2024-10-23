import numpy as np

# 1. Einführung in Mathematische Matrizen
print("1. Einführung in Mathematische Matrizen:")
print("Eine Matrix ist ein rechteckiges Zahlenarray, das aus Zeilen und Spalten besteht.")
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Beispielmatrix:\n", matrix)
print("Zeilenanzahl:", matrix.shape[0], "Spaltenanzahl:", matrix.shape[1], "\n")

# Begriffe: Zeile, Spalte, Elemente
print("Eine Matrix besteht aus:")
print("Zeilen:", matrix[0], "-> Dies ist die erste Zeile.")
print("Spalten:", matrix[:, 0], "-> Dies ist die erste Spalte.")
print("Elemente (auch als Koeffizienten bezeichnet):", matrix[0, 0], "-> Dies ist das erste Element.")

# 2. Eigenschaften von Matrizen
print("\n2. Eigenschaften von Matrizen:")
print("Größe: Eine Matrix hat eine Größe, die durch die Anzahl der Zeilen und Spalten beschrieben wird.")
print("Unsere Beispielmatrix ist eine", matrix.shape[0], "x", matrix.shape[1], "Matrix.")

# Symmetrische und antisymmetrische Matrizen
print("\nSymmetrische Matrix: Eine Matrix ist symmetrisch, wenn A = A^T.")
symmetrische_matrix = np.array([[1, 2], [2, 1]])
print("Symmetrische Matrix:\n", symmetrische_matrix)
print("Antisymmetrische Matrix: A ist antisymmetrisch, wenn A = -A^T.")
antisymmetrische_matrix = np.array([[0, 2], [-2, 0]])
print("Antisymmetrische Matrix:\n", antisymmetrische_matrix)

# Rang der Matrix
print("\nRang: Der Rang einer Matrix gibt die Anzahl der linear unabhängigen Zeilen/Spalten an.")
print("Rang der Beispielmatrix:", np.linalg.matrix_rank(matrix))

# Determinante
print("\nDeterminante: Eine Matrix hat eine Determinante, die durch ihre Koeffizienten definiert ist.")
print("Determinante der Beispielmatrix:", np.linalg.det(matrix))

# 3. Relation zwischen Matrizen
print("\n3. Relationen zwischen Matrizen:")
print("Matrizen können gleich sein, wenn alle ihre Elemente übereinstimmen.")
matrix_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Ist matrix gleich matrix_2?:", np.array_equal(matrix, matrix_2))

# 4. Spezielle Matrizen
print("\n4. Spezielle Matrizen:")
print("Quadratische Matrix: Eine Matrix, bei der die Anzahl der Zeilen gleich der Anzahl der Spalten ist.")
quadratische_matrix = np.array([[1, 2], [3, 4]])
print("Quadratische Matrix:\n", quadratische_matrix)

print("\nObere Dreiecksmatrix: Eine Matrix, bei der alle Einträge unterhalb der Hauptdiagonale 0 sind.")
obere_dreiecksmatrix = np.array([[1, 2, 3], [0, 5, 6], [0, 0, 9]])
print("Obere Dreiecksmatrix:\n", obere_dreiecksmatrix)

print("\nDiagonalmatrix: Eine Matrix, bei der alle Nicht-Diagonalelemente 0 sind.")
diagonalmatrix = np.diag([1, 2, 3])
print("Diagonalmatrix:\n", diagonalmatrix)

print("\nEinheitsmatrix: Eine quadratische Matrix, bei der alle Diagonalelemente 1 und alle anderen Elemente 0 sind.")
einheitsmatrix = np.eye(3)
print("Einheitsmatrix:\n", einheitsmatrix)

print("\nNullmatrix: Eine Matrix, bei der alle Elemente 0 sind.")
nullmatrix = np.zeros((3, 3))
print("Nullmatrix:\n", nullmatrix)

# 5. Operationen auf Matrizen
print("\n5. Operationen auf Matrizen:")

# Matrizenaddition
print("\nMatrizenaddition: Zwei Matrizen werden addiert, indem die entsprechenden Elemente addiert werden.")
matrix_A = np.array([[1, 2], [3, 4]])
matrix_B = np.array([[5, 6], [7, 8]])
matrix_add = matrix_A + matrix_B
print("Addition von Matrix A und B:\n", matrix_add)

# Skalarmultiplikation
print("\nSkalarmultiplikation: Jede Komponente der Matrix wird mit einem Skalar multipliziert.")
skalare_matrix = 2 * matrix_A
print("Skalarmultiplikation von Matrix A mit 2:\n", skalare_matrix)

# Matrizenmultiplikation
print("\nMatrizenmultiplikation: Matrixprodukt zweier Matrizen.")
matrix_mult = np.dot(matrix_A, matrix_B)
print("Multiplikation von Matrix A und B:\n", matrix_mult)

# Multiplikation mit der Einheitsmatrix
print("\nMultiplikation mit der Einheitsmatrix:")
print("Ergebnis bleibt gleich:\n", np.dot(matrix_A, np.eye(2)))

# Multiplikation mit der Nullmatrix
print("\nMultiplikation mit der Nullmatrix:")
print("Ergebnis ist immer eine Nullmatrix:\n", np.dot(matrix_A, np.zeros((2, 2))))

# Potenzieren einer Matrix
print("\nPotenzieren einer Matrix:")
matrix_potenz = np.linalg.matrix_power(matrix_A, 2)
print("Matrix A hoch 2:\n", matrix_potenz)

# 6. Berechnung der Determinante
print("\n6. Berechnung der Determinante:")
print("Die Determinante einer Matrix kann mit verschiedenen Methoden berechnet werden.")

# Entwicklungssatz von Laplace
print("\nEntwicklungssatz von Laplace:")
print("Die Determinante der Beispielmatrix kann mit dem Entwicklungssatz von Laplace berechnet werden.")
det_matrix_A = np.linalg.det(matrix_A)
print("Determinante der Matrix A:", det_matrix_A)

# Sarrus-Regel (nur für 3x3-Matrizen)
print("\nSarrus-Regel für 3x3-Matrizen:")
matrix_C = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix C:\n", matrix_C)
print("Die Determinante von Matrix C (mit Sarrus-Regel):", np.linalg.det(matrix_C))

print("\nDas Skript bietet eine Übersicht über Matrizen und ihre Eigenschaften.")
