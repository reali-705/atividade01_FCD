# Tradutor de Código Morse para Texto e Áudio

## 📂 Estrutura de Diretórios e Responsabilidades

Abaixo está o mapeamento dos módulos do projeto e seus respectivos responsáveis técnicos:

```bash
atividade02/
├── app/
│   ├── api/             # [Alessandro] - Desenvolvimento da API com FastAPI
│   ├── core/            # [Felipe]     - Lógica central de tradução Morse e DSP
│   ├── db/              # [Felipe]     - Modelagem SQLite e persistência de dados
│   ├── ui/              # [Caio]       - Interface Desktop com Flet
│   │   ├── assets/      # [Caio]       - Recursos visuais e mídias do app
│   │   └── components/  # [Caio]       - Componentes reutilizáveis de UI
│   └── utils/           # [Alessandro] - Sistema de Logging e utilitários
├── data/                # [Geral]      - Diretório de persistência local
│   └── recordings/      # [Alessandro] - Logs de áudio (.wav) para debug
├── docs/                # [Alessandro] - Documentação técnica e Relatório LaTeX
├── pyproject.toml       # [Alessandro] - Gestão de dependências via UV
└── main.py              # [Geral]      - Ponto de entrada da aplicação integrada
```

## 🛠️ Divisão Técnica das Sprints

| Integrante | Foco Principal | Entregáveis Críticos |
| :-- | :-: | :-: |
| Alessandro | Infraestrutura e API | Servidor FastAPI e estrutura de logging. |
| Felipe | Lógica e Dados | Algoritmo de tradução Morse e banco SQLite. |
| Caio | Frontend e Hardware | Interface em Flet. |

## 📝 Notas de Implementação

- **Comunicação:** O Frontend (Caio) consumirá os serviços de tradução via requisições para a API (Alessandro).

- **Auditoria:** Toda tradução realizada pela lógica do `core/` deve disparar um log estruturado através do módulo de `utils/` para ser persistido no banco e em arquivo.

- **Ambiente:** O arquivo uv.lock deve ser mantido no repositório para garantir que o PC de apresentação do Caio replique exatamente o ambiente de desenvolvimento
