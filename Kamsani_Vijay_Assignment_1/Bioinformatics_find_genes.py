"""
homework-1
Problem -2
Kamsani vijay kumar
"""
# using regular expression
import re


# regular expression to check the required conditions
def _find_genes(genome):
    list = re.findall('ATG(?:[ACGT])*?(?:TAG|TAA|TAA)', genome)
    gen_list = []
    for i in list:
        if len(i[3:-3]) % 3 == 0:  # condition to check multiples of 3
            gen_list.append(i[3:-3])

    if len(gen_list) == 0:
        print("no gene is  found")
    else:
        for i in gen_list:
            print(i)


if __name__ == '__main__':
    genome_input = input("Enter a genome string: ")
    _find_genes(genome_input)
