
lines = open("2022/01/input.txt", 'r')
input = lines.readlines()
input
input_lists = ''.join(input).split("\n\n")
digit_lists = [i.split('\n') for i in input_lists]
list_of_cals = list(map(lambda x: [int(i) for i in x if i!=''], digit_lists))
sum_cals = list(map(sum, list_of_cals))
max(sum_cals)

sum(sorted(sum_cals)[-3:])
