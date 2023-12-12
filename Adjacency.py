#  File: Adjacency.py
#  Name: Samanvitha Nukala


import sys

def edge_to_adjacency(edge_list):

    # Dictionary to store which vertices have been visited
    visited_dict = {}
    # Iteration of the adjacency list
    for from_vertex, to_vertex, weight in edge_list:
        # If from_vertex not in dictionary, it will be added
        if from_vertex not in visited_dict:
            visited_dict[from_vertex] = {}
        # The to_vertex is added to dictionary
        # The weight associated with each from and to vertex is added to dictionary
        visited_dict[from_vertex][to_vertex] = weight

    # List of unvisited vertices
    new_vertices = []
    # If vertex is not in new_vertices list, it will be added
    for weighted_edge in edge_list:
        for vertices in weighted_edge[:2]:
            if vertices not in new_vertices:
                new_vertices.append(vertices)

    # Adjacency matrix
    adjacency_matrix = []
    # The vertices are iterated through
    for from_vertex in new_vertices:
        matrix_row = []
        for to_vertex in new_vertices:
            # If vertices are visited and have weight it will be added in matrix
            if from_vertex in visited_dict:
                if to_vertex in visited_dict[from_vertex]:
                    key = visited_dict[from_vertex][to_vertex]
                    matrix_row.append(key)
                # If vertices have no weight it will be added to matrix as 0
                else:
                    key = 0
                    matrix_row.append(key)

        adjacency_matrix.append(matrix_row)

    return adjacency_matrix

# remove formatting and convert to list of tokens
# do not change this method
def clean(text):
    text = text.strip()
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace("”", "")
    text = text.replace(" ", "")
    text = text.replace("\"", "")
    text = text.split(",")
    return text

# Debug flag - set to False before submitting
debug = False
if debug:
    in_data = open('adjacency.in')
else:
    in_data = sys.stdin

# get line of input, remove formatting, convert to list of tokens
input_text = in_data.readline()
input_text = clean(input_text)

# convert one string to 2D list of edge data
edges = []
for i in range(0, len(input_text), 3):
    newList = [input_text[i], input_text[i+1], int(input_text[i+2])]
    edges.append(newList)

# convert the 2D list to an adjacency matrix
adj_matrix = edge_to_adjacency(edges)

print('\n'.join([' '.join([str(cell) for cell in row]) for row in adj_matrix]))
