import sys
from random import*

from utils import *

file_res_name = "File_res"
file_fail_name = "File_fail"

def analyse_best(n,m,t):
    if t <= m:
        return (t*(t+1))/2
    else:
        return  ((m*(m+1))/2 + (t-m)*m)

def analyse_worst(n,m,t):
    fake_links = n*(n-1) - m
    if t <= fake_links:
        return 0
    else:
        rest = t-fake_links
        return  (rest*(rest+1))/2

def analyse_random(n,m,t):
    density=m / (((n-1)*n) /2)

    rounds = 1 / density
    number_of_rounds = int(t/rounds)

    if t > rounds*number_of_rounds:
        return (number_of_rounds*(number_of_rounds-1)/2)*rounds + number_of_rounds*(t-rounds*number_of_rounds)
    else:
        return (m*(m+1)/2)*rounds + (t-1*rounds-m*rounds)*m

def absolute_efficiency(file_res_name):
    number_link = 0
    my_file=open(file_res_name,"r")
    my_file1 = open(file_res_name, "r")
    number_lines=sum(1 for _ in my_file1)
    total=0
    for line in  reversed(list(my_file)):
        line_split=line.split(" ")
        if number_link==0:
            previous=int(line_split[0])
            total+=number_lines
        else:
            current=int(line_split[0])
            total+=((previous-current)*number_lines)
            previous=current
        #previous=line_split[]
        number_lines-=1
        number_link+=1
    return total

def get_normalized_efficiency(worst_efficiency,best_efficiency,absolute_efficiency):
    return (absolute_efficiency - worst_efficiency) / (best_efficiency - worst_efficiency)

def get_relative_efficiency(random_efficiency,absolute_efficiency, worst_efficiency, best_efficiency):
    return get_normalized_efficiency(worst_efficiency,best_efficiency,absolute_efficiency)/get_normalized_efficiency(worst_efficiency,best_efficiency,random_efficiency)

#file_res is the name of the file,
def calculate_precision(number_iteration):
    true_positives=number_lines(file_res_name)
    return true_positives/number_iteration

def calculate_recall( initial_file):
    return number_lines(file_res_name)/number_lines(initial_file)

def calculate_fScore(initial_file,number_iteration):
    precision=calculate_precision(file_res_name,number_iteration)
    recall=calculate_recall(file_res_name,initial_file)
    return 2*(precision*recall)/(precision+recall)

def calcul_positives_negatives(number_links,number_iteration):
    true_positive=number_lines(file_res_name)
    false_positive=number_iteration - true_positive
    false_negative=number_links - true_positive

def number_lines(file_name):
    my_file1 = open(file_name, "r")
    return sum(1 for _ in my_file1)

def complete_strategy(exist_link,unexist_link,average_degree_exist,current_iteration,number_node,loaded_graph,File_res):
    comp=0
    keys = set()
    [keys.add(str(x)) for x in loaded_graph.keys()]

    if number_node > len(average_degree_exist) or number_node == 0:
        number_node = len(average_degree_exist)

    while(comp < number_node):
        node=average_degree_exist[comp]
        node=node[0]

        node_exist_link=set()
        node_unexist_link=set()
        if node in exist_link.keys():
            node_exist_link=exist_link[node]
        if node in unexist_link.keys():
            node_unexist_link=unexist_link[node]

        node_test_link=set.union(node_unexist_link,node_exist_link)

        node_untest_link= set(keys).symmetric_difference(set(node_test_link))

        nbre=test_untested_links(node,node_untest_link,loaded_graph,current_iteration,File_res)
        current_iteration+=nbre
        comp+=1

    return current_iteration

def TBF_strategy(exist_link,unexist_link,couple_average_degree_exist,current_iteration,number_node,loaded_graph,File_res):
    comp=0

    if number_node > len(couple_average_degree_exist) or number_node == 0:
        number_node=len(couple_average_degree_exist)

    while(comp < number_node):
        node=couple_average_degree_exist[comp]
        node=node[0]
        #print(node)
        node1=node[0]
        node2=node[1]

        node_exist_link=set()
        node_unexist_link=set()
        #print(node1)
        if node1 in exist_link.keys():
            node_exist_link=exist_link[node1]
        if node1 in unexist_link.keys():
            node_unexist_link=unexist_link[node1]

        node_test_link=set.union(node_unexist_link,node_exist_link)

        if node2 not in node_test_link:
            node_untest_link= []
            node_untest_link.append(node2)
            #print(node_untest_link)
            nbre=test_untested_links(node1,node_untest_link,loaded_graph,current_iteration,File_res)
            #print(current_iteration)
            current_iteration=nbre
        comp+=1

    return current_iteration

def max_degree_node_somme(average_degree_exist,number_node):
    comp=0
    sum_node_degree=[]
    if number_node > len(average_degree_exist) or number_node==0:
        number_node=len(average_degree_exist)

    while comp < number_node:
        line = average_degree_exist[comp]
        node1=line[0]
        degree = line[1]
        compte=comp+1
        while compte < number_node:
            line2 = average_degree_exist[compte]
            degree2 = line2[1]
            node2=line2[0]
            nodes=[]
            sum=degree+degree2
            nodes.append((node1,node2))
            sum_node_degree.append(((node1,node2), sum))
            compte+=1
        comp+=1

    return list(reversed(sorted(sum_node_degree, key=lambda tup: tup[1])))

def test_untested_links(node,untested_nodes,loaded_graph,test_number,file_res):
    keys = []
    [keys.append(int(x)) for x in loaded_graph.keys()]
    for element in untested_nodes:
        test_number+=1
        if str(element) in loaded_graph[str(node)]:
            write_line(file_res, test_number, node, element)

    return test_number


