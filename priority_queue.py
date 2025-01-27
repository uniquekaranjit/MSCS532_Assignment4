# ----------------------------------------------------------------------------------------------------------------------
# Priority Queue Algorithm
# Description: This Python code implements the priority Queue Algorithm - max-heap (highest priority first) 
# Author: Unique Karanjit
# Date: 2025-01-25
# ----------------------------------------------------------------------------------------------------------------------

class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline
        
    def __repr__(self):
        return f"Task ID: {self.task_id}, Priority: {self.priority}, Arrival Time: {self.arrival_time}, Deadline: {self.deadline}"



class MaxHeapPriorityQueue:
    def __init__(self):
        self.heap = []
    
    # Insert a new task into the heap
    def insert(self, task):
        if task is None:  # Check if task is None before inserting
            print("Cannot insert None as a task.")
            return
        self.heap.append(task)
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index].priority < self.heap[index].priority:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break
    
    # Extract the task with the highest priority (max-heap)
    def extract_max(self):
        if not self.heap:
            print("Priority Queue is empty, cannot extract.")
            return None

        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return root
    
    # Helper function to maintain heap property by bubbling down
    def heapify_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index
        
        if left_child < len(self.heap) and self.heap[left_child].priority > self.heap[largest].priority:
            largest = left_child
        if right_child < len(self.heap) and self.heap[right_child].priority > self.heap[largest].priority:
            largest = right_child
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)
    
    # Increase the priority of a given task (bubble up)
    def increase_key(self, task, new_priority):
        if task is None:  # Ensure task is valid before modifying
            print("Cannot increase key for None.")
            return
        task.priority = new_priority
        index = self.heap.index(task)
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index].priority < self.heap[index].priority:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break


        
    
    # Check if the priority queue is empty
    def is_empty(self):
        return len(self.heap) == 0


            

# ----------------------------------------------------------------------------------------------------------------------
# Driver Code
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    pq = MaxHeapPriorityQueue()

    print("\n\n---------------------------------------------")
    print("Priority Queue before inserting any tasks:")
    print(pq.heap)
    print("---------------------------------------------")
    
    # Create some tasks with different priorities
    task1 = Task(1, 5, "10:00", "12:00")
    task2 = Task(2, 2, "11:00", "13:00")
    task3 = Task(3, 8, "12:00", "14:00")
    task4 = Task(4, 10, "13:00", "15:00")
    
    # Insert tasks into the priority queue
    pq.insert(task1)
    pq.insert(task2)
    pq.insert(task3)
    pq.insert(task4)
    
    print("\n\n---------------------------------------------")
    print("Priority Queue after inserting tasks:")
    print(pq.heap) 
    print("---------------------------------------------")
    
    # Extract the task with the highest priority
    print("\n\n---------------------------------------------")
    print("Extracting max priority task:")
    max_task = pq.extract_max()
    print(f"Extracted: {max_task}")
    print("---------------------------------------------")
    
    # Increase priority of a task
    print("\n\n---------------------------------------------")
    pq.increase_key(task2, 12)
    print("Priority Queue after increasing priority of task2:")
    print(pq.heap)
    print("---------------------------------------------")
    
    # Check if the priority queue is empty
    print("\n\n---------------------------------------------")
    print("Is the priority queue empty?")
    print(pq.is_empty())
    print("---------------------------------------------")
