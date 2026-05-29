# indexing = accessing elements of a sequence using [] indexing operator [start : end : step]

credit_number = "12334-5678-2526-2736"
print(credit_number[0])
print(credit_number[0:4])
print(credit_number[5:9])
print(credit_number[::2])

#Last four digits of credit card numnber
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

#Reverse the string
credit_number_reversed = credit_number[::-1]
print(credit_number_reversed)