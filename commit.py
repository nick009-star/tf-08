class Commit:
    """Representa um commit e liga seu histórico ao commit anterior."""

    def __init__(
        self,
        id,
        mensagem,
        autor,
        pai=None,
    ):
        """Guarda os dados deste commit e o commit anterior, se houver."""
        self.id = id
        self.mensagem = mensagem
        self.autor = autor
        self.pai = pai

    def historico(self):
        """Imprime este commit e chama o histórico do pai até o primeiro."""
        print(f"#{self.id} {self.mensagem} ({self.autor})")
        if self.pai is not None:
            self.pai.historico()


class Repositorio:
    """Guarda os dados do repositório e aponta para seu commit mais recente."""

    def __init__(self, nome, autor):
        """Inicia o repositório sem commits e com o contador zerado."""
        self.nome = nome
        self.autor = autor
        self.head = None
        self.contador_commits = 0

    def commitar(self, mensagem):
        """Cria um commit numerado e atualiza o mais recente do repositório."""
        self.contador_commits += 1
        self.head = Commit(
            self.contador_commits,
            mensagem,
            self.autor,
            self.head,
        )

    def log(self):
        """Imprime o histórico do mais recente ao mais antigo."""
        if self.head is None:
            print("Nenhum commit ainda")
            return
        self.head.historico()

    def total_de_commits(self):
        """Conta os commits seguindo os pais a partir do mais recente."""
        total = 0
        commit_atual = self.head
        while commit_atual is not None:
            total += 1
            commit_atual = commit_atual.pai
        return total
