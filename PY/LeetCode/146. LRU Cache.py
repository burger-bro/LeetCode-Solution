from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            ret = self.cache[key]

            del self.cache[key]
            self.cache[key] = ret

        else:
            ret = -1
        
        print("get:", ret)
        return ret

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) >= self.capacity:
            del self.cache[next(iter(self.cache.keys()))]
        self.cache[key] = value

        print("put:", self.cache)

    # def put(self, key: int, value: int) -> None:
    #     if len(self.cache) < self.capacity:
    #         if key in self.cache:
    #             del self.cache[key]
    #             self.cache[key] = value
    #         else:
    #             self.cache[key] = value
    #     else:
    #         # for i in self.cache.keys():
    #         #     print(i)
    #         # print(next(iter(self.cache.keys())))
    #         if key in self.cache:
    #             del self.cache[key]
    #             self.cache[key] = value
    #         else:
    #             del self.cache[next(iter(self.cache.keys()))]
    #             self.cache[key] = value
    #     print("put:", self.cache)
        

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    def get(self, key:int)->int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1
    def put(self, key, value):
        if key in  self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            self.cache[key] = value
        if len(self.cache)>self.capacity:
            self.cache.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# case1
capacity = 2
obj = LRUCache(capacity)
obj.put(1, 1)
obj.put(2, 2)
obj.get(1)
obj.put(3, 3)
obj.get(2)
obj.put(4, 4)
obj.get(1)
obj.get(3)
obj.get(4)
# case2
capacity = 1
obj = LRUCache(capacity)
obj.get(0)
obj.put(1, 1)
obj.put(2, 2)
obj.put(3, 3)


