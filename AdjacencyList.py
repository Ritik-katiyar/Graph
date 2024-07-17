class Vertex:
    def __init__(self,data):
        self.vertex = data
        self.next = None
class Graph:
    def __init__(self,vertices):
        self.nV = vertices
        self.graph_arr = [None]*self.nV
    def add_edge(self,src,dest):
        node = Vertex(dest)
        node.next = self.graph_arr[src]
        self.graph_arr[src]  = node
        node = Vertex(src)
        node.next = self.graph_arr[dest]
        self.graph_arr[dest]  = node
    def print_graph(self):
        for i in range(self.nV):
            print("list of vertex {}\n".format(i),end="")
            temp = self.graph_arr[i]
            while temp:
                print("->{}".format(temp.vertex),end="")
                temp = temp.next
            print("\n")
    
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0,1)
    g.add_edge(1,2)
    g.add_edge(2,3)
    g.add_edge(3,0)
    g.add_edge(1,3)
    g.print_graph()