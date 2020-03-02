samelist = []


def lcs(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return 0
    else:
        if str1[-1] == str2[-1]:
            samelist.insert(0, str1[-1])
            return lcs(str1[:-1], str2[:-1]) + 1
        else:
            lstr = 0
            rstr = 0
            lstr = lcs(str1[:-1], str2)
            rstr = lcs(str1, str2[:-1])
            if lstr > rstr:
                return lstr
            else:
                return rstr


array = []


def lcsiter(str1, str2):
    array = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]
    for i in range(len(array)):
        print(array[i])
    for i in range(1, (len(str1) + 1)):
        for j in range(1, len(str2) + 1):
            if str1[i-1] == str2[j-1]:
                array[j][i] = array[i - 1][j - 1] + 1
            else:
                if array[j - 1][i] > array[j][i - 1]:
                    array[j][i] = array[j - 1][i]
                else:
                    array[j][i] = array[j][i - 1]
    print("------------------------------------------")
    for i in range(len(array)):
        print(array[i])
    return array[len(str2)][len(str1)]


str1 = input("please input the 1st comparable string \n")
str2 = input("please input the 2nd comparable string \n")
print("the same characters in the comparable strings nb is :" + str(lcsiter(str1, str2)) + "and the character is :")
# print(samelist)

