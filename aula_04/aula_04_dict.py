# Type Hint
from typing import Dict, Any
idade: int = 30
altura: float = 1.75
nome: str = 'Alice'
is_estudante: bool = True

livros: dict = {
    'livro_1': {
        'titulo': 'Título do Livro',
        'autor': 'Autor do Livro',
        'ano_publicacao': 2000
    }
}

livro: Dict[str, Any] = {
    'titulo': 'Título do Livro',
    'autor': 'Autor do Livro',
    'ano_publicacao': 2000
}

for key in livros:
    print(livros[key])
