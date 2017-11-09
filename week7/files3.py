from collections import re, Counter
words = re.findall(r'\w+',open(r'usdeclar.txt').read().lower())
count = Counter(words).most_common(15)
print(count)