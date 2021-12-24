class FixedStack:

    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity = 256):
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0
    
    def __len__(self):
        return self.ptr
    
    def is_empty(self):
        return self.ptr <= 0
    
    def is_full(self):
        return self.ptr >= self.capacity
    
    def push(self, value):
        if self.is_full():
            raise FixedStack.Full
        else:
            self.stk[self.ptr] = value
            self.ptr += 1
    
    def pop(self):
        if self.is_empty():
            raise FixedStack.Empty
        else:
            self.ptr -= 1
            return self.stk[self.ptr]
    
    def peek(self):
        if self.is_empty():
            raise FixedStack.Empty
        else:
            return self.stk[self.ptr -1]
    
    def clear(self):
        self.ptr = 0

    def find(self, value):
        for i in range(self.ptr-1,-1,-1):
            if self.stk[i] == value:
                return i
        return -1
    
    def count(self, value):
        cnt = 0
        for i in range(self.ptr - 1,-1,-1):
            if self.stk[i] == value:
                cnt += 1
        return cnt

    def __contains__(self, value):
        return self.count(value) > 0
    
    def dump(self):
        if self.is_empty():
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])