dna_len, pw_len = map(int, input().split())
dna = input()
a, c, g, t = map(int, input().split())
count = 0
count_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for i in range(pw_len):
    count_dict[dna[i]] += 1

for i in range(dna_len-pw_len+1):
    if (count_dict['A'] >= a and count_dict['C'] >= c and count_dict['G'] >= g and count_dict['T'] >= t):
        count += 1
    if (i != dna_len-pw_len):
        count_dict[dna[i]] -= 1
        count_dict[dna[i+pw_len]] += 1

print(count)
