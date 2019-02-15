def mergeSort(l):
    if len(l) > 1:
        L = l[:len(l) // 2]
        R = l[len(l) // 2:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                l[k] = L[i]
                i += 1
            else:
                l[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            l[k] = L[i]
            i+=1
            k+=1
          
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
