import socket as s

host = input('URL DA VITIMA :')

ip = s.gethostbyname(host)

print (ip)



