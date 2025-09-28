# Integrantes
| Nome                           | Matrícula | Papel / Responsabilidades                                                                      |
| ------------------------------ | --------: | ---------------------------------------------------------------------------------------------- |
| Abrahão Levy Barbosa de Lavor  |   2323796 | Gestão do escopo e Priorização de Entregas.    |
| Carlos Filipe Madeira de Souza |   2317449 | Implementação do Código: `src/models.py`, `src/tasks.py`, `src/cli.py`; integração com testes. |
| Dayon Oliveira de Souza        |   2324030 | Documentação dos requisitos e mapeamento RF↔código.                           |
| Igor Davi Vieira dos Santos    |   2326203 | Desenvolvimento e execução de testes (`pytest`), QA e verificação de comportamento.            |
| Thiago de Vasconcelos Sousa    |   2415581 | Diagramas de arquitetura e aplicação de padrões de projeto.           |
| Sabrina dos Santos Alves       |   2326657 | Documentação Técnica e Revisão do Código.                                                      |



---

# Requisitos Funcionais
RF1. O sistema deve permitir adicionar uma tarefa (id, título, tags, prioridade).  
  -> Implementado em: `create_task` - `src/tasks.py`.  

RF2. O sistema deve permitir listar tarefas filtradas por tag.  
  -> Implementado em: `filter_tasks` + `make_tag_filter` — `src/tasks.py`.  

RF3. O sistema deve permitir marcar tarefa como concluída.  
  -> Implementado em: `mark_done` - `src/tasks.py`.  

RF4. O sistema deve permitir remover tarefa.  
  -> Implementado em: `remove_task` - `src/tasks.py`.  

---

# Requisitos Não Funcionais
RNF1. O código deve ser escrito em Python 3.8+ e rodar sem erros.  
  -> Evidência: execução local e `pytest` passando (comando: `pytest -q`) e `requirements.txt` contendo `pytest`.  

RNF2. O código deve documentar onde as construções funcionais são usadas (lambda, list comprehension, closure, função de ordem superior).  
  -> Implementação: seção **Construções de Programação Funcional** abaixo e comentários no código-fonte (`src/tasks.py`).

RNF3. O repositório deve conter:
  - `README.md` com instruções de uso.  
  - `docs/requisitos.md`.  
  - `tests/test_tasks.py` com testes automatizados.  

---

# Construções de Programação Funcional
- Lambda: usado em sort_by_priority (key_func = lambda t: t.priority). [arquivo/src/tasks.py, linha ...]
- List comprehension: usado em remove_task e get_titles. [arquivo/src/tasks.py]
- Closure: make_tag_filter retorna predicate que captura 'tag'. [arquivo/src/tasks.py]
- Função de alta ordem: filter_tasks recebe predicate como argumento. [arquivo/src/tasks.py]

# Mapeamento requisitos e funções
| Requisito              |        Arquivo | Função                                                      | Observação                                                                  |
| ---------------------- | -------------: | ----------------------------------------------------------- | --------------------------------------------------------------------------- |
| RF1 - Adicionar tarefa | `src/tasks.py` | `create_task` (cria `Task`) e `add_task` (adiciona à lista) | `create_task` retorna `Task`; `add_task` retorna nova lista (imutabilidade) |
| RF2 - Listar por tag   | `src/tasks.py` | `make_tag_filter` + `filter_tasks`                          | `make_tag_filter(tag)` produz predicate; `filter_tasks` aplica predicate    |
| RF3 - Marcar concluída | `src/tasks.py` | `mark_done`                                                 | Retorna nova lista com a task com `done=True` (usa `dataclasses.replace`)   |
| RF4 - Remover tarefa   | `src/tasks.py` | `remove_task`                                               | Usa list comprehension para remover por id                                  |

