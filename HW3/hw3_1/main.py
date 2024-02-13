import time
import random
import matplotlib.pyplot as plt
import numpy as np


# Insertion sort algorithm
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# merge sort algorithm
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Time measurer
def measure_time(sort_function, data):
    start_time = time.perf_counter()
    sort_function(data)
    end_time = time.perf_counter()
    return end_time - start_time



def plot_runtimes():
    # Create a list for each size of data to measure
    sizes = [n for n in range(10, 110)]
    insertion_times = []
    merge_times = []

    # For each size
    for size in sizes:
        #Create a list of data of length size
        data = [random.randint(0, 100) for n in range(size)]

        # Measure the time it takes for insertion sort to sort data
        insertion_time = measure_time(insertion_sort, data.copy())
        insertion_times.append(insertion_time * 100)

        # Measure the time it takes for merge sort to sort data
        merge_time = measure_time(merge_sort, data.copy())
        merge_times.append(merge_time * 100)

    # Create a line of best fit of degree 2 for insertion sort
    # and plot the line with a blue dashed line
    insertion_coefficients = np.polyfit(sizes, insertion_times, 2)
    insertion_line = np.poly1d(insertion_coefficients)
    plt.plot(sizes, insertion_line(sizes), linestyle='--', color='blue')

    # Create a line of best fit of degree 2 for insertion sort
    # and plot the line with an orange dashed line    
    merge_coefficients = np.polyfit(sizes, merge_times, 1)
    merge_line = np.poly1d(merge_coefficients)
    plt.plot(sizes, merge_line(sizes), linestyle='--', color='orange')

    # Solve for the intersection points of each line of best fit 
    intersection_x = np.roots(insertion_line - merge_line)
    intersection_y = insertion_line(intersection_x)
    
    # Plot each insertion time at each size for insertion and merge sort
    plt.scatter(sizes, insertion_times, label='Insertion Sort')
    plt.scatter(sizes, merge_times, label='Merge Sort')

    # Plot the intersection point and its x location
    plt.plot(intersection_x[0], intersection_y[0], color = 'black', marker='d', markersize=10)
    plt.text(intersection_x[0], intersection_y[0], f'({intersection_x[0]:.2f} inputs', fontsize=12,
             ha='left', va='bottom', color='black')
    
    # Label axis and legend
    plt.xlabel('Input Size')
    plt.ylabel('Runtime (seconds)')
    plt.title('Insertion Sort vs Merge Sort Runtime')
    plt.xticks(np.arange(min(sizes), max(sizes) + 1, 10))
    plt.legend()
    plt.show()

def average_intersection(n):
    # Create a list for each size of data to measure
    sizes = [n for n in range(10, 110)]
 
    intersection_inputs = []

    # Run N trials
    for n in range(n):
        insertion_times = []
        merge_times = []
        # For each size
        for size in sizes:
            #Create a list of data of length size
            data = [random.randint(0, 100) for n in range(size)]

            # Measure the time it takes for insertion sort to sort data
            insertion_time = measure_time(insertion_sort, data.copy())
            insertion_times.append(insertion_time * 100)

            # Measure the time it takes for merge sort to sort data
            merge_time = measure_time(merge_sort, data.copy())
            merge_times.append(merge_time * 100)

        # Create a line of best fit of degree 2 for insertion sort
        insertion_coefficients = np.polyfit(sizes, insertion_times, 2)
        insertion_line = np.poly1d(insertion_coefficients)

        # Create a line of best fit of degree 1 for insertion sort
        merge_coefficients = np.polyfit(sizes, merge_times, 1)
        merge_line = np.poly1d(merge_coefficients)

        # Solve for the intersection points of each line of best fit 
        intersection_x = np.roots(insertion_line - merge_line)

        # Add the x coordinate of the intersection to a list
        intersection_inputs.append(intersection_x)

        # Get the average of items in the list
    return (sum(intersection_inputs) / len(intersection_inputs))[0]
    
  

if __name__ == "__main__":
    # plot_runtimes()
    print(average_intersection(1000))
