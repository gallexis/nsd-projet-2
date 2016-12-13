from random import*

from utils import *


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
    density=0.1# m / (((n-1)*n) /2)

    rounds = 1 / density
    number_of_rounds = int(t/rounds)

    if t > rounds*number_of_rounds:
        return (number_of_rounds*(number_of_rounds-1)/2)*rounds + number_of_rounds*(t-rounds*number_of_rounds)
    else:
        print("toto")
        return (m*(m+1)/2)*rounds + (t-1*rounds-m*rounds)*m

def absolute_efficiency(file_res,t):
    number_link=0
   # for line in file_res:
   #     print(line)

def get_normalized_efficiency(worst_efficiency,best_efficiency,absolute_efficiency):
    return (absolute_efficiency - worst_efficiency) / (best_efficiency - worst_efficiency)

def get_relative_efficiency(random_efficiency,absolute_efficiency, worst_efficiency, best_efficiency):
    return get_normalized_efficiency(worst_efficiency,best_efficiency,absolute_efficiency)/get_normalized_efficiency(worst_efficiency,best_efficiency,random_efficiency)

def calculate_precision(true_positives,false_positives):
    return true_positives/(true_positives + false_positives)

def calculate_recall(true_positives, false_negatives):
    return true_positives/(true_positives + false_negatives)

def calculate_fScore(precision, recall):
    return 2*(precision*recall)/(precision+recall)

def calcul_positives_negatives(file_res,number_links,number_iteration):
    true_positive=0#number of lines in file_res
    false_positive=number_iteration - true_positive
    false_negative=number_links - true_positive

def test_untested_links(node,untested_nodes,loaded_graph,test_number):
    keys = []
    [keys.append(int(x)) for x in loaded_graph.keys()]
    for element in untested_nodes:
        test_number+=1
        if node in keys:
            if str(element) in loaded_graph[str(node)]:
                write_line(file_res, current_iteration, node1, node2)


def implementation(file_res, file_fail, loaded_graph, number_iteration, number_node):
    checked_links={}
    current_iteration=1
    #print(number_node)
    number_possible_links= number_node * (number_node - 1) / 2
    if number_iteration > number_possible_links:
        number_iteration=number_possible_links

    while current_iteration < number_iteration:
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


def main():

    file = open("Flickr-test", "r+")
    graph= file.read().splitlines()
    g_original = load_graph(graph)

    delete_loop(g_original)
    number_nodes=size_of_graph(g_original)

    file_res = open("File_res", "w")
    file_fail = open("File_fail", "w")

    implementation(file_res, file_fail, g_original, 100000, number_nodes)

    absolute_efficiency(file_res,3)

    # 10: complete strategy
    file_res.close()
    file_fail.close()

    file_res = open("File_res", "r+")
    graph = file_res.read().splitlines()
    file_res_g = load_graph(graph, with_t=True)

    file_fail = open("File_fail", "r+")
    graph = file_fail.read().splitlines()
    file_fail_g = load_graph(graph, with_t=True)

    average_degree_distrib = nodes_degrees(file_res_g)





if __name__ == '__main__':
    main()