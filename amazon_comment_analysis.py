comment = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		comment.append(line.strip())
		count = count + 1
		if count % 1000 == 0:
			print(len(comment))
print('There are', len(comment), ' comments in total.')

sum_len = 0
for d in comment:
	sum_len = sum_len + len(d)
print('The average quantity of the characters in the comment are', sum_len / len(comment))