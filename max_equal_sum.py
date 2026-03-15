def maxEqualSum(s1, s2, s3):

    sum1 = sum(s1)
    sum2 = sum(s2)
    sum3 = sum(s3)

    i = j = k = 0

    while True:

        # if any stack empty
        if i == len(s1) or j == len(s2) or k == len(s3):
            return 0

        # if sums equal
        if sum1 == sum2 == sum3:
            return sum1

        # remove from largest sum stack
        if sum1 >= sum2 and sum1 >= sum3:
            sum1 -= s1[i]
            i += 1

        elif sum2 >= sum1 and sum2 >= sum3:
            sum2 -= s2[j]
            j += 1

        else:
            sum3 -= s3[k]
            k += 1


# Function Call
s1 = [3,2,1,1,1]
s2 = [4,3,2]
s3 = [2,5,4,1]

print(maxEqualSum(s1,s2,s3))