from ModelarPessoa import Pessoa

def main():
    pessoa1 = Pessoa('Ana', 13, 55, 1.45)
    print(f"\nNome: {pessoa1.nome}\nIdade: {pessoa1.idade} anos\nAltura: {pessoa1.altura}m\nPeso: {pessoa1.peso}kg")

    pessoa1.nome = 'Paula'
    print(f"\nNome: {pessoa1.nome}\nIdade: {pessoa1.idade} anos\nAltura: {pessoa1.altura}m\nPeso: {pessoa1.peso}kg")

if __name__ == "__main__":
    main()