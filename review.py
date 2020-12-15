data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		cont = count + 1
		if count % 1000 == 0 :
			print(len(data))

	
print ('档案读完了，中间有', len(data),'笔资料')



sum_length = 0
for d in data:
	sum_length = sum_length + len(d)
	print(sum_length)

print('the average length is', sum_length/len(data))




new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('total have', len(new), 'messages length is shorter than 100')
print(new[0])






