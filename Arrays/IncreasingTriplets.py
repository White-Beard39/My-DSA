class IncreasingTriplets :

    def inc_trip(arr : list) -> tuple :

        tup = []

        l, m, h = 0, len(arr)//2, len(arr)-1

        if len(arr) >= 3 :

            for i in range(len(arr)):
                if arr[l]<arr[m]: tup.append(l)
                else: l += 1
                if arr[m]<arr[h]: tup.appen 
                else: h-=1