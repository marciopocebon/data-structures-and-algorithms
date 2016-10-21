class Queue():
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return len(self.items) == 0

  def enqueue(self, item):
    self.items.insert(0, item)

  def dequeue(self):
    return self.items.pop()

def isUnvisited(vertex, graph_info):
  return graph_info[vertex]['distance'] == None

def build_graph_info(adjacency_list):
  vertices = []

  for i in range(len(adjacency_list)):
    vertex = {
      'distance': None,
      'predecessor': None
    }

    vertices.append(vertex)

  return vertices

def breadth_first_search(graph, starting_vertex):
  # will be used to compute the distance between
  # source and destination vertices
  graph_info = build_graph_info(graph)

  queue = Queue()
  queue.enqueue(starting_vertex)
  graph_info[starting_vertex]['distance'] = 0

  while not queue.isEmpty():
    src_vertex = queue.dequeue()

    for dest_vertex in graph[src_vertex]:
      if isUnvisited(dest_vertex, graph_info):
        graph_info[dest_vertex]['distance'] = graph_info[src_vertex]['distance'] + 1
        graph_info[dest_vertex]['predecessor'] = src_vertex
        queue.enqueue(dest_vertex)

  return graph_info
