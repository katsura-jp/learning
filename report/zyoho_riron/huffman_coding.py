import json
import math
import argparse


class Node:  
    def __init__(self, left, right):
        self.name = '({} + {})'.format(left.name, right.name)
        self.p = left.p + right.p
        self.left = left
        self.right = right
        self.__signal = None
    
    @property
    def signal(self):
        return self.__signal
    
    @signal.setter
    def signal(self, signal):
        self.__signal = signal
 
        
class Leaf:
    def __init__(self, name, p):
        self.name = name
        self.p = p
        self.__signal = None
        
    @property
    def signal(self):
        return self.__signal
    
    @signal.setter
    def signal(self, signal):
        self.__signal = signal


def give_signal(node):
    if isinstance(node, Node):
        node.left.signal = node.signal + str(0)
        node.right.signal = node.signal + str(1)
        give_signal(node.left)
        give_signal(node.right)

def ave_codeword_length(leafs):
    result = 0
    for leaf in leafs:
        result += len(leaf.signal) * leaf.p
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, default=None,help='give frequency json file')
    args = parser.parse_args()
    if args.file is None:
      raise("give file path \n [usage] python huffman_coding.py --file <JSON file>")

    with open(args.file, 'r') as f:
        frequency = json.load(f)

    leafs = [Leaf(name, p) for name, p in frequency.items()]

    nodes = {leaf.name:{'p':leaf.p, 'node': leaf} for leaf in leafs}

    while(len(nodes) > 1):
        for i, (k, v) in enumerate(sorted(nodes.items(), key=lambda x: x[1]['p'])):
            if i == 0:
                left = v['node']
                nodes.pop(k)
            elif i == 1:
                right = v['node']
                nodes.pop(k)
            else:
                break
        new_node = Node(left, right)
        nodes[new_node.name] = {'p' : new_node.p, 'node': new_node}
    root = list(nodes.values())[0]['node']
    root.signal = ''


    give_signal(root)
    print('===  ハフマン符号化  ===')
    for leaf in leafs:
        print('{} : {}'.format(leaf.name, leaf.signal))
    print('========================')
    
    print('平均符号語長: {}'.format(ave_codeword_length(leafs)))


if __name__ == '__main__':
    main()
