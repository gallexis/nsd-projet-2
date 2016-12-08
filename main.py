from utils import *

def adjacency_matrix_from_graph(graph):
    nodes = get_nodes_from_graph(graph)
    matrix = {}

    for node in nodes:
        matrix[node] = []

    return matrix


def link_exists(node1,node2,graph):
    nodes = graph[node1]

    return node2 in nodes

def add_link(node1,node2,simul):
    simul[node1].append(node2)
    simul[node2].append(node1)

def write_line(file,test_number,node1,node2):
    file.write(str(test_number) + ' ' + str(node1+" "+node2+"\n"))


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
    for line in file_res:
        print(line)

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
    true_positive=number of lines in file_res
    false_positive=number_iteration - true_positive
    false_negative=number_links - true_positive

def implementation(file_test,file_res,number_iteration,number_links,number_node):



def main():

    file = open("Flickr-test", "r+")
    file_res = open("File_res", "a")
    graph= file.read().splitlines()
    g_original = load_graph(graph)
    delete_loop(g_original)

    #print(g_original)

    sample = adjacency_matrix_from_graph(g_original)
    node1="118"
    node2="6"
    test_num=2

    if link_exists(node1,node2,g_original):
        add_link(node1,node2,sample)
        write_line(file_res,test_num,node1,node2)
        write_line(file_res,test_num,node1,node2)


    #print(link_exists(node1,node2,g_original))
    #print(sample)

    #print(analyse_random(3,3,50))
    absolute_efficiency(file_res,3)







if __name__ == '__main__':
    main()