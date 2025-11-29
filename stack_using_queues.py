from collections import deque

class myStack:
    
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        
    def push(self, x):
        # Push x first in empty q2
        self.q2.append(x)
        
        # Push all the remaining
        # elements in q1 to q2.
        while len(self.q1) != 0:
            self.q2.append(self.q1[0])
            self.q1.popleft()
        
        # swap the names of two queues
        self.q1, self.q2 = self.q2, self.q1
        
    def pop(self):
        # if no elements are there in q1
        if len(self.q1) == 0:
            return
        self.q1.popleft()
        
    def top(self):
        if len(self.q1) == 0:
            return -1
        return self.q1[0]
        
    def size(self):
        return len(self.q1)

    def print(self):
        for i in range(len(self.q1)):
            print(self.q1[i], end="\n")

def main():
    st = myStack()
    while True:
        cmd = int(input("Enter commands:\n 1. To pop \n 2. To push\n 3. To get top\n 4. To get size\n 5. To print the Stack\n 6.To exit\n"))

        if cmd == 1:
            st.pop()
        if cmd == 2:
            x = int(input("Enter value to push\n"))
            st.push(x)
        if cmd == 3:
            print(st.top())
        if cmd == 4:
            print(st.size())
        if cmd == 5:
            st.print()
        if cmd == 6:
            break

main()