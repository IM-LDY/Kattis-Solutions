correct_ans = int(input())
input2 = input()
input3 = input()

same_chars = 0

for i in range(len(input2)):
    if(input2[i] == input3[i]):
        same_chars += 1
differnt_chars = len(input2)-same_chars

maxi_correct = 0
if correct_ans <= same_chars:
    maxi_correct = correct_ans
    left_over = len(input2)-same_chars
else:
    maxi_correct = same_chars
    left_over = len(input2)-correct_ans

print(maxi_correct+left_over)
