import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import time

start = 1
stop = 1000
step = 50
arithmetic_mean = 5
lineWD = 2
markSZ = 6
markWD = 3
frequency = 2

def create_array(n):
    array = []
    for i in range(n):
        array.append(i)
    random.shuffle(array)
    return(array)

def duble_selection_sort(array):
    for i in range(len(array)//2):
        maxy = i
        miny = i
        for j in range(i, len(array) - i):
            if array[j] > array[maxy]:
                maxy = j
            elif array[j] < array[miny]:
                miny = j
        array[i], array[miny] = array[miny], array[i]
        if maxy == i:
            maxy = miny
        array[j], array[maxy] = array[maxy], array[j] 
    return array

def insertion(array):
    for i in range(len(array) - 1):
        j = i - 1
        key = array[i]
        while array[j] > key and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

def sort_selection(array):
    for j in range(len(array)):
        local_max = array[0]
        max_pos = 0
        for i in range(0, len(array) - j, 1):
            if array[i] > local_max:
                max_pos = i
                local_max = array[i]
        array[len(array) - j - 1], array[max_pos] = array[max_pos], array[len(array) - j - 1]
    return array

def odd_even(array):
    length = len(array)
    flag = 0
    while flag == 0:
        flag = 1
        for i in range(1, length - 1, 2):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                flag = 0
                  
        for i in range(0, length - 1, 2):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                flag = 0
    return array

def bubble_sort(array):
    for i in range(len(array) - 1):
        for element in range(len(array) - 1 - i):
            if array[element] > array[element + 1]:
                array[element], array[element + 1] = array[element + 1], array[element]
    return array

def shaker_sort(array): 
    up = range(len(array) - 1)       
    while True:
        for indices in (up, reversed(up)):
            swapped = False
            for i in indices:
                if array[i] > array[i+1]:  
                    array[i], array[i+1] =  array[i+1], array[i]
                    swapped = True
            if not swapped:
                return array

def quick_sort(array):
    less = []
    pivotList = []
    more = []
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        for i in array:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivotList + more
    

def duble_selection_plot(dictionary, start, stop, step, arithmetic_mean):
    for i in range(start, stop, step):
        times = []
        for j in range(arithmetic_mean):
            array = create_array(i)
            start_time = time.time()
            duble_selection_sort(array)
            end_time = time.time()
            times.append(end_time - start_time)
        summ = 0
        for k in times:
            summ += k
        dictionary[i] = summ / len(times)
        print(i, summ / len(times))
    return dictionary    

     
def insertion_plot(dictionary, start, stop, step, arithmetic_mean):
    for i in range(start, stop, step):
        times = []
        for j in range(arithmetic_mean):
            array = create_array(i)
            start_time = time.time()
            insertion(array)
            end_time = time.time()
            times.append(end_time - start_time)
        summ = 0
        for k in times:
            summ += k
        dictionary[i] = summ / len(times)
        print(i, summ / len(times))
    return dictionary
    
    
    
def selection_plot(dictionary, start, stop, step, arithmetic_mean):   
    for i in range(start, stop, step):
        times = []
        for j in range(arithmetic_mean):
            array = create_array(i)
            start_time = time.time()
            sort_selection(array)
            end_time = time.time()
            times.append(end_time - start_time)
        summ = 0
        for k in times:
            summ += k
        dictionary[i] = summ / len(times)
        print(i, summ / len(times))
    return dictionary
    
    
def odd_even_plot(dictionary, start, stop, step, arithmetic_mean):
    for i in range(start, stop, step):
        times = []
        for j in range(arithmetic_mean):
            array = create_array(i)
            start_time = time.time()
            odd_even(array)
            end_time = time.time()
            times.append(end_time - start_time)
        summ = 0
        for k in times:
            summ += k
        dictionary[i] = summ / len(times)
        print(i, summ / len(times))
    return dictionary

def bubble_plot(dictionary, start, stop, step, arithmetic_mean):
    for i in range(start, stop, step):
        times = []
        for j in range(arithmetic_mean):
            array = create_array(i)
            start_time = time.time()
            bubble_sort(array)
            end_time = time.time()
            times.append(end_time - start_time)
        summ = 0
        for k in times:
            summ += k
        dictionary[i] = summ / len(times)
        print(i, summ / len(times))
    return dictionary

def shaker_plot(dictionary, start, stop, step, arithmetic_mean):
    for i in range(start, stop, step):
        times = []
        for j in range(arithmetic_mean):
            array = create_array(i)
            start_time = time.time()
            shaker_sort(array)
            end_time = time.time()
            times.append(end_time - start_time)
        summ = 0
        for k in times:
            summ += k
        dictionary[i] = summ / len(times)
        print(i, summ / len(times))
    return dictionary
    
def quick_sort_plot(dictionary, start, stop, step, arithmetic_mean):
    for i in range(start, stop, step):
        times = []
        for j in range(arithmetic_mean):
            array = create_array(i)
            start_time = time.time()
            quick_sort(array)
            end_time = time.time()
            times.append(end_time - start_time)
        summ = 0
        for k in times:
            summ += k
        dictionary[i] = summ / len(times)
    return dictionary
            

time_bubble = dict()
time_bubble = bubble_plot(time_bubble, start, stop, step, arithmetic_mean)

for i in time_bubble:
    print(i, time_bubble[i])

print('---------------------- It was bubble_sort')

time_shaker = dict()
time_shaker = shaker_plot(time_shaker, start, stop, step, arithmetic_mean)

for i in time_shaker:
    print(i, time_shaker[i])
    
print('---------------------- It was shaker_sort')
    
time_quick = dict()
time_quick = quick_sort_plot(time_quick, start, stop, step, arithmetic_mean)

for i in time_quick:
    print(i, time_quick[i])
    
print('---------------------- It was quick_sort')

time_odd_even = dict()
time_odd_even = odd_even_plot(time_odd_even, start, stop, step, arithmetic_mean)

for i in time_odd_even:
    print(i, time_odd_even[i])
    
print('---------------------- It was odd_even_sort')

time_selection = dict()
time_selection = selection_plot(time_selection, start, stop, step, arithmetic_mean)

for i in time_selection:
    print(i, time_selection[i])
    
print('---------------------- It was selection_sort')

time_insertion = dict()
time_insertion = insertion_plot(time_insertion, start, stop, step, arithmetic_mean)

for i in time_insertion:
    print(i, time_insertion[i])
    
print('---------------------- It was insertion_sort')

time_duble_selection = dict()
time_duble_selection = duble_selection_plot(time_duble_selection, start, stop, step, arithmetic_mean)

for i in time_duble_selection:
    print(i, time_duble_selection[i])
    
print('---------------------- It was duble_selection_sort')

    
x = []
y = []
for i in time_bubble:
    x.append(i)
    y.append(time_bubble[i])
    
x1 = []
y1 = []
for i in time_shaker:
    x1.append(i)
    y1.append(time_shaker[i])
    
x2 = []
y2 = []
for i in time_quick:
    x2.append(i)
    y2.append(time_quick[i])
    
x3 = []
y3 = []
for i in time_odd_even:
    x3.append(i)
    y3.append(time_odd_even[i])

x4 = []
y4 = []
for i in time_selection:
    x4.append(i)
    y4.append(time_selection[i])
    
x5 = []
y5 = []
for i in time_insertion:
    x5.append(i)
    y5.append(time_insertion[i])
    
x6 = []
y6 = []
for i in time_duble_selection:
    x6.append(i)
    y6.append(time_duble_selection[i])

fig = plt.figure()
plt.plot(x, y, 
         linestyle = ':',
         linewidth = 3,
         color = 'r')
plt.plot(x1, y1,
         linestyle = '--',
         linewidth = lineWD,
         color = 'deepskyblue')
plt.plot(x2, y2,
         linestyle = '-.',
         linewidth = lineWD,
         color = 'yellow')
plt.plot(x3, y3,
         linestyle = '-',
         linewidth = lineWD,
         color = 'lime')
plt.plot(x4, y4,
         marker = 'x',
         markersize = markSZ,
         color = 'fuchsia',
         markevery = frequency,
         markerfacecolor = 'fuchsia',
         markeredgecolor = 'fuchsia',
         markeredgewidth = markWD)
plt.plot(x5, y5,
         marker = 'p',
         markersize = markSZ,
         color = 'orange',
         markevery = frequency,
         markerfacecolor = 'orange',
         markeredgecolor = 'orange',
         markeredgewidth = markWD)
plt.plot(x6, y6,
         marker = '>',
         markersize = markSZ,
         color = 'indigo',
         markevery = frequency,
         markerfacecolor = 'indigo',
         markeredgecolor = 'indigo',
         markeredgewidth = markWD)

plt.legend(handles=[mpatches.Patch(color = 'r', label = 'Сортировка Пузырьком '),
                    mpatches.Patch(color = 'deepskyblue', label = 'Шейкерная Сортировка'),
                    mpatches.Patch(color = 'lime', label = 'Чётная Сортировка  '),
                    mpatches.Patch(color = 'fuchsia', label = 'Сортровка Выбором'),
                    mpatches.Patch(color = 'orange', label = 'Cортировка вставками'),
                    mpatches.Patch(color = 'indigo', label = 'Парная Сортировка Выбором'),
                    mpatches.Patch(color = 'yellow', label = 'Quick Сортировка')])

plt.title("Сравнение сортировок")
plt.xlabel('Количество элементов')
plt.ylabel('Время')

plt.show()
