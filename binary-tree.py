import graphviz

# Generate perfect binary tree of height h
def gen(h):
  assert h > 0
  # hl : 'i' for such that nodes which contain i in their range are highlighted
  n = 2**(h + 1) - 1

  g = graphviz.Digraph(comment="Binary Tree", format="svg")
  # g.attr(rankdir="LR")
  g.attr("node", shape="circle")
  
  for i in range(1, n + 1):
    node_id = "%d" % (i)
    g.node(node_id, node_id)
    if i > 1:
      g.edge("%d" % (i / 2), node_id)
  g.render()

gen(3)
