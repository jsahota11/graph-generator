# graph-generator
Online tool to generate random graphs with varying vertex and edge sets. 
Goal is to implement multiple tools so the user can generate graphs subject to certain constraints.

### TODO
##### Housekeeping
* Implement custom labels
* Clean up comments and refactor
* Add style
* Fix extra nodes when selected labels mismatch custom edges (ex. choose integer labels with custom edge A-B)
* Restrict graph movement to box bounds
* Fix "none" label option (still displays labels by default)
* Fix that extra nodes appear when edge relationships skip over labels in sequence for letters
  * ex. 5 nodes and 7 edges with letter labels, but edges consider A-D, F. Form will automatically add node labelled E.
  * Works fine for numbers AFAIK, but may need more testing

##### Features
* Customize node colours
* Customize edge direction placement
* Allow distortion without maintaining graph proportions
* Implement simple search system to generate known graphs
* Edge options for: Line type, arrow strike-through, colouring
* Implement edge weights

##### Meta
* Figure out what made vercel deployment work
* Script auto-deploy upon push to main
* Script dir/file edits upon push to main
