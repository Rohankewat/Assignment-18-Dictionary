sample_dict = {'C':92,'Java':66,'Python':85}    # Question no :- 10
a,b,c = sample_dict['C'],sample_dict['Java'],sample_dict['Python']
small = (c if b>c else b) if a>b else (c if a>c else a)
for e in sample_dict:
    if sample_dict[e] == small:
        print(e)
        break
print()
    