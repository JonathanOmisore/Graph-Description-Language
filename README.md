The Graph Description Language is a domain-specific language for graph theory. Below is the BNF definition of the language

```
<program> ::= <statement> | <statement> <program>

<statement> ::= <create_graph> 
              | <add_vertex>
              | <add_edge>
              | <neighbors>
              | <is_connected>
              | <is_empty>
              | <degree_of>
              | <all_vertices>

<create_graph> ::= "create graph" <graph_name>
<add_vertex> ::= "add vertex" <vertex_name> "to" <graph_name>
<add_edge> ::= "add edge" <vertex_name> "to" <vertex_name> "in" <graph_name>
<neighbors> ::= "neighbors of" <vertex_name> "in" <graph_name>
<is_connected> ::= "is connected" <vertex_name> "to" <vertex_name> "in" <graph_name>
<is_empty> ::= "is empty" <graph_name>
<degree_of> ::= "degree of" <vertex_name> "in" <graph_name>
<all_vertices> ::= "all vertices in" <graph_name>

<graph_name> ::= <identifier>
<vertex_name> ::= <identifier>
<identifier> ::= <letter> | <letter> <identifier>
<letter> ::= "a" | "b" | "c" | ... | "z" | "A" | "B" | "C" | ... | "Z"
```
