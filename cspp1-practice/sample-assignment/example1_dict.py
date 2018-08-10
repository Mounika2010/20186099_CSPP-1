no_lines = int(input())
no_dict = {}
for temp_variable in range(no_lines):
	str_input = input().split(" ")
	print(str_input[0])
	print(str_input[1])
	if int(str_input[0]) not in no_dict:
		no_dict[int(str_input[0])] = int(str_input[1])
	else:
		no_dict[int(str_input[0])] += int(str_input[1])
	print(no_dict)
