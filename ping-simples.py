import os # importa o módulo ou biblioteca os (integra os programas de recursos do sistema operacional)

# imprime #60 vezes
print("#" * 60)

# recebe IP do usuário
ip_ou_host = input("Digite o ip ou host a ser verificado: ")

# imprime - 60 vezes
print("-" * 60)

# imprime o pi_ou_host
os.system(f"ping -n 6 {ip_ou_host}")
print("-" * 60)
