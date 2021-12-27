Null = -1


class Node:

    def __init__(self, data=Null, next=Null, dnext=Null):
        self.data = data
        self.next = next
        self.dnext = dnext


class ArrayLinkedList:

    def __init__(self, capacity):
        self.capacity = capacity
        self.n = [Node()] * self.capacity
        self.head = Null
        self.current = Null
        self.deleted = Null
        self.max = Null
        self.no = 0

    def __len__(self):
        return self.no

    def get_insert_index(self):
        if self.deleted == Null:
            if self.max + 1 < self.capacity:
                self.max += 1
                return self.max
            else:
                return Null
        else:
            rec = self.deleted
            self.deleted = self.n[rec].dnext
            return rec

    def delete_index(self, idx):
        if self.deleted == Null:
            self.deleted = idx
            self.n[idx].dnext = Null

        else:
            rec = self.deleted
            self.deleted = idx
            self.n[idx].dnext = rec

    def search(self, data):
        cnt = 0
        ptr = self.head

        while ptr != Null:
            if self.n[ptr].data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = self.n[ptr].next
        return Null

    def __contains__(self, data):
        return self.search(data) >= 0

    def add_first(self, data):
        ptr = self.head
        rec = self.get_insert_index()
        if rec != Null:
            self.head = self.current = rec
            self.n[rec] = Node(data, ptr)
            self.no += 1

    def add_last(self, data):
        if self.head == Null:
            self.add_first(data)
        else:
            ptr = self.head
            rec = self.get_insert_index()

            if rec != Null:
                while self.n[ptr].next != Null:
                    ptr = self.n[ptr].next

                self.n[ptr].next = self.current = rec
                self.n[rec] = Node(data)
                self.no += 1

    def remove_first(self):
        if self.head != Null:
            ptr = self.n[self.head].next
            self.delete_index(self.head)
            self.head = self.current = ptr
            self.no -= 1

    def remove_last(self):
        if self.head != Null:
            if self.n[self.head].next == Null:
                self.remove_first()
            else:
                ptr = self.head
                pre = self.head
                while self.n[ptr].next != Null:
                    pre = ptr
                    ptr = self.n[ptr].next
                self.delete_index(ptr)
                self.n[pre].next = Null
                self.current = pre
                self.no -= 1

    def remove(self, p):
        if self.head != Null:
            if p == self.head:
                self.remove_first()
            else:
                ptr = self.head

                while self.n[ptr].next != p:
                    ptr = self.n[ptr].next
                    if ptr == Null:
                        return Null

                self.n[ptr].next = self.n[p].next
                self.delete_index(p)
                self.current = ptr
                self.no -= 1

    def remove_current_node(self):
        if self.current != Null:
            self.remove(self.current)

    def clear(self):
        while self.head != Null:
            self.remove_first()
        self.current = Null
        self.no = 0

    def next(self):
        if self.current == Null or self.n[self.current].next == Null:
            return False
        self.current = self.n[self.current].next
        return True

    def print_current_node(self):
        if self.current == Null:
            print('주목 노드가 없습니다.')
        else:
            print(self.n[self.current].data)

    def print(self):
        ptr = self.head

        while ptr != Null:
            print(self.n[ptr].data)
            ptr = self.n[ptr].next

    def dump(self):
        for i in self.n:
            print(f'[{i}] {i.data} {i.next} {i.dnext}')

    def __iter__(self):
        return ArrayLinkedListIterator(self.n, self.head)


class ArrayLinkedListIterator:

    def __init__(self, n, head):
        self.n = n
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == Null:
            raise StopIteration
        else:
            data = self.n[self.current].data
            self.current = self.n[self.current].next
            return data
