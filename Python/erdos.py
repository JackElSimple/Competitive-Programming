import os
import sys
from collections import deque

class Node:
    def __init__(self, name):
        self.name = name
        self.number = -1
        self.adjacent_nodes = dict()

    def connect_with(self, other):
        if not other.name in self.adjacent_nodes.keys():
            self.adjacent_nodes[other.name] = other

    def erdos_number(self):
        if self.number >= 0:
            return self.number
        else:
            return 'infinity'

if __name__ == '__main__':
    scenarios = int(input().strip())
    for i in range(scenarios):
        papers, authors = [int(x) for x in input().strip().split()]
        d = dict()
        # load all papers from papers database
        for j in range(papers):
            line = input().strip().split(sep = ':')[0]
            parts = line.split(sep = ',')
            # prepare the list of authors of the current paper
            current_paper_author_list = list()
            for k in range(0, len(parts), 2):
                if k + 1 < len(parts):
                    author_name = parts[k].strip() + ', ' + parts[k+1].strip()
                else:
                    author_name = parts[k].strip()
                current_paper_author_list.append(author_name)

            # add to the nodes of the graph those authors that did not exist yet
            current_paper_node_list = list()
            for author_name in current_paper_author_list:
                if not author_name in d.keys():
                    d[author_name] = Node(author_name) # crea nodo del autor y lo añade a d
                    #print('*****', author_name)
                current_paper_node_list.append(d[author_name])

            # connect the co-authors (i.e., the nodes) 
            for k in range(len(current_paper_node_list)):
                for l in range(k + 1, len(current_paper_node_list)): 
                    current_paper_node_list[k].connect_with(current_paper_node_list[l]) # bidireccional
                    current_paper_node_list[l].connect_with(current_paper_node_list[k]) # bidireccional
                    
            
        # compute the Erdos numbers for all the nodes
        erdos_name = "Erdos, P."
        if erdos_name in d:
            erdos_node = d[erdos_name]
            erdos_node.number = 0 
            
            queue = deque([erdos_node])
            
            # Bucle principal del BFS
            while queue:
                current_node = queue.popleft()
                distancia_actual = current_node.number
                
                # Explorar coautores conectados
                for neighbor in current_node.adjacent_nodes.values():
                    # Si el número es -1, es que no ha sido visitado aún 
                    if neighbor.number == -1:
                        neighbor.number = distancia_actual + 1
                        queue.append(neighbor)

        print("Scenario {}".format(i + 1))
        # print Erdos number of required authors
        for j in range(authors):
            name = input().strip()
            print(name, d[name].erdos_number() if name in d.keys() else 'infinity')