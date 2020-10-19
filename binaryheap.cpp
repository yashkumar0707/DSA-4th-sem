#include<iostream> 
#include<climits> 
using namespace std; 
  
// Prototype of a utility function to swap two integers 
void swap(int *x, int *y); 
  
class BinHeap 
{ 
    int *harr; // pointer to array of elements in heap 
    int capacity; // maximum possible size of min heap 
    int heap_size; // Current number of elements in min heap 
public: 
    MinHeap(int capacity);  
    void MinHeapify(int ); 
    int parent(int i) { return (i-1)/2; }  
    int left(int i) { return (2*i + 1); } 
    int right(int i) { return (2*i + 2); }  
    void decreaseKey(int i, int new_val); 
    int getMin() { return harr[0]; } 
    void insertKey(int k); 
}; 
    void MinHeap::insertKey(int k) 
{ 
    if (heap_size == capacity) 
    { 
        cout << "\nOverflow: Could not insertKey\n"; 
        return; 
    } 
  
    // First insert the new key at the end 
    heap_size++; 
    int i = heap_size - 1; 
    harr[i] = k; 
  
    // Fix the min heap property if it is violated 
    while (i != 0 && harr[parent(i)] > harr[i]) 
    { 
       swap(&harr[i], &harr[parent(i)]); 
       i = parent(i); 
    } 
} 