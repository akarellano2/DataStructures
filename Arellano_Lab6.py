# Name: Ana K. Arellano
# Lab: 6
# ID: 80631366


class DisjointSetForest:
    def __init__(self, n):
        self.forest = [-1] * n

    def is_index_valid(self, index):
        return 0 <= index < len(self.forest)

    # Problem 6
    def find(self, a):
        if not self.is_index_valid(a):
            return -1

        if self.forest[a] < 0:
            return a

        return self.find(self.forest[a])

    # Problem 7
    def find_contains_loop(self, a, s=None):
        if not self.is_index_valid(a):
            return -1

        if s is None:
            s = set()

        if a in s:
            print("Loop found")
            return -1

        s.add(a)

        if self.forest[a] < 0:
            return a

        return self.find_contains_loop(self.forest[a], s)

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra != rb:  # Problems 3 and 4
            self.forest[rb] = ra

    # Problem 2
    def in_same_set(self, a, b):
        if not self.is_index_valid(a) or not self.is_index_valid(b):
            return False

        return self.find(a) == self.find(b)

    # Problem 5
    def num_sets(self):
        count = 0

        for k in self.forest:
            if k < 0:
                count += 1

        return count

    # Problem 9
    def is_equal(self, dsf):

        if len(self.forest) != len(dsf.forest):
            return False

        # Running time O(n^2). Can you do it in O(n)? (:
        for i in range(len(self.forest)):
            for j in range(len(self.forest)):
                if self.in_same_set(i, j) != dsf.in_same_set(i, j):
                    return False

        return True


class Queue:
    def __init__(self, item = None):
        self.item = item
        self.queue = []

    def put(self, item):
        self.queue.append(item)

    def get(self):
        if self.is_empty():
            return
        a = self.queue[0]
        del self.queue[0]
        return a

    def is_empty(self):
        return len(self.queue) == 0


class Edge:
    def __init__(self, dest, weight=1):
        self.dest = dest
        self.weight = weight


class GraphAL:
    # Constructor
    def __init__(self, vertices, weighted=False, directed=False):
        self.al = [[] for i in range(vertices)]
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AL'

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.al)

    def insert_vertex(self):
        self.al.append([])

        return len(self.al) - 1  # Return id of new vertex

    def insert_edge(self, source, dest, weight=1):
        if not self.is_valid_vertex(source) or not self.is_valid_vertex(dest):
            print('Error, vertex number out of range')
        elif weight != 1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.al[source].append(Edge(dest, weight))
            if not self.directed:
                self.al[dest].append(Edge(source, weight))

    def delete_edge(self, source, dest):
        if source >= len(self.al) or dest >= len(self.al) or source < 0 or dest < 0:
            print('Error, vertex number out of range')
        else:
            deleted = self._delete_edge(source, dest)
            if not self.directed:
                deleted = self._delete_edge(dest, source)
            if not deleted:
                print('Error, edge to delete not found')

    def _delete_edge(self, source, dest):
        i = 0
        for edge in self.al[source]:
            if edge.dest == dest:
                self.al[source].pop(i)
                return True
            i += 1
        return False

    def num_vertices(self):
        return len(self.al)

    def vertices_reachable_from(self, src):
        reachable_vertices = set()

        for edge in self.al[src]:
            reachable_vertices.add(edge.dest)

        return reachable_vertices

    def get_highest_cost_edge(self):

        max_key = -float("inf")

        for lst in self.al:
            for edge in lst:
                max_key = max(edge.weight, max_key)

        return max_key

    def num_edges(self):
        count = 0

        for lst in self.al:
            count += len(lst)

        return count

    def edge_weight(self, src, dest):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return 0  # Design decision

        lst = self.al[src]

        for edge in lst:
            if edge.dest == dest:
                return edge.weight

        return 0

    def reverse_edges(self):

        graph = GraphAL(vertices=len(self.al), weighted=self.weighted, directed=self.directed)

        for i in range(len(self.al)):
            lst = self.al[i]
            for edge in lst:
                graph.insert_edge(edge.dest, i, edge.weight)

        self.al = graph.al

    def num_of_self_edges(self):
        count = 0

        for i in range(len(self.al)):
            for edge in self.al[i]:
                if edge.dest == i:
                    count += 1

        return count

    def contains_cyle(self):  # Asumption: Directed Graph
        dsf = DisjointSetForest(self.num_vertices())

        for i in range(len(self.al)):
            for edge in self.al[i]:
                if dsf.find(i) == dsf.find(edge.dest):
                    return True

                dsf.union(i, edge.dest)

        return False

    def is_isolated(self, v):
        if not self.is_valid_vertex(v):
            return False

        if len(self.al[v]) != 0:
            return False

        for lst in self.al:
            for edge in lst:
                if edge.dest == v:
                    return False

        return True

    def display(self):
        print('[', end='')
        for i in range(len(self.al)):
            print('[', end='')
            for edge in self.al[i]:
                print('(' + str(edge.dest) + ',' + str(edge.weight) + ')', end='')
            print(']', end=' ')
        print(']')

    def get_adj_vertices(self, v):
        adj_list = list()
        for i in self.al[v]:
            adj_list.append(i.dest)
        return adj_list

    def compute_indegree_every_vertex(self):
        list_indegree = list() # list that will have indegrees
        self.reverse_edges() #changing the to point to the oposite direction
        for i in range(len(self.al)):
            list_indegree.append(len(self.al[i])) #appending the number of degrees that is pointing to the vertex

        return list_indegree

    def get_edges(self): #method that is getting all of the edges of the graph
        dictionary_vertex_dest = {} # placing the vertex and destination in the vertex
        for i in range(len(self.al)):
            for j in self.al[i]:
                dictionary_vertex_dest[(i, j.dest)] = j.weight # making vertex and destination as key and saving the
                                                                                                        #weight of it
        return dictionary_vertex_dest


