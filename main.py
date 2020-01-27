class queue:
    def __init__(self, items):
        self.queue = items
        self.maxSize = len(items)
        self.head = 0
        self.tail = -1
        self.size = len(items)

    def isFull(self):
        if self.size == self.maxSize:
            return True
        else:
            False

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def enqueue(self, data):
        if self.isFull():
            return ("Queue Full")
        else:
            self.tail = (self.tail+1) % self.maxSize
            self.queue[self.tail] = data
            self.size += 1
            return ("Queued: " + str(data) + ". Queue --> " + str(self.queue))

    def dequeue(self):
        if self.isEmpty():
            return ("Queue Empty")
        else:
            data = self.queue[self.head]
            self.queue[self.head] = ''
            self.head = (self.head +1) % self.maxSize
            self.size -= 1
            return ("Dequeued: " + str(data) + ". Queue --> " + str(self.queue)) 
