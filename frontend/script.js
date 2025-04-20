console.log("Loaded script.js")

async function sendData(event) {
    // idk why someone said to online
  event.preventDefault();

    // Grab form data
    form = event.target;
    vertices = parseInt(form.vertices.value);
    edges = parseInt(form.edges.value);
    labelType = form.label_type.value;
    directed = form.directed.checked;

    // check that form data is valid before generating
    customEdgeTokens = form.custom_edges.value.trim();
    customEdges = [];

    // check valid amount of vertices
    if (isNaN(vertices) || vertices <1){
        alert("The graph must contain atleast 1 vertex.");
        return;
    }

    // check valid number of edges
    if (isNaN(edges) || edges < 0){
        alert("The graph cannot have negative edge count.");
        return;
    }

    // check that custom edges are valid
    if (customEdgeTokens.length > 0){

        // incase they were inputted weird
        edgeList = customEdgeTokens.split(',').map(edge => edge.trim());
        for (edge of edgeList){
            endpoints = edge.split("-");

            // invalid format
            if (endpoints.length !== 2){
                alert(`Invalid edge format: \"${edge}\". Expected format: A-B.`)
                return;
            }

            // otherwise, we good so add it to the edges
            customEdges.push(endpoints);
        }
    }

    let labels = [];

    // validate custom labels (if selected)
    if (labelType === "custom"){
        vals = form.custom_labels.value.trim();

        if (!vals){
            alert("Custom labels were chosen, but none were entered!");
            return;
        }

        labels = vals.split(",").map(l => l.trim());

        if (labels.length!==vertices){
            alert(`You must provide exactly ${vertices} labels.`);
            return;
        }
    }

    // send data to the back
    response = await fetch ('/api/data', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            vertices,
            edges,
            label_type: labelType,
            directed,
            custom_labels: labels,
            custom_edges: customEdges
        })
    });

    // wait for the back to do its thing
    result = await response.json();

    // display results in output element (pre in index, but that ruins abstraction!)
    document.getElementById('output').textContent = JSON.stringify(result, null, 2);

    // cook with vis
    container = document.getElementById('graphContainer');
    nodes = new vis.DataSet(result.nodes.map(n=>({ id: n, label: n })));
    edges = new vis.DataSet(result.edges.map(([from, to]) => ({ from, to })));
    data = {nodes, edges};
    options ={
        nodes: {shape: "dot", size: 15},
        edges: {arrows: directed ? "to" : ""},
        physics: {enabled: true}
    };

    new vis.Network(container, data, options);
}

// bind sendData to the submit button
document.getElementById("graphInfo").addEventListener("submit", sendData)
