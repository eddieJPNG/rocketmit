# 🚀 CommitRocket

> Uma CLI simples e rápida para gerar comandos `git commit` padronizados com emojis, diretamente pelo terminal.

O **CommitRocket** é uma pequena ferramenta desenvolvida em Python para automatizar a criação de mensagens de commit seguindo um padrão visual consistente.

Em vez de escrever manualmente:

```bash
git commit -m ":rocket: implementa autenticação JWT :rocket:"
```

basta executar:

```bash
commitrocket "implementa autenticação JWT"
```

E a ferramenta gera automaticamente:

```bash
git commit -m ":rocket: implementa autenticação JWT :rocket:"
```

A proposta é simples: **menos digitação, menos erros e commits mais consistentes.**

---

## ✨ Funcionalidades

* 🚀 Geração automática de commits com `:rocket:`
* 💻 Execução diretamente pelo terminal
* 🌎 Disponível globalmente após a instalação
* 🐍 Desenvolvido em Python
* ⚡ Execução rápida e sem dependências externas
* 🧹 Remove espaços desnecessários da mensagem
* 🛡️ Validação para impedir mensagens vazias
* 📦 Estrutura preparada para distribuição como pacote Python
* 🔧 Arquitetura simples e fácil de expandir

---

## 📦 Instalação

### Instalação local para desenvolvimento

Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/commitrocket.git
```

Entre no diretório:

```bash
cd commitrocket
```

Instale o pacote:

```bash
pip install -e .
```

Após a instalação, o comando `commitrocket` ficará disponível no terminal.

Verifique:

```bash
commitrocket --help
```

---

## 🚀 Uso

Passe a mensagem do commit como argumento:

```bash
commitrocket "adiciona autenticação JWT"
```

Resultado:

```bash
git commit -m ":rocket: adiciona autenticação JWT :rocket:"
```

Basta copiar o comando gerado e executá-lo no seu projeto Git.

### Exemplo

```bash
commitrocket "cria endpoint de usuários"
```

Saída:

```bash
git commit -m ":rocket: cria endpoint de usuários :rocket:"
```

Outro exemplo:

```bash
commitrocket "corrige validação de email"
```

Saída:

```bash
git commit -m ":rocket: corrige validação de email :rocket:"
```

---

## 🧠 Como funciona

O funcionamento do CommitRocket é propositalmente simples:

```text
Mensagem do usuário
        │
        ▼
┌─────────────────────┐
│   CommitRocket CLI  │
└──────────┬──────────┘
           │
           ▼
   Validação da mensagem
           │
           ▼
   Adição dos marcadores
       :rocket:
           │
           ▼
┌──────────────────────────────┐
│ git commit -m ":rocket: ... │
│ ... :rocket:"                │
└──────────────────────────────┘
```

A lógica central transforma:

```text
MINHA MENSAGEM
```

em:

```text
git commit -m ":rocket: MINHA MENSAGEM :rocket:"
```

---

## 🛠️ Tecnologias

| Tecnologia | Utilização                    |
| ---------- | ----------------------------- |
| Python     | Linguagem principal           |
| argparse   | Interface de linha de comando |
| setuptools | Empacotamento e instalação    |
| Git        | Controle de versão            |

O projeto não depende de frameworks ou serviços externos.

---

## 📁 Estrutura do projeto

```text
commitrocket/
├── src/
│   └── commitrocket/
│       ├── __init__.py
│       └── cli.py
├── README.md
├── pyproject.toml
└── .gitignore
```

### `cli.py`

Contém a lógica principal da aplicação e a interface de execução pelo terminal.

### `pyproject.toml`

Define as configurações do pacote Python e registra o comando:

```text
commitrocket
```

---

## ⚙️ Requisitos

* Python 3.10+
* Git
* pip

Verifique sua versão do Python:

```bash
python --version
```

ou:

```bash
python3 --version
```

---

## 🔍 Validação

O CommitRocket não permite mensagens vazias.

Por exemplo:

```bash
commitrocket ""
```

resultará em um erro informando que uma mensagem deve ser fornecida.

Isso evita a geração de comandos inválidos ou inúteis.

---

## 🗺️ Roadmap

O projeto começa propositalmente pequeno, mas pode evoluir para uma ferramenta mais completa.

### Versão atual

* [x] CLI básica
* [x] Geração de comandos `git commit`
* [x] Prefixo e sufixo `:rocket:`
* [x] Validação de mensagens
* [x] Empacotamento como aplicação Python

### Próximas versões

* [ ] Suporte a diferentes emojis
* [ ] Presets de tipos de commit
* [ ] Opção `--bug`
* [ ] Opção `--feature`
* [ ] Opção `--refactor`
* [ ] Opção `--docs`
* [ ] Configuração personalizada de emojis
* [ ] Execução direta do `git commit`
* [ ] Testes automatizados
* [ ] Publicação no PyPI
* [ ] CI/CD com GitHub Actions

---

## 💡 Exemplos futuros

A CLI poderá evoluir para algo como:

```bash
commitrocket "adiciona sistema de login"
```

```bash
git commit -m ":rocket: adiciona sistema de login :rocket:"
```

Ou utilizar diferentes tipos:

```bash
commitrocket --bug "corrige erro de autenticação"
```

```bash
git commit -m ":bug: corrige erro de autenticação :bug:"
```

Outro exemplo:

```bash
commitrocket --refactor "separa camada de serviços"
```

```bash
git commit -m ":recycle: separa camada de serviços :recycle:"
```

---

## 🎯 Objetivo

O objetivo do projeto não é substituir ferramentas completas de gerenciamento de commits.

A ideia é resolver um problema pequeno de maneira **simples, rápida e automatizada**:

> **Transformar uma mensagem comum em um comando Git padronizado em poucos segundos.**

---

## 🤝 Contribuição

Contribuições são bem-vindas.

Para contribuir:

```bash
git clone https://github.com/SEU_USUARIO/commitrocket.git
```

Crie uma branch:

```bash
git checkout -b feature/minha-feature
```

Faça suas alterações e crie um commit:

```bash
git commit -m ":rocket: adiciona minha feature :rocket:"
```

Envie a branch:

```bash
git push origin feature/minha-feature
```

Depois, abra um Pull Request.

---

## 📄 Licença

Este projeto está disponível sob a licença **MIT**.

Consulte o arquivo [`LICENSE`](LICENSE) para mais informações.

---

## 👨‍💻 Autor

Desenvolvido por **EddieWAV**.

Se o projeto for útil para você, considere deixar uma ⭐ no repositório.

---

<div align="center">

### 🚀 CommitRocket

**Write less. Commit better.**

</div>
