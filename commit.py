from __future__ import annotations

class Commit:
    def __init__(
        self,
        id: int,
        mensagem: str,
        autor: str,
        pai: Commit | None = None,
    ) -> None:
        self.id = id
        self.mensagem = mensagem
        self.autor = autor
        self.pai = pai

    def historico(self) -> None:
        print(f"#{self.id} {self.mensagem} ({self.autor})")
        if self.pai is not None:
            self.pai.historico()
