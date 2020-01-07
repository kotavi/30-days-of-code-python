from collections import deque

def find_person(graph, root_name, name_to_search):
    to_search = deque()
    to_search += graph[root_name]
    searched = list()
    while to_search:
        person = to_search.popleft()
        if person not in searched:
            if person == name_to_search:
                print("Connection was found")
                return True
            else:
                to_search += graph[person]
                searched.append(person)
    print("Connection was not found")
    return False


if __name__ == '__main__':
    my_graph = dict()
    my_graph['Tanya'] = ['Ihor', 'Anna', 'Nadya']
    my_graph['Ihor'] = ['Petr', 'Vasya', 'Anna', 'Nikita', 'Chris']
    my_graph['Petr'] = []
    my_graph['Vasya'] = []
    my_graph['Chris'] = ['Nick']
    my_graph['Nikita'] = []
    my_graph['Nick'] = []
    my_graph['Anna'] = ['Nikita', 'Olga']
    my_graph['Olga'] = []
    my_graph['Nadya'] = ['Viktor', 'Vladimir']
    my_graph['Viktor'] = []
    my_graph['Vladimir'] = []

    find_person(my_graph, 'Tanya', 'Vladimir')
    find_person(my_graph, 'Nadya', 'Vladimir')
    find_person(my_graph, 'Ihor', 'Vladimir')
