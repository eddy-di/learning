# LIFO - Last In - First Out (stacks where you get the last one) ex with browsing session
browsing_session = []
browsing_session.append(1) # adds page
browsing_session.append(2)
browsing_session.append(3)
browsing_session.pop() # removes the last session
if not browsing_session:
    browsing_session([-1]) 
print(browsing_session)

# FIFO First In - First Out (Queues where you get the first one) ex with queue and deque class
from collections import deque #deque is a class object from collections (have no idea what the heck is that)
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")
