while True:
    try:
        n = str(input("nome: "))
    except (TypeError, ValueError):
        print(f'ERRO! Digite um nome alfabético ')
        continue
    except KeyboardInterrupt:
        print(f'ERRO! O usuário preferiu não digitar')
    else:
        if n.isalpha():
            print(n)
            break
