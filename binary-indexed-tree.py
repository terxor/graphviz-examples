# Generating a binary indexed tree
# with each node containing id, bit representation
# and range denoted by that node
# 
# Also supports highlighting nodes whose range
# contain a particular id

import graphviz

# Remove LSB
def h(x):
  if x == 0: return 0
  return x - (x & ~(x - 1))

# Get bit representation
def bits(x):
  return format(x, '04b')

# Generate graph with name, number of nodes, optional highlight
def gen(name, n, hl=-1):
  assert n > 0
  # hl : 'i' for such that nodes which contain i in their range are highlighted

  g = graphviz.Digraph(name=name, comment="BIT", format="svg")

  # Left to Right instead of Top to Bottom
  # g.attr(rankdir="LR")
  
  # Rounded rectangle like nodes
  g.attr("node", shape="Mrecord")

  a = [h(i) for i in range(n + 1)]

  g.node("0", "0 (0000)")
  for i in range(1, n + 1):
    u, v = h(i) + 1, i
    col = "red" if (u <= hl and hl <= v) else "black"
    # g.node("%d" % (i), "%d (%s) | %d, %d" % (i, bits(i), u, v), color=col)
    g.node("%d" % (i), "{%d (%s) | %d, %d}" % (i, bits(i), u, v), color=col)

  for i in range(1, n + 1):
    g.edge("%d" % (h(i)), "%d" % (i))

  g.render(filename=name)

# ---
gen("bit-example", 15)
gen("bit-example-2", 15, 5)
gen("bit-example-3", 15, 9)
