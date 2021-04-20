import pyUnionFind as uf

foo = uf.DisjointSets(10)
assert foo.size() == 10

assert foo.rank(0) == 0

foo.unite(0, 1)

assert foo.same(0, 1)
assert foo.same(1, 0)
assert foo.rank(0) == 1

assert not foo.same(0, 2)


