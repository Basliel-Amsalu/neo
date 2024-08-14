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


def write_nodes_and_edges_ratings():
    with open("ml-latest-small/ratings.csv", "r", encoding="utf-8") as r:
        ratings = csv.reader(r)
        next(ratings)  # Skip the header
        for rating_row in ratings:
            user_id = rating_row[0]
            movie_id = rating_row[1]
            rating = rating_row[2]
            timestamp = rating_row[3]
            write_node_and_edge_ratings(user_id, movie_id, rating, timestamp)


def write_node_and_edge_ratings(user_id, movie_id, rating, timestamp):
    with open("output/users.cypher", "a", encoding="utf-8") as u:
        u.write(f"MERGE (:User {{id: {user_id}}});\n")
    with open("output/ratings.cypher", "a", encoding="utf-8") as r:
        r.write(f"MERGE (:Rating {{rating: {rating}, timestamp: {timestamp}}});\n")
    with open("output/edges.cypher", "a", encoding="utf-8") as ed:
        ed.write(
            f"MATCH (u:User {{id: {user_id}}}), (m:Movie {{id: {movie_id}}}), (r:Rating {{rating: {rating}, timestamp: {timestamp}}})\n"
        )
        ed.write(f"MERGE (u)-[:RATED {{timestamp: {timestamp}}}]->(m)\n")
        ed.write(f"MERGE (m)-[:RATED_BY {{timestamp: {timestamp}}}]->(u)\n")
        ed.write(f"MERGE (m)-[:HAS_RATING {{timestamp: {timestamp}}}]->(r)\n")
        ed.write(f"MERGE (u)-[:GAVE_RATING]->(r)\n")
        ed.write(f"MERGE (r)-[:RATED_BY]->(u);\n")


write_nodes_and_edges_ratings()

