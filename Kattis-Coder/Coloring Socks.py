input1 = input().split(' ')
input2 = sorted(list(map(int, input().split(' '))))
socks = int(input1[0])
capacity = int(input1[1])
color_difference = int(input1[2])


def check_color(to_put_in, bucket):
    try:
        if abs(to_put_in-min(bucket)) > color_difference:
            return False
    except:
        return True
    return True


def calc():
    buckets = 0
    tmp_bucket = []
    # If min and largest color difference and capacity satisfy the criteria, directly return without wasting time.
    if input2[-1]-input2[0] <= color_difference and capacity >= socks:
        print(1)
        return
    for i in range(int(input1[0])):
        appended = False
        ok = check_color(input2[i], tmp_bucket)
        if ok:
            if len(tmp_bucket) == capacity:
                buckets += 1
                appended = False
                tmp_bucket = []
                tmp_bucket.append(input2[i])
            else:
                tmp_bucket.append(input2[i])

        else:
            buckets += 1
            appended = False
            tmp_bucket = []
            tmp_bucket.append(input2[i])

        if (i == len(input1[0])):
            if appended == False:
                if tmp_bucket != []:
                    buckets += 1
    print(buckets)


calc()
