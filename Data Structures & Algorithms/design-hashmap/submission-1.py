class MyHashMap:

    def __init__(self):
        self.items = {}
        

    def put(self, key: int, value: int) -> None:
        self.items[key] = value
        

    def get(self, key: int) -> int:
        if key in self.items:
            return self.items[key]
        return -1
        

    def remove(self, key: int) -> None:
        if key in self.items:
            del self.items[key]
        
 

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)