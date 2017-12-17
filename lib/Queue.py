class Queue(object):
    def __init__(self, queue=None):
        if type(queue) is type([]):
            self.queue = queue
        elif queue is None:
            self.queue = []
        else:
            print("Error Message: Your input is not type of list")


    def enqueue(self, *lists):
        for li in lists:
            self.queue.append(li)


    def dequeue(self):
        first_list = []
        if not len(self.queue) == 0:
            first_list = self.queue[0]
            del self.queue[0]
        # else:
            # print("queue is empty")

        return first_list


    def is_Empty(self):
        return not(bool(self.queue))


    def reset_queue(self, *original_durations):
        self.clear()
        self.enqueue(*original_durations)


    def clear(self):
        self.queue.clear()


    def show_queue(self):
        print(self.queue)
