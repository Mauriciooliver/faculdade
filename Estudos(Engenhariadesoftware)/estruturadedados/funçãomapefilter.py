print("EXEMPLO")

linguagens = '''Python java javascript c c# c++ swift go kotlin'''.split()

new_list = map(lambda x: x.upper(), linguagens)
print(f"a nova lista é = {new_list}\n")

new_list = list(new_list)
print(f"agora sim , a nova lista é = {new_list}")
