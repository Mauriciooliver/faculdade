linguagem = ['PYTHON', 'JAVA', 'JAVASCRIPT', 'C', 'C#', 'C++', 'SWIFT', 'GO', 'KOTLIN']

print('antes da listcomp = ', linguagem)

linguagem = [item.lower() for item in linguagem]

print("\ndepois da listcomp = ", linguagem)