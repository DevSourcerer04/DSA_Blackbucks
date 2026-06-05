def sumRange (self, left:int, right:int) -> int:
    return self.query(0, self.tree, 0, self.n-1, left, right)

def query (self, node, tree, start, end, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    leftvalue = self.query(2*node+1, tree, start, mid, left, right)
    rightvalue = self.query(2*node+2, tree, mid+1, end, left, right)
    return leftvalue + rightvalue

