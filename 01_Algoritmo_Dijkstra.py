# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 23:32:06 2023

@author: julia
"""

import sys

# Función para encontrar el vértice con la distancia mínima
def encontrar_vertice_minimo(distancias, visitados):
    min_distancia = sys.maxsize
    min_vertice = None

    for v in range(len(distancias)):
        if distancias[v] < min_distancia and not visitados[v]:
            min_distancia = distancias[v]
            min_vertice = v

    return min_vertice

# Función para imprimir la solución
def imprimir_solucion(distancias):
    print("Vértice \t Distancia desde el vértice fuente")
    for nodo in range(len(distancias)):
        print(nodo, "\t", distancias[nodo])

# Función principal para encontrar la ruta más corta utilizando Dijkstra
def dijkstra(grafo, fuente):
    num_vertices = len(grafo)
    distancias = [sys.maxsize] * num_vertices
    distancias[fuente] = 0
    visitados = [False] * num_vertices

    for _ in range(num_vertices):
        vertice_actual = encontrar_vertice_minimo(distancias, visitados)
        visitados[vertice_actual] = True

        for v in range(num_vertices):
            if (
                not visitados[v]
                and grafo[vertice_actual][v] != 0
                and distancias[vertice_actual] + grafo[vertice_actual][v] < distancias[v]
            ):
                distancias[v] = distancias[vertice_actual] + grafo[vertice_actual][v]

    imprimir_solucion(distancias)

# Ejemplo de uso
grafo_ejemplo = [
    [0, 2, 0, 0, 0, 3],
    [2, 0, 4, 0, 0, 0],
    [0, 4, 0, 5, 0, 0],
    [0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [3, 0, 0, 0, 1, 0],
]

fuente = 0
dijkstra(grafo_ejemplo, fuente)
