import csv


def write_nodes_and_edges_movies():
    with open("ml-latest-small/movies.csv", "r", encoding="utf-8") as m:
        movies = csv.reader(m)
        next(movies)  # Skip the header
        for movie_row in movies:
            id = movie_row[0]
            title = movie_row[1]
            genres = movie_row[2]
            write_node_and_edge_movies(id, title, genres)


def write_node_and_edge_movies(id, title, genres):
    with open("output/movies.cypher", "a", encoding="utf-8") as m:
        m.write(f'MERGE (:Movie {{id: {id}, title: "{title}"}});\n')

    genre_list = genres.split("|")
    with open("output/genres.cypher", "a", encoding="utf-8") as g:
        for genre in genre_list:
            g.write(f'MERGE (:Genre {{name: "{genre}"}});\n')
    with open("output/edges.cypher", "a", encoding="utf-8") as ed:
        for genre in genre_list:
            ed.write(f'MATCH (m:Movie {{id: {id}}}), (g:Genre {{name: "{genre}"}})\n')
            ed.write(f"MERGE (m)-[:HAS_GENRE]->(g);\n")


# Run the function
write_nodes_and_edges_movies()


