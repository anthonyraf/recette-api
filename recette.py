import json
class Recette:
    def __init__(self, nom: str, description: str, ingredients: list[str]) -> None:
        self.nom: str = nom
        self.description: str = description
        self.ingredients: list[str] = ingredients


class ListeRecettes:
    def __init__(self) -> None:
        self.recettes: list[Recette] = []

    def add(self, *recette: Recette) -> None:
        self.recettes.extend(recette)

    def get(self, nom_recette: str) -> dict[str, str | list[str]] | None:
        for recette in self.recettes:
            if recette.nom == nom_recette:
                print(recette.__dict__)
                return recette.__dict__
        return None