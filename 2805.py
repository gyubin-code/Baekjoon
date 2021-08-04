n,m = map(int, input().split())


max_tree_tall = 2,000,000,000

max_tree_cnt =1,000,000
tree=list(map(int,input().split())) #s내가 받은 나무들





left =0
right = max(tree)
mid =(left+right)/2
while(left<=right):
    mid =int((left+right)/2)
    
    get_tree =0
    for i in range(len(tree)):
        if(tree[i]>mid):
            get_tree+=(tree[i]-mid)
    if(get_tree>=m):
        left = mid+1
    else:
        right = mid-1
print(right)