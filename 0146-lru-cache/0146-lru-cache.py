import queue

class Node:
  _next = None
  _prev = None
  def __init__(self, val):
    self._val = val
  
  def __str__(self):
    s = f"cur={self._val}"
    if self._prev:
      s = f"prev={self._prev._val} {s}"
    if self._next:
      s = f"{s} next={self._next._val}"
    return s
class Deque:
  _head = None
  _tail = None

  def __str__(self):
    node = self._head
    l = []
    while node:
      l.append(f"{node._val[0]} -> {node._val[1]}")
      node = node._next
    return ", ".join(l)
  
  def remove_last(self):
    el = self._tail
    # print(f"removing tail")
    # print(f"tail {self._tail} head {self._head}")
    if el:
      # print(f"tail found {el}")
      if el._prev:
        el._prev._next = None
        self._tail = el._prev
        # print(f"head is not last")
      else:
        # print("resetting all")
        self._tail = None
        self._head = None
      # print(f"state after removing end head({self._head}), tail({self._tail})")
      # print("remove end")
      return el
    else:
      # print("remove end")
      return None 

  def add_to_head(self, val):
    new_node = Node(val)
    if self._head:
      new_node._next = self._head
      self._head._prev = new_node
      self._head = new_node
    else:
      self._head = new_node
      self._tail = new_node
    # print(f"state after adding {val} to head: head({self._head}), tail({self._tail})")
    return new_node
  
  def move_to_head(self, node):
    # print(f"moving to head start")
    # print(f"moving node {node}")
    # print(f"state before: head({self._head}), tail({self._tail})")
    if self._head == node:
      return
    # Make prev node point to next after
    # And if exists make next node pointing to prev and adjust tail
    node._prev._next = node._next
    if node._next:
      # print("it's not last node removed")
      node._next._prev = node._prev
    else:
      # print("it's last node moved")
      self._tail = node._prev
    # Make prev head next to current node, move it head and reset prev
    node._next = self._head
    self._head._prev = node
    self._head = node
    node._prev = None
    # print(f"state after: head({self._head}), tail({self._tail})")
    # print(f"moving to head end")

class LRUCache:
    def __init__(self, capacity: int):
      self._capacity = capacity
      self._usage_list = Deque()
      self._map = {}

    def get(self, key: int) -> int:
      # print()
      # print(f"get {key}")
      # print()
      if key in self._map:
        node = self._map[key]
        self._usage_list.move_to_head(node)
        return node._val[1]
      return -1
        

    def put(self, key: int, value: int) -> None:
      # print()
      # print(f"put {key} {value}")
      # print()
      if key in self._map:
        node = self._map[key]
        upd = (node._val[0], value)
        node._val = upd
        self._usage_list.move_to_head(node)
      elif key not in self._map:
        new_node = self._usage_list.add_to_head((key, value))
        self._map[key] = new_node 
        if len(self._map) == self._capacity + 1:
          old_node = self._usage_list.remove_last()
          # print(f"remove returns {old_node}")
          del self._map[old_node._val[0]]

        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# obj.put(key,value)
# param_1 = obj.get(key)