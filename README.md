# MSCS532_Assignment4

## Overview
This repository contains an implementation of the **Heap Sort** algorithm and the implementation of a **Priority Queue**. The project includes Python scripts to demonstrate the behavior and performance of these two algorithms, with visual outputs generated as evidence.

The primary components of the project are:
- Heapsort implementation with runtime data evidence.
- Comparision between heap sort, merge and quick sort algorithm with graph visualized evidence for runtime. 
- Priority Queue Implementation with Insert/Extract operation. 

## Project Structure

- **evidences/**: A directory containing images that showcase the results of the algorithms.
  - `comparing_sorting_algo.png`: The runtime graph generated by `algorithms_compare.py`, depicting the three algorithm’s performance - heap sort, merge sort and quick sort. The array used is sorted array. 
  - `heap_sort_evidence.png`: The output of a sample array being sorted using heapsort generated from `heap_sort.py`.
  - `priority_queue_evidence.png`: The output generated from `priority_queue.py` showing insertion, extraction, priority increase and nullness of the queue. 

- **heap_sort.py**: Python script that performs an implementation of the **Heap QuickSort** algorithm. It generates sorted array for a sample unsorted array defined within the code.  
  
- **priority_queue.py**: Python script that implements a **Priority Queue** implementation. 

- **algorithms_compare.py**: Python script that analyzes a **Heapsort, MergeSort and QuickSort** algorithms. 

- **merge_sort.py**: Helper Python script used by **algorithms_compare.py** to analyze sorting algorithms.

- **quick_sort.py**: Helper Python script used by **algorithms_compare.py** to analyze sorting algorithms.

- **HeapSort_PriorityQueue_Analysis_Report.pdf**: A report regarding the analysis/implementation of heapsort and priority queue.  

- **requirements.txt**: A file containing the dependencies required to run the Python code. Use this file to set up the Python environment.

## Getting Started

To get started with the project, follow the instructions below to set up your environment and run the Python scripts.

### 1. Install dependencies:
The project requires several Python libraries that are listed in `requirements.txt`. You can install them using `pip`. Run the following command to install the dependencies:
```bash
pip install -r requirements.txt
```

### 2. Run Python Code:
Run the following command to run `heap_sort`:
```bash
python3 heap_sort.py
```

Run the following command to run `priority_queue`:
```bash
python3 priority_queue.py
```

Run the following command to run `algorithms_compare`:  
*Note: This is just a helper code to compare Heapsort, Quicksort and Mergesort.*
```bash
python3 algorithms_compare.py
```



