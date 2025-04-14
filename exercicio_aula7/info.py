# Desenvolver um algoritimo que receba informações de nome, sobrenome e idade e que pergunte se quer cadastrar mais pessoas ou não, se a resposta for negativa, somar a quantidade de pessoas que foi cadastrada e verifique se tem cadastro duplicado pelo nome.

class Cadastro:
    def __init__(self): # Define o método construtor da classe Cadastro
        self.pessoas = [] # Cria uma lista vazia chamada pessoas que irá armazenar as informações das pessoas cadastradas
        
    def cadastrarPessoa(self): # Define um método chamado cadastrar_pessoa que irá solicitar as informações da pessoa e cadastrá-la
        nome = input("Digite o nome: ") # Solicita ao usuário que digite o nome da pessoa e armazena a resposta na variável nome
        sobrenome = input("Digite o sobrenome: ") # Solicita ao usuário que digite o sobrenome da pessoa e armazena a resposta na variável sobrenome
        idade = int(input("Digite a idade: ")) # Solicita ao usuário que digite a idade da pessoa e armazena a resposta na variável idade
        
        pessoa = { # Cria um dicionário chamado pessoa que armazena as informações da pessoa
            "nome": nome,
            "sobrenome": sobrenome,
            "idade": idade
        }
        
        if pessoa in self.pessoas: # Verifica se a pessoa já está cadastrada na lista pessoas
            print("Pessoa já cadastrada!") # Se a pessoa já estiver cadastrada, imprime uma mensagem informando que a pessoa já está cadastrada
        else:
            self.pessoas.append(pessoa) # Se a pessoa não estiver cadastrada, adiciona a pessoa à lista pessoas
            print("Pessoa cadastrada com sucesso!") # Imprime uma mensagem informando que a pessoa foi cadastrada com sucesso
            
    def verificarCadastro(self): # Define um método chamado verificar_cadastro que irá perguntar ao usuário se ele deseja cadastrar mais pessoas
        resposta = input("Deseja cadastrar mais pessoas? (s/n): ") # Solicita ao usuário que responda se deseja cadastrar mais pessoas
        return resposta.lower() == "s" # Retorna True se a resposta for "sim" e False caso contrário
        
    def somarPessoas(self): # Define um método chamado somar_pessoas que irá retornar o número de pessoas cadastradas
        return len(self.pessoas) # Retorna o número de elementos na lista pessoas
        
    def verificarDuplicidade(self, pessoa): # Define um método chamado verificar_duplicidade que irá verificar se uma pessoa já está cadastrada
        return pessoa in self.pessoas # Retorna True se a pessoa estiver cadastrada e False caso contrário
        
    def executar(self): # Define um método chamado executar que irá executar o programa
        while True: # Inicia um loop infinito que irá continuar até que o usuário decida parar
            self.cadastrarPessoa() # Chama o método cadastrar_pessoa para cadastrar uma pessoa
            if not self.verificarCadastro(): # Verifica se o usuário deseja cadastrar mais pessoas
                break # Se não, sai do loop
                
        print(f"Total de pessoas cadastradas: {self.somarPessoas()}") # Imprime o número total de pessoas cadastradas

        print("Pessoas cadastradas: ") # Imprime as informações de todas as pessoas cadastradas
        for pessoa in self.pessoas:
            print(f"Nome: {pessoa['nome']} {pessoa['sobrenome']}, Idade: {pessoa['idade']}")

# Cria uma instância da classe Cadastro e chama o método executar para iniciar o programa
cadastro = Cadastro()
cadastro.executar()