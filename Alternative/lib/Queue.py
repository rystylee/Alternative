##　------------------------------------------------------------------------------

## Queue.py
## Queue that manages arrays

##　------------------------------------------------------------------------------


class Queue(object):
    def __init__(self, queue=None):
        if type(queue) is type([]):
            self._queue = queue
        elif queue is None:
            self._queue = []
        else:
            print("Error Message: Your input is not type of list")


    def enqueue(self, *lists):
        for li in lists:
            self._queue.append(li)


    def dequeue(self):
        first_list = []
        if not len(self._queue) == 0:
            first_list = self._queue[0]
            del self._queue[0]
        # else:
            # print("queue is empty")

        return first_list


    def is_Empty(self):
        return not(bool(self._queue))


    def reset_queue(self, *original_durations):
        self.clear()
        self.enqueue(*original_durations)


    def clear(self):
        self._queue.clear()


    def show_queue(self):
        print(self._queue)
