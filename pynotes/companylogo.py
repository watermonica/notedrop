from collections import Counter

occurances = Counter(sorted(input()))
[print(*char) for char in occurances.most_common(3)]