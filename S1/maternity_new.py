mom = input()
mom_gene = []
for i in range(0, len(mom), 2):
    mom_gene.append(mom[i:i+2])
dad = input()
dad_gene = []
for i in range(0, len(dad), 2):
    dad_gene.append(dad[i:i+2])

babies = []
x = int(input())
for i in range(x):
    baby = input()
    babies.append(baby)

possible_genes = []
for i in range(5):
    current_possible_genes = []
    gene_1 = ''
    if mom_gene[i][0] == dad_gene[i][0] and mom_gene[i][0] == chr(97 + i):
        gene_1 = chr(97 + i)
    else:
        gene_1 = chr(65 + i)
    if gene_1 not in current_possible_genes:
        current_possible_genes.append(gene_1)
    gene_2 = ''
    if mom_gene[i][0] == dad_gene[i][1] and mom_gene[i][0] == chr(97 + i):
        gene_2 = chr(97 + i)
    else:
        gene_2 = chr(65 + i)
    if gene_2 not in current_possible_genes:
        current_possible_genes.append(gene_2)
    gene_3 = ''
    if mom_gene[i][1] == dad_gene[i][0] and mom_gene[i][1] == chr(97 + i):
        gene_3 = chr(97 + i)
    else:
        gene_3 = chr(65 + i)
    if gene_3 not in current_possible_genes:
        current_possible_genes.append(gene_3)
    gene_4 = ''
    if mom_gene[i][1] == dad_gene[i][1] and mom_gene[i][1] == chr(97 + i):
        gene_4 = chr(97 + i)
    else:
        gene_4 = chr(65 + i)
    if gene_4 not in current_possible_genes:
        current_possible_genes.append(gene_4)
    possible_genes.append(current_possible_genes)

possible_babies = []
baby = ''
# please don't call the programming police on me
for i in range(len(possible_genes[0])):
    for j in range(len(possible_genes[1])):
        for k in range(len(possible_genes[2])):
            for l in range(len(possible_genes[3])):
                for m in range(len(possible_genes[4])):
                    baby = possible_genes[0][i] + possible_genes[1][j] + possible_genes[2][k] + possible_genes[3][l] + possible_genes[4][m]
                    possible_babies.append(baby)
                    baby = ''

for i in babies:
    correct_baby = False
    for j in possible_babies:
        if i == j:
            correct_baby = True
    if correct_baby:
        print("Possible baby.")
    else:
        print("Not their baby!")
