# Neo4j node and edge writer for movie recommender system

## Description

This project helps write neo4j querie to create nodes and edges extracted from movie datasets in csv format.
it has multiple functions to help with the extraction

- `write_nodes_and_edges_movies`: iterates over the rows of the movies.csv data and pass the values of the row for the write_node_and _edge_movies function.

- `write_node_and_edge_movies`: takes the row data from the movies.csv and use it to write a neo4j query to create a movie node, genre node and edge(relationship between nodes) between a movie and a genre and writes the queries on the `movies.cypher, genres.cypher and edges.cypher` files.

- `write_nodes_and_edges_ratings`: iterates over the rows of the rating.csv and pass the values of the row for the write_node_and_edge_ratings funciton.

- `write_node_and_edge_ratings`: takes the row data from the rating.csv and use it to write a neo4j query to create a user node, rating node and edge between a movie and a rating, a user and a rating and a user and a movie. then it writes them on the `ratings.cypher, user.cypher and edges.cypher` files.

- `write_nodes_and_edges_tags`: iterates over the rows of the tags.csv and pass the values of the row for the write_node_and_edge_tags function.
- `write_node_and_edge_tags`: takes the row data from the tags.csv and use it to write a neo4j query to create a tag node and additional user nodes and edge between movies and tags and movies and users and users and tags. then it writes them onto the `tags.cypher, users.cypher and edges.cypher` files.

because the data has no separate user data the userid columns from the tags.csv and rating.csv were used to create a user node and to avoid creating redundant nodes and edges a `MERGE` query instead of `CREATE`.

## Usage

To use this project, follow these steps:

1. Clone the project
2. Run the writer.py program 
`python writer.py` you can choose the function you want to call depending on the queries you want to generate.
3. copy the queries generated into neo4j browser/aura and test out the nodes and the connections.

