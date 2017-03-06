#!/usr/bin/env python

class dependency_resolution:
        """ convert introduced element into a formatted list"""
        def elem_to_array(self, n_lines, line, graph):
                elems = line.split()
                self.add_node(graph, elems[0])
                root = elems[0]
                for i in range(1,len(elems)):
                        if i < (len(elems)):
                                self.add_dependency(graph, elems[i], root)

        """Add a node to the graph if not already exists."""
        def add_node(self, graph, elem):
                if not graph.has_key(elem):
                        graph[elem] = []

        """ append a new introduced dependency"""
        def add_dependency(self, graph, elem, root):
                graph[root].append(elem)

        """ get root elements which does not need any deps to be installed"""
        def getroot_elem(self, graph):
                roots = []
                for node in graph:
                        if(not graph[node]):
                                print "empty"
                                #graph.pop(node)
                                roots.append(node)
                return roots

        """ delete root element when it is installed"""
        def delete_root_elems(self, graph, roots):
                for node in roots:
                        graph.pop(node)

        """ delete deps when they are already installed"""
        def delete_deps_elems(self, graph, roots):
                for node in graph:
                        for child in graph[node]:
                                graph[node].remove(child)


"""main """
graph = {}
dps = dependency_resolution()

n=0
#read number of lines
print "please provide the number of lines"
n_lines = raw_input(" >>  ")

while(not n_lines.isdigit()):
        print("You have to introduce a number")
        n_lines = raw_input(" >>  ")

#read lines, split them and add them as nodes to the graph
print "please provide the lines"
while(n < int(n_lines)):
        line = raw_input(" >>  ")
        dps.elem_to_array(n_lines, line, graph)
        n=n+1
roots = dps.getroot_elem(graph)
dps.delete_deps_elems(graph, roots)
dps.delete_root_elems(graph, roots)

print graph
