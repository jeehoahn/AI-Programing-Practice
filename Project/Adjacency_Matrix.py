def create_adjacency_matrix(vertices, edges):
    adjacency_matrix = [[0] * vertices for _ in range(vertices)]

    # Fill the matrix based on the edges
    for edge in edges:
        vertex1, vertex2 = edge
        # Assuming the graph is undirected, so set both entries to 1
        adjacency_matrix[vertex1][vertex2] = 1
        adjacency_matrix[vertex2][vertex1] = 1

    return adjacency_matrix

# Example usage
num_vertices = 5
edge_list = [(0, 1), (0, 3), (1, 2), (2, 4), (3, 4)]
print(type(edge_list[0]))

adj_matrix = create_adjacency_matrix(num_vertices, edge_list)

# Display the adjacency matrix
for row in adj_matrix:
    print(row)
