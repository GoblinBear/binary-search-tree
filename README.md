# Binary Search Tree

## Run

```shell
$ python3 bst.py
```

Features:
- `insert()`
- `search()`
- `delete()`
- `display()`

```python
bst = BST()
bst.insert(24)
bst.insert(28)
bst.insert(26)
bst.insert(27)
bst.insert(25)
bst.insert(12)
bst.insert(18)
bst.insert(15)
bst.insert(20)
bst.insert(35)
bst.insert(42)
bst.insert(40)
bst.insert(33)
bst.insert(30)
bst.insert(34)
bst.insert(49)

bst.display()
```
```
                                24                                                              

                12                              28                              

        --              18              26              35              

    --      --      15      20      25      27      33      42      

  --  --  --  --  --  --  --  --  --  --  --  --  30  34  40  49
```

### Run Tests

```shell
$ python3 -m unittest -v tests/test_bst.py
```

## File Structure

```
📦bst
 ┣ 📂tests
 ┃ ┗ 📜test_bst.py
 ┗ 📜bst.py
```
- `bst.py`: The data structure of binary search tree.
