# indexing = accessing the elements of a sequence using [] (indexing operator)
#            [start : end : stop]

credit_number = "1235-7652-3763-8724"

# print(credit_number[4])
# print(credit_number[:4])
# print(credit_number[5:])
# print(credit_number[5:9])
# print(credit_number[-4])
# print(credit_number[2::3])

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

reverse = credit_number[::-1]
print(reverse)
