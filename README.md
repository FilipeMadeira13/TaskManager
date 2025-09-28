# Task Manager

Projeto simples de gerenciador de tarefas (CLI), implementado com princípios funcionais.
Atende aos requisitos do trabalho: CRUD de tarefas, uso de lambda, list comprehension, closure e função de alta ordem. Inclui testes com pytest.

## Estrutura do projeto

```
task-manager/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── models.py
│   ├── tasks.py
│   └── cli.py
└── tests/
    └── test_tasks.py
```

## Requisitos

- Python 3.8+
- (opcional) ambiente virtual
- `pytest` (para rodar testes)

Arquivo `requirements.txt` mínimo:
```
pytest
```

## Como configurar

### 1. Crie e ative um ambiente virtual

**Linux / macOS**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell)**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Instale dependências
```bash
pip install -r requirements.txt
```

## Rodando o menu interativo (CLI)

Recomendado: rode a partir da raiz do projeto.

### Opção A - via -m
```bash
python -m src.cli
```

### Opção B - executando diretamente (se houver erro de import)

**Linux/macOS:**
```bash
PYTHONPATH=. python src/cli.py
```

**Windows (cmd):**
```cmd
set PYTHONPATH=. & python src/cli.py
```

**Windows (PowerShell):**
```powershell
$env:PYTHONPATH="."; python src/cli.py
```

### O menu permite:
- Adicionar tarefa (título, tags, prioridade)
- Listar todas as tarefas
- Listar pendentes
- Filtrar por tag
- Listar ordenadas por prioridade
- Marcar tarefa como concluída
- Remover tarefa
- Mostrar títulos

## Rodando testes (pytest)

Na raiz do projeto:
```bash
python -m pytest -q
```

## Notas sobre implementação

- **Lambda:** usada em `sort_by_priority` (key func).
- **List comprehension:** usada em `remove_task`, `get_titles`, etc.
- **Closure:** `make_tag_filter(tag)` retorna um predicate que captura `tag`.
- **Função de alta ordem:** `filter_tasks(tasks, predicate)` recebe uma função `predicate`.
