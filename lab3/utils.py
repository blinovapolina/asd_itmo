def open_file(file_name):
    with open(file_name, 'r') as file:
        #     data = file.readlines()
        #     if len(data) == 2:
        #         n = int(data[0])
        #         if ord(data[1][0]) in range(65, 91):
        #             arr = [i for i in data[1]]
        #         else:
        #             arr = list(map(int, data[1].split()))
        #         return n, arr
        #     if len(data) == 4:
        #         n1 = int(data[0])
        #         n2 = int(data[2])
        #         arr1 = list(map(int, data[1].split()))
        #         arr2 = list(map(int, data[3].split()))
        #         return n1, arr1, n2, arr2
        #     else:
        #         n = int(data[0].strip())
        #         arr1 = list()
        #         for i in range(1, n + 1):
        #             row = list(map(int, data[i].strip().split()))
        #             arr1.append(row)
        #         arr2 = list()
        #         for i in range(n + 1, 2 * n + 1):
        #             row = list(map(int, data[i].strip().split()))
        #             arr2.append(row)
        #     return arr1, arr2
        lines = file.readlines()
        return lines


def write_file(arr, file_name):
    with open(file_name, 'w') as file:
        # if arr == str(arr):
        #     file.write(arr)
        # else:
        #     if isinstance(arr, list):
        #         if isinstance(arr[0], list):
        #             for r in arr:
        #                 file.write(' '.join(map(str, r)) + '\n')
        #         else:
        #             file.write(' '.join(map(str, arr)))
        #     elif isinstance(arr, tuple):
        #         file.write(f"{' '.join(map(str, arr[0]))}\n")
        #         file.write(' '.join(map(str, arr[1])))
        #     else:
        #         file.write(arr)
        if isinstance(arr, list):
            if isinstance(arr[0], list):
                for r in arr:
                    file.write(' '.join(map(str, r)) + '\n')
            else:
                file.write(' '.join(map(str, arr)))
        else:
            file.write(arr)
