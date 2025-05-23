"""
ОСНОВНЫЕ ФОРМУЛЫ КОМБИНАТОРИКИ

1. Пусть слово состоит из k символов и
n1, n2, n3, … nk – количество вариантов для первой, второй, третьей … k-й букв,
Тогда количество возможных комбинаций составит:
S = n1 * n2 * n3 * … * nk

2. Пусть слово состоит из k символов и
n  – количество вариантов для каждой буквы,
Тогда количество возможных комбинаций составит:
S = n * n * n * … * n = nk

3. Пусть слово состоит из k символов, на каждом месте может находиться один из набора n символов,
причем любой символ из набора должен быть использован не более одного раза.
Тогда количество возможных комбинаций составит:
S = n * (n -1) * (n – 2) * (n-k)
При k = n количество возможных комбинаций составит:
S = n * (n -1) * (n – 2) * … * 2 * 1 = n!
"""