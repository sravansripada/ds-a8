import uuid
import random


# implement queue


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def isEmpty(self):
        return self.items == []

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# Implement Stack


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


# Printer simulation

class Printer:
    def __init__(self, print_time):
        self.print_time = print_time
        self.time = 0
        self.printing_task = None
        self.running_time = 0
        self.is_running = False

    def get_is_running(self):
        return self.is_running

    def increment_running_time(self):
        self.running_time += 1

    def update_task_completed_timestamp(self):
        if self.printing_task is not None:
            self.printing_task.set_completed_timestamp(self.time)
        else:
            raise Warning('No task to update')

    def increment_time(self):
        self.time += 1

    def reset_running_time(self):
        self.running_time = 0

    def submit_task(self, task):
        self.printing_task = task
        self.is_running = True

    def is_task_complete(self):
        if self.printing_task is not None:
            if self.running_time == self.printing_task.get_num_pages() * self.print_time:
                return True
            else:
                return False

    def set_is_running(self, flag):
        self.is_running = flag

    def reset_printing_task(self):
        self.printing_task = None

    def get_printing_task(self):
        return self.printing_task


class PrintingTask:
    def __init__(self, timestamp_created, num_pages):
        self.task_id = uuid.uuid1()
        self.timestamp_created = timestamp_created
        self.timestamp_completed = None
        self.num_pages = num_pages

    def set_timestamp_completed(self, timestamp_completed):
        self.timestamp_completed = timestamp_completed

    def get_timestamp_completed(self):
        return self.timestamp_completed

    def get_timestamp_created(self):
        return self.timestamp_created

    def get_num_pages(self):
        return self.num_pages


def simulation(print_time, num_seconds):
    q = Queue()
    time_queue = []
    printer = Printer(print_time=print_time)
    for second in range(num_seconds):

        printer.increment_time()

        if random.randrange(1, 181) == 180:
            printing_task = PrintingTask(timestamp_created=second, num_pages=random.randrange(1, 21))
            q.enqueue(printing_task)

        if printer.get_is_running():
            printer.increment_running_time()
            if printer.is_task_complete():
                printer.get_printing_task().set_timestamp_completed(second)
                time_queue.append(
                    printer.get_printing_task().get_timestamp_completed() - printer.get_printing_task().get_timestamp_created())
                printer.reset_running_time()
                printer.set_is_running(False)
                printer.reset_printing_task()

        else:
            if q.isEmpty():
                pass
            else:
                printer.submit_task(q.dequeue())
                printer.increment_running_time()

    print((sum(time_queue) * 1.0) / (len(time_queue) * 1.0))


for i in range(10):
    simulation(5, 3600)
