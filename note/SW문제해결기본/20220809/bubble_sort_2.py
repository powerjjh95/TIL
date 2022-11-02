a = [[4, 4, 16], [6, 1, 6], [4, 3, 12], [1, 12, 12], [5, 4, 20], [2, 3, 6], [3, 4, 12]]

def bubble_sort(idx):

    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j][idx] > a[j+1][idx]:
                a[j], a[j+1] = a[j+1], a[j]
