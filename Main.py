"""
Main files
"""
from DS import LinkedList
import sort_methods
import time

print(30 * ' ' + 20 * '*')
print('Type "exit" when you wanted to quit.')
print(30 * ' ' + 20 * '*')
print('Type "help" for allowed commands.')
print(30 * ' ' + 20 * '*')

data = []


def cycle_matrix(row):
    z = 0
    for v in graph[int(edges[row][0]) - 1][1]:
        if v in graph[edges[row][1] - 1][1]:
            z += 1
    return z


def dfs(Graph, Start):
    Visited = [Start]
    stack = []
    for i in range(0,len(Graph[Start-1][1])):
        stack.append(Graph[Start - 1][1][i])
    while stack != []:
        tmp = stack.pop()
        if tmp not in Visited:
            Visited.append(tmp)
            for i in range(0, len(Graph[tmp - 1][1])):
                stack.append(Graph[tmp - 1][1][i])

    return Visited

while True:
    _input = input('Enter a command: ').split()
    try:
        if len(_input) is 0:
            print('Wrong!\ncheck "help" for more information!')
        elif 'exit' in _input[0]:
            break
        elif 'help' in _input[0]:
            print(30 * ' ' + 40 * '*')
            print('At first you have to set data!')
            print(30 * ' ' + 40 * '*')
            print('run commands:')
            # print('    >>> run LinkedList Quick ')
            # print('    >>> run LinkedList Insertion ')
            # print('    >>> run LinkedList Merge ')
            # print('    >>> run LinkedList Bubble ')
            # print('    >>> run LinkedList Optimum Insertion <your input number> ')
            # print('    >>> run LinkedList Optimum Bubble <your input number> ')
            print('    >>> run Matrix Quick ')
            print('    >>> run Matrix Insertion  ')
            print('    >>> run Matrix Merge ')
            print('    >>> run Matrix Bubble ')
            # print('    >>> run Matrix Optimum Insertion <your input number> ')
            # print('    >>> run Matrix Optimum Bubble <your input number> ')
            print(30 * ' ' + 40 * '*')
            print('input command:')
            print('    >>> input <name of your test case file>')

        elif _input[0] in 'input':
            data = open(_input[1], 'r')
            lineList = data.readlines()
            for i in range(len(lineList)):
                lineList[i] = lineList[i].split(',')
            for i in range(len(lineList)):
                for j in range(2):
                    lineList[i][j] = int(lineList[i][j])
            graph = [[0 for i in range(2)] for i in range(int(lineList[-1][0]))]

            s = []
            start = 1
            for i in range(0, len(lineList)):
                if lineList[i][0] is start:
                    s.append(lineList[i][1])
                else:
                    start = lineList[i][0]
                    graph[lineList[i - 1][0] - 1][0] = lineList[i - 1][0]
                    graph[lineList[i - 1][0] - 1][1] = s
                    s = []
                    s.append(lineList[i][1])
            graph[-1][0] = lineList[-1][0]
            graph[-1][1] = s
            edges = [[0 for i in range(3)] for i in range(len(lineList))]
            for i in range(len(lineList)):
                edges[i][0], edges[i][1] = lineList[i][0], lineList[i][1]

            k = []
            degree = 0
            start = 1
            for i in range(0, len(edges)):
                if edges[i][0] is start:
                    degree += 1
                else:
                    start = edges[i][0]
                    print(degree)
                    k.append(degree)
                    degree = 1
            k.append(degree)

            print("Data set!", '\n', "Graph created!")
        # elif _input[1] == 'LinkedList' and data is not None:
        #     graph_linkedList = LinkedList()
        #     i = len(graph) - 1
        #     while i is not -1:
        #         child = LinkedList()
        #         graph_linkedList.__add__(graph[i])
        #         graph_linkedList.add__child(child)
        #         j = len(graph[i][1]) - 1
        #         while j is not -1:
        #             child.__add__(graph[i][1][j])
        #             j -= 1
        #         child.clear()
        #         i -= 1
        #     i = None
        #
        #     if _input[2] in 'Quick' and len(_input) == 3:
        #         print("DO2")
        #     elif _input[2] in 'Insertion' and len(_input) == 3:
        #         print("DO3")
        #     elif _input[2] in 'Merge' and len(_input) == 3:
        #         print("DO4")
        #     elif _input[2] in 'Bubble' and len(_input) == 3:
        #         print("DO5")
        #     elif _input[2] in 'Optimum':
        #         if _input[3] in 'Insertion' and len(_input) == 4:
        #             print("DO6")
        #         elif _input[3] in 'Bubble' and len(_input) == 4:
        #             print("DO7")
        #         else:
        #             print('Wrong!\ncheck "help" for more information!')

        elif _input[1] == 'Matrix' and data is not None:
            start_time = time.time()
            matrix = [[0 for i in range(3)] for i in range(len(lineList))]
            for i in range(len(lineList)):
                matrix[i][0], matrix[i][1] = lineList[i][0], lineList[i][1]
            lineList.clear()
            if _input[2] in 'Quick' and len(_input) == 3:
                visited = dfs(graph, 1)
                while len(visited) == len(graph):
                    for member in range(len(edges)):
                        Cij = 0
                        Zij = cycle_matrix(member)
                        if min(k[edges[member][0] - 1] - 1, k[edges[member][1] - 1] - 1) != 0:
                            Cij = Zij / (min(k[edges[member][0] - 1] - 1, k[edges[member][1] - 1] - 1))
                        else:
                            Cij = 10 ** 7
                        edges[member][2] = Cij
                    sort_methods.quick_sort(edges, 0, len(edges) - 1)
                    tmp1 = edges.pop(0)
                    tmp2 = edges.pop(0)
                    tmp1[2] = int(tmp1[2])
                    tmp2[2] = int(tmp2[2])
                    print(tmp1)
                    print(matrix[7])
                    matrix.remove(tmp1)
                    matrix.remove(tmp2)
                    k[tmp1[0] - 1] -= 1
                    k[tmp1[1] - 1] -= 1
                    graph[tmp1[0] - 1][1].remove(tmp1[1])
                    graph[tmp1[1] - 1][1].remove(tmp1[0])
                    visited = dfs(graph, 1)
                end_time = time.time()
                print(graph[0:10])
                print("Done!")
                print(end_time - start_time)

            elif _input[2] in 'Insertion' and len(_input) == 3:
                    visited = dfs(graph, 1)
                    while len(visited) == len(graph):
                        for member in range(len(edges)):
                            Cij = 0
                            Zij = cycle_matrix(member)
                            if min(k[edges[member][0] - 1] - 1, k[edges[member][1] - 1] - 1) != 0:
                                Cij = Zij / (min(k[edges[member][0] - 1] - 1, k[edges[member][1] - 1] - 1))
                            else:
                                Cij = 10 ** 7
                            edges[member][2] = Cij
                        sort_methods.insertion_sort(edges)
                        tmp1 = edges.pop(0)
                        tmp2 = edges.pop(0)
                        tmp1[2] = int(tmp1[2])
                        tmp2[2] = int(tmp2[2])
                        print(tmp1)
                        print(matrix[7])
                        matrix.remove(tmp1)
                        matrix.remove(tmp2)
                        k[tmp1[0] - 1] -= 1
                        k[tmp1[1] - 1] -= 1
                        graph[tmp1[0] - 1][1].remove(tmp1[1])
                        graph[tmp1[1] - 1][1].remove(tmp1[0])
                        visited = dfs(graph, 1)
                    end_time = time.time()
                    print(graph[0:10])
                    print("Done!")
                    print(end_time - start_time)
            elif _input[2] in 'Merge' and len(_input) == 3:
                visited = dfs(graph, 1)
                while len(visited) == len(graph):
                    for member in range(len(edges)):
                        Cij = 0
                        Zij = cycle_matrix(member)
                        if min(k[edges[member][0] - 1] - 1, k[edges[member][1] - 1] - 1) != 0:
                            Cij = Zij / (min(k[edges[member][0] - 1] - 1, k[edges[member][1] - 1] - 1))
                        else:
                            Cij = 10 ** 7
                        edges[member][2] = Cij
                    sort_methods.merge_sort(edges, 0, 1)
                    tmp1 = edges.pop(0)
                    tmp2 = edges.pop(0)
                    tmp1[2] = int(tmp1[2])
                    tmp2[2] = int(tmp2[2])
                    print(tmp1)
                    print(matrix[7])
                    matrix.remove(tmp1)
                    matrix.remove(tmp2)
                    k[tmp1[0] - 1] -= 1
                    k[tmp1[1] - 1] -= 1
                    graph[tmp1[0] - 1][1].remove(tmp1[1])
                    graph[tmp1[1] - 1][1].remove(tmp1[0])
                    visited = dfs(graph, 1)
                end_time = time.time()
                print(graph[0:10])
                print("Done!")
                print(end_time - start_time)
            elif _input[2] in 'Bubble' and len(_input) == 3:
                visited = dfs(graph, 1)
                while len(visited) == len(graph):
                    for member in range(len(edges)):
                        Cij = 0
                        Zij = cycle_matrix(member)
                        if min(k[edges[member][0] - 1] - 1, k[edges[member][1] - 1] - 1) != 0:
                            Cij = Zij / (min(k[edges[member][0] - 1] - 1, k[edges[member][1] - 1] - 1))
                        else:
                            Cij = 10 ** 7
                        edges[member][2] = Cij
                    sort_methods.bubble_sort(edges)
                    tmp1 = edges.pop(0)
                    tmp2 = edges.pop(0)
                    tmp1[2] = int(tmp1[2])
                    tmp2[2] = int(tmp2[2])
                    print(tmp1)
                    print(matrix[7])
                    matrix.remove(tmp1)
                    matrix.remove(tmp2)
                    k[tmp1[0] - 1] -= 1
                    k[tmp1[1] - 1] -= 1
                    graph[tmp1[0] - 1][1].remove(tmp1[1])
                    graph[tmp1[1] - 1][1].remove(tmp1[0])
                    visited = dfs(graph, 1)
                end_time = time.time()
                print(graph[0:10])
                print("Done!")
                print(end_time - start_time)
            # elif _input[2] in 'Optimum':
            #     if _input[3] in 'Insertion' and len(_input) == 4:
            #         print("DO62")
            #     elif _input[3] in 'Bubble' and len(_input) == 4:
            #         print("DO72")
            #     else:
            #         print('Wrong!\ncheck "help" for more information!')

            else:
                print('Wrong!\ncheck "help" for more information!')
        else:
            print('Wrong!\ncheck "help" for more information!')
        print(30 * ' ' + 20 * '*')
    except:
        print('Wrong!\ncheck "help" for more information!')
