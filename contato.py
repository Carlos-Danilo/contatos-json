import json

class Contato:
    def __init__(self, id, nome, email, telefone, data_nascimento):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.data_nascimento = data_nascimento  # string: "dd/mm/aaaa"

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Nome: {self.nome}\n"
                f"E-mail: {self.email}\n"
                f"Telefone: {self.telefone}\n"
                f"Data de Nascimento: {self.data_nascimento}")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "data_nascimento": self.data_nascimento
        }

    @staticmethod
    def from_dict(dados):
        return Contato(
            dados["id"],
            dados["nome"],
            dados["email"],
            dados["telefone"],
            dados["data_nascimento"]
        )


class ContatoUI:
    def __init__(self):
        self.contatos = {}

    def menu(self):
        while True:
            print("\n--- MENU ---")
            print("1. Inserir")
            print("2. Listar")
            print("3. Listar por ID")
            print("4. Atualizar")
            print("5. Excluir")
            print("6. Pesquisar por iniciais")
            print("7. Aniversariantes do mês")
            print("8. Abrir contatos de arquivo")
            print("9. Salvar contatos em arquivo")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")

            match opcao:
                case "1": self.inserir()
                case "2": self.listar()
                case "3": self.listar_id()
                case "4": self.atualizar()
                case "5": self.excluir()
                case "6": self.pesquisar()
                case "7": self.aniversariantes()
                case "8": self.abrir()
                case "9": self.salvar()
                case "0": break
                case _: print("Opção inválida.")

    def inserir(self):
        id = input("ID: ")
        if id in self.contatos:
            print("ID já existe.")
            return
        nome = input("Nome: ")
        email = input("E-mail: ")
        telefone = input("Telefone: ")
        data = input("Data de nascimento (dd/mm/aaaa): ")
        contato = Contato(id, nome, email, telefone, data)
        self.contatos[id] = contato
        print("Contato inserido com sucesso.")

    def listar(self):
        if not self.contatos:
            print("Nenhum contato cadastrado.")
        else:
            for contato in self.contatos.values():
                print("-" * 30)
                print(contato)

    def listar_id(self):
        id = input("Informe o ID do contato: ")
        contato = self.contatos.get(id)
        if contato:
            print(contato)
        else:
            print("Contato não encontrado.")

    def atualizar(self):
        id = input("ID do contato a atualizar: ")
        contato = self.contatos.get(id)
        if not contato:
            print("Contato não encontrado.")
            return
        nome = input("Novo nome: ")
        email = input("Novo email: ")
        telefone = input("Novo telefone: ")
        data = input("Nova data de nascimento (dd/mm/aaaa): ")
        contato.nome = nome
        contato.email = email
        contato.telefone = telefone
        contato.data_nascimento = data
        print("Contato atualizado.")

    def excluir(self):
        id = input("ID do contato a excluir: ")
        if id in self.contatos:
            del self.contatos[id]
            print("Contato excluído.")
        else:
            print("Contato não encontrado.")

    def pesquisar(self):
        iniciais = input("Digite as iniciais do nome: ").lower()
        encontrados = [c for c in self.contatos.values() if c.nome.lower().startswith(iniciais)]
        if encontrados:
            for c in encontrados:
                print("-" * 30)
                print(c)
        else:
            print("Nenhum contato encontrado com essas iniciais.")

    def aniversariantes(self):
        try:
            mes = int(input("Informe o mês (1 a 12): "))
            encontrados = [
                c for c in self.contatos.values()
                if int(c.data_nascimento.split("/")[1]) == mes
            ]
            if encontrados:
                for c in encontrados:
                    print("-" * 30)
                    print(c)
            else:
                print("Nenhum aniversariante nesse mês.")
        except:
            print("Mês inválido.")

    def abrir(self):
        try:
            with open("contatos.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                self.contatos = {d["id"]: Contato.from_dict(d) for d in dados}
            print("Contatos carregados de 'contatos.json'.")
            self.listar()  
        except FileNotFoundError:
            print("Arquivo não encontrado.")
        except Exception as e:
            print("Erro ao abrir:", e)


    def salvar(self):
        try:
            dados = [c.to_dict() for c in self.contatos.values()]
            with open("contatos.json", "w", encoding="utf-8") as arquivo:
                json.dump(dados, arquivo, ensure_ascii=False, indent=4)
            print("Contatos salvos em 'contatos.json'.")
        except Exception as e:
            print("Erro ao salvar:", e)


if __name__ == "__main__":
    app = ContatoUI()
    app.menu()