def topological_sort(graph):  # sorting the graph in topological order
    all_in_degrees = graph.compute_indegree_every_vertex()
    graph.reverse_edges() # reversing the edges back to the way they were in order to sort them correctly
    graph.display()
    sort_result = []
    q = Queue()
    for i in range(len(all_in_degrees)):
        if all_in_degrees[i] == 0:
            q.put(i)

    while not q.is_empty():
        u = q.get()
        sort_result.append(u)

        for adj_vertex in graph.get_adj_vertices(u):
            all_in_degrees[adj_vertex] -= 1

            if all_in_degrees[adj_vertex] == 0:
                q.put(adj_vertex)

    if len(sort_result) != graph.num_vertices():
        return None

    return sort_result


def kruskal_algorithm(graph):  # kruskal algorith which will show the minnimun spanning tree
    min_spanning_tree = GraphAL(graph.num_vertices(), weighted=True, directed= True) # creating new graph
    dictionary_edges = graph.get_edges()  # dictionary that saves edges
    list_weights = list()
    for i in dictionary_edges: # adding edges with weights to the list
        if dictionary_edges[i] not in list_weights:
            list_weights.append(dictionary_edges[i])

    list_weights.sort() #sorting the list of the weights

    for i in list_weights:
        for j in dictionary_edges:
            if dictionary_edges[j] == i:

                min_spanning_tree.insert_edge(j[0],j[1], i)
                if min_spanning_tree.contains_cyle():
                    min_spanning_tree.delete_edge(j[0], j[1])
    return min_spanning_tree


def main():
    print("Topological")
    g = GraphAL(6, directed=True)
    g.insert_edge(0, 1)
    g.insert_edge(0, 2)
    g.insert_edge(1, 2)
    g.insert_edge(2, 3)
    g.insert_edge(3, 4)
    g.insert_edge(4, 5)
    g.insert_edge(1, 5)

    g.display()
    print(topological_sort(g))
    print("")
    g1 = GraphAL(6, weighted=True, directed=True)
    g1.insert_edge(0, 1, 4)
    g1.insert_edge(0, 2, 3)
    g1.insert_edge(1, 2, 2)
    g1.insert_edge(2, 3, 1)
    g1.insert_edge(3, 4, 5)
    g1.insert_edge(4, 1, 4)
    print("Kruskal")
    kruskal_algorithm(g1).display()


main()

