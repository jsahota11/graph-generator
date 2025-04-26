from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
import networkx as nx
import random

print("loaded backend")

app = Flask(__name__)
CORS(app)

# for my statics
@app.route('/')
def serve_index():
    return send_from_directory('../frontend', 'index.html')

@app.route('/script.js')
def serve_script():
    return send_from_directory('../frontend', 'script.js')

@app.route('/style.css')
def serve_style():
    return send_from_directory('../frontend', 'style.css')


# actually process the form here
@app.route('/api/data', methods=['POST'])
def process_data():
    data = request.get_json()

    # by construction, absolute default graph is empty
    numVertices = int(data.get("vertices", 0))
    numEdges = int(data.get("edges",0))
    labelType = data.get("label_type", "none")
    directed = data.get("directed", False)
    customLabels = data.get("custom_labels", [])
    customEdges = data.get("custom_edges", [])

    print("data loaded from form")

    # build the graph!!

    G = nx.MultiDiGraph() if directed else nx.MultiGraph()

    # generate the labels
    labels = []
    ASCII = 65

    # user chose integer labels
    if labelType =="numbers":
        labels = [str(i) for i in range(numVertices)]

    # user chose letter labels
    elif labelType == "letters":
        # we need letters
        labels = [chr(ASCII+i) for i in range(numVertices)]

    # user has custom labels
    elif labelType == "custom":
        if len(customLabels)!=numVertices:
            return jsonify({"error": "Number of custom labels must match number of vertices"}), 400
        labels = customLabels

    # none for labels
    else:
        labels = ["" for i in range(numVertices)]

    print("labels chosen based off form")

    
    # adding nodes to G
    for label in labels:
        G.add_node(label)

    # add custom edges
    for edge in customEdges:
        if len(edge) ==2:
            G.add_edge(edge[0], edge[1])

    # add remaining edges if needed
    while G.number_of_edges() < numEdges:
        u = random.choice(labels)
        v = random.choice(labels)

        #might make this also random incase the user wanted a digraph, but i dont care for now
        G.add_edge(u,v)

    print("graph built from form")

    
    print("now returning json nodes and edges")
    # return the graph data
    return jsonify({
        "nodes" : list(G.nodes),
        "edges" : list(G.edges)
    })


app = app



if __name__ == "__main__":
    app.run(debug=True)