def Random_strategy(file_res, file_fail, loaded_graph, number_iteration, number_node):
    checked_links={}
    current_iteration=1

    number_possible_links= number_node * (number_node - 1) / 2
    if number_iteration > number_possible_links:
        number_iteration=number_possible_links

    while current_iteration < number_iteration:
        #print(current_iteration)
        verify = True
        while verify:
            node1=randint(0,number_node-1)
            node2=randint(0,number_node-1)

            while node1==node2:
                node2=randint(0,number_node-1)

            minim=min(node1,node2)
            maxim=max(node1,node2)

            if minim in checked_links.keys():
                neighbors = checked_links[minim]
                if maxim not in neighbors:
                    verify=False
                    neighbors.add(maxim)
                    checked_links[minim]=neighbors
            else:
                verify=False
                new=set()
                new.add(maxim)
                checked_links[minim] = new

        keys = []
        [keys.append(int(x)) for x in loaded_graph.keys()]

        if node1 in keys:
            if str(node2) in loaded_graph[str(node1)]:
                write_line(file_res,current_iteration,node1,node2)
            else:
                write_line(file_fail, current_iteration, node1, node2)

        current_iteration+=1
    return current_iteration


# ------------------------------------------------------------------------------

def getGraph(file):
    file = open(graph_file, "r+")
    graph = file.read().splitlines()
    return load_graph(graph)


def prepare_strategy(file_res, file_fail):
    # 10: complete strategy
    file_res.close()
    file_fail.close()

    file_res = open("File_res", "r+")
    graph = file_res.read().splitlines()
    file_res_g = load_graph(graph, with_t=True)

    file_fail = open("File_fail", "r+")
    graph = file_fail.read().splitlines()
    file_fail_g = load_graph(graph, with_t=True)

    return file_res_g, file_fail_g


"""
    Implementation of the strategies
"""

def run_random_strategy(graph_file, iteration1, iteration2):
    g_original = getGraph(graph_file)

    delete_loop(g_original)
    number_nodes = size_of_graph(g_original)

    file_res = open(file_res_name, "w")
    file_fail = open(file_fail_name, "w")
    number_test = 50000
    Random_strategy(file_res, file_fail, g_original, number_test, number_nodes)


def run_complete_strategy(graph_file, iteration1, iteration2):
    g_original = getGraph(graph_file)

    delete_loop(g_original)
    number_nodes = size_of_graph(g_original)

    file_res = open(file_res_name, "w")
    file_fail = open(file_fail_name, "w")
    number_test = iteration1
    current_iteration = Random_strategy(file_res, file_fail, g_original, number_test, number_nodes)

    file_res_g, file_fail_g = prepare_strategy(file_res, file_fail)

    average_degree_distrib = nodes_degrees(file_res_g)

    return complete_strategy(file_res_g, file_fail_g, average_degree_distrib, current_iteration, iteration2, g_original,
                             file_res)


def run_tbf_strategy(graph_file, iteration1, iteration2):
    g_original = getGraph(graph_file)

    delete_loop(g_original)
    number_nodes = size_of_graph(g_original)

    file_res = open(file_res_name, "w")
    file_fail = open(file_fail_name, "w")
    number_test = iteration1
    current_iteration = Random_strategy(file_res, file_fail, g_original, number_test, number_nodes)

    file_res_g, file_fail_g = prepare_strategy(file_res, file_fail)

    average_degree_distrib = nodes_degrees(file_res_g)
    couple_average_degree_distrib = max_degree_node_somme(average_degree_distrib, 0)

    return TBF_strategy(file_res_g, file_fail_g, couple_average_degree_distrib, current_iteration, iteration2,
                        g_original,
                        file_res)


def run_mixed_tbf_complete_strategy(graph_file, iteration1, iteration2):
    current_iteration = run_complete_strategy(graph_file, iteration1, iteration2)

    file_res = open(file_res_name, "w")
    file_fail = open(file_fail_name, "w")

    file_res_g, file_fail_g = prepare_strategy(file_res, file_fail)

    average_degree_distrib = nodes_degrees(file_res_g)
    couple_average_degree_distrib = max_degree_node_somme(average_degree_distrib, 0)

    TBF_strategy(file_res_g, file_fail_g, couple_average_degree_distrib, current_iteration, iteration2, g_original,
                 file_res)


def run_mixed_complete_tbf_strategy(graph_file, iteration1, iteration2):
    current_iteration = run_tbf_strategy(graph_file, iteration1, iteration2)

    file_res = open(file_res_name, "w")
    file_fail = open(file_fail_name, "w")

    file_res_g, file_fail_g = prepare_strategy(file_res, file_fail)
    average_degree_distrib = nodes_degrees(file_res_g)

    complete_strategy(file_res_g, file_fail_g, average_degree_distrib, current_iteration, iteration2, g_original,
                      file_res)


if __name__ == '__main__':
    print("Args: ", sys.argv[1])

    if len(sys.argv) <= 1:
        print("please enter an argument")


    elif len(sys.argv) == 5:
        graph_file = sys.argv[1]
        strategy = sys.argv[2]
        iteration1 = int(sys.argv[3])
        iteration2 = int(sys.argv[4])

        if strategy == "random":
            run_random_strategy(graph_file, iteration1, iteration2)

        elif strategy == "complete":
            run_complete_strategy(graph_file, iteration1, iteration2)

        elif strategy == "tbf":
            run_tbf_strategy(graph_file, iteration1, iteration2)

        elif strategy == "mixed_tbf_complete":
            run_mixed_tbf_complete_strategy(graph_file, iteration1, iteration2)

        elif strategy == "mixed_complete_tbf":
            run_mixed_complete_tbf_strategy(graph_file, iteration1, iteration2)

        else:
            print("erreur")

    else:
        print("erreur number of args")
