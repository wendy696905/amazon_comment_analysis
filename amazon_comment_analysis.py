comment = []
with open('reviews.txt', 'r') as f:
	for line in f:
		comment.append(line.strip())
print(len(comment))
print(comment[0])