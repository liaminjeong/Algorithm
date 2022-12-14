import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
tree = {} #딕셔너리(사전형태) key,value로 이루어짐
for i in range(n):
    root,left,right = sys.stdin.readline().strip().split()
    tree[root] = [left,right]

def preorder(root):
    if root !='.':
        print(root,end='')
        preorder(tree[root][0]) #left
        preorder(tree[root][1]) #right

def inorder(root):
    if root !='.':
        inorder(tree[root][0]) #left
        print(root,end='')
        inorder(tree[root][1]) #right

def postorder(root):
    if root !='.':
        postorder(tree[root][0]) #left
        postorder(tree[root][1]) #right
        print(root,end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')

    