def all_variants(text):
    length = len(text)
    for i in range(length + 1):
        for j in range(length - i + 1):
            yield text[j:j+i]


for variant in all_variants('abc'):
    print(variant)