# emergency_queue.py
# Implementation of an Emergency Room Patient Queue using a Min-Heap

class Patient:
    """Represents an emergency room patient with a name and urgency level."""
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency  # 1 = most urgent, 10 = least urgent

    def __repr__(self):
        return f"{self.name} ({self.urgency})"


class MinHeap:
    """Custom min-heap to manage patient intake order."""
    def __init__(self):
        self.data = []

    def insert(self, patient):
        """Insert a new patient and maintain heap order."""
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def heapify_up(self, index):
        """Move the inserted patient up to maintain heap property."""
        parent_index = (index - 1) // 2
        if index > 0 and self.data[index].urgency < self.data[parent_index].urgency:
            self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
            self.heapify_up(parent_index)

    def heapify_down(self, index):
        """Reorder heap after removing the root."""
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency:
            smallest = left
        if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
            smallest = right

        if smallest != index:
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            self.heapify_down(smallest)

    def peek(self):
        """Return the most urgent patient without removing them."""
        return self.data[0] if self.data else None

    def remove_min(self):
        """Remove and return the most urgent patient."""
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()

        root = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return root

    def print_heap(self):
        """Display current patient queue."""
        print("\nCurrent Queue:")
        for p in self.data:
            print(f"- {p.name} ({p.urgency})")


# Example usage
if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()

    next_up = heap.peek()
    print(f"\nNext up: {next_up.name} ({next_up.urgency})")

    served = heap.remove_min()
    print(f"\nServed: {served.name}")
    heap.print_heap()
