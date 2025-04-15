from collections import deque

class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.cnt = 0
        self.queue = deque([])
        self.cur_packet = set([])

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.cur_packet:
            return False
        else:
            if len(self.queue)>self.limit:
                self.forwardPacket()
            self.cnt += 1
            self.cur_packet.add(packet)
            self.queue.append(packet)
            return True

    def forwardPacket(self) -> List[int]:
        if self.queue:
            packet = self.queue.popleft()
            forward = list(packet)
            self.cur_packet.remove(packet)
            self.cnt -= 1
        else:
            forward = []
        return forward

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        cnt = 0
        for q in self.queue:
            if q[1] == destination and startTime <= q[2] <= endTime:
                cnt += 1
        return cnt


class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.cnt = 0
        self.queue = deque([])
        self.cur_packet = set([])
        self.pack_tree :dict[set] = {}

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.cur_packet:
            return False
        else:
            if len(self.queue)==self.limit:
                self.forwardPacket()
            self.cnt += 1
            self.cur_packet.add(packet)
            self.queue.append(packet)
            if destination not in self.pack_tree:
                self.pack_tree[destination] = {timestamp:1}
            else:
                self.pack_tree[destination][timestamp] = self.pack_tree[destination].get(timestamp, 0)+1
            return True

    def forwardPacket(self) -> List[int]:
        if self.queue:
            packet = self.queue.popleft()
            forward = list(packet)
            self.cur_packet.remove(packet)
            self.cnt -= 1
            self.pack_tree[packet[1]][packet[2]] -= 1
        else:
            forward = []
        return forward

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        cnt = 0
        for ts_cnt in self.pack_tree[destination].keys():
            if startTime <= ts_cnt <= endTime:
                cnt += self.pack_tree[destination][ts_cnt]
        return cnt

class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.cnt = 0
        self.queue = deque([])
        self.cur_packet = set([])
        self.pack_tree :dict[set] = {}

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.cur_packet:
            return False
        else:
            if len(self.queue)==self.limit:
                self.forwardPacket()
            self.cnt += 1
            self.cur_packet.add(packet)
            self.queue.append(packet)
            if destination not in self.pack_tree:
                self.pack_tree[destination] = deque([timestamp])
            else:
                self.pack_tree[destination].append(timestamp)
            return True

    def forwardPacket(self) -> List[int]:
        if self.queue:
            packet = self.queue.popleft()
            forward = list(packet)
            self.cur_packet.remove(packet)
            self.cnt -= 1
            self.pack_tree[packet[1]].popleft()
        else:
            forward = []
        return forward

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        cnt = 0
        count_list = self.pack_tree[destination]
        l, r = 0, len(count_list)-1
        begin, end = 0, 0
        while l<=r:
            mid = l+(r-l)//2
            if(count_list[mid] > startTime):
                r = mid-1
            else:
                begin = mid
                mid = l+1

        l, r = 0, len(count_list)-1       
        while l<=r:
            mid = l+(r-l)//2
            if(count_list[mid] > endTime):
                end = mid
                r = mid-1
            else:
                mid = l+1
        return end - begin + 1


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)