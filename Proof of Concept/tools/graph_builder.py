import os
import pickle
import networkx as nx
import matplotlib.pyplot as plt

GRAPH_PATH = "graph_store/security_graph.gpickle"

def update_graph(entity_dict: dict):
    G = load_graph()

    # add nodes by type
    for category, items in entity_dict.items():
        for item in items:
            G.add_node(item, type=category)

    # add edges by co-occurrence
    for items in entity_dict.values():
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                G.add_edge(items[i], items[j], relation="co-occurrence")

    save_graph(G)

def load_graph():
    if os.path.exists(GRAPH_PATH):
        with open(GRAPH_PATH, "rb") as f:
            return pickle.load(f)
    return nx.Graph()

def save_graph(G):
    with open(GRAPH_PATH, "wb") as f:
        pickle.dump(G, f)

def show_graph():
    if not os.path.exists(GRAPH_PATH):
        print("⚠️ No graph file found yet.")
        return

    G = load_graph()
    pos = nx.spring_layout(G)

    # node color by type
    types = nx.get_node_attributes(G, 'type')
    color_map = {
        'people': 'skyblue',
        'orgs': 'lightgreen',
        'locations': 'orange',
        'crimes': 'salmon'
    }
    node_colors = [color_map.get(types.get(n, ''), 'lightgray') for n in G.nodes()]

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1000, font_size=8)
    plt.title("Entity Relationship Graph")
    plt.show()
