pyUnionFInd
==============

pyUnionFind offers a Union-Find data structure (aka disjoint sets) with path compression and union by rank. 

It is [pybind11](https://github.com/pybind/pybind11) wrapper around [Wenzel Jakob's](https://github.com/wjakob) header-only [C++11 implementation](https://github.com/wjakob/dset).

Installation
------------

**On Unix (Linux, OS X)**

 - clone this repository
 - `pip install .`
 
Uninstall via `pip uninstall pyUnionFind`. 

Usage
---------
```python
foo = pyUnionFind.DisjointSets(m)
```
creates a UnionFind data structure `foo` consisting of `m` disjoint subsets.

```python
foo.unite(a,b)
``` 
merges subsets `a, b` into a single subset.

```python
foo.find(a)
``` 
returns the "representative" of the subset that `a` is an element of.  

```python
foo.same(a,b)
``` 
returns `True` iff `a, b` belong to the same single subset.


Example
---------

```python
import pyUnionFind as m

# foo = { {0}, {1}, {2}, {3}, {4} }
foo = m.DisjointSets(5)
print(foo)

foo.rank(0)
foo.parent(1)
foo.same(0,1)
foo.find(0)
foo.find(1)

# join sets {0} and {1}
foo.unite(0,1)

# foo = { {0, 1}, {2}, {3}, {4} } 
foo.rank(0)
foo.parent(1)
foo.same(0,1)
foo.find(0)
foo.find(1)
```

