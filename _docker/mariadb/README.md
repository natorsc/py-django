# MariaDB

O **MariaDB** é um sistema de gerenciamento de banco de dados relacional (SGBD) de código aberto.

Ele foi criado como um **fork** do **MySQL** em 2009 por Michael "Monty" Widenius, o criador original do MySQL, em resposta à aquisição do MySQL pela Oracle.

O objetivo do MariaDB é garantir que o SGBD continue sendo de código aberto e que a comunidade tenha controle sobre seu desenvolvimento.

## Principais características do MariaDB:

1. **Compatibilidade com MySQL**: O MariaDB foi projetado para ser substituído diretamente pelo MySQL, com as mesmas APIs, comandos e estrutura de dados. Isso significa que muitos projetos que usam MySQL podem migrar facilmente para MariaDB.
2. **Performance aprimorada**: Inclui várias otimizações para melhorar a velocidade e eficiência em comparação com o MySQL, especialmente para consultas complexas.
3. **Segurança**: O MariaDB traz melhorias de segurança em relação ao MySQL, como autenticação mais robusta e maior controle sobre permissões.
4. **Engines de armazenamento avançadas**: Além das engines padrão como InnoDB e MyISAM, o MariaDB oferece suporte a engines exclusivas como **Aria**, **ColumnStore**, e **TokuDB**, que são otimizadas para diferentes cenários de uso.
5. **Comunidade ativa**: Por ser um projeto liderado pela comunidade, o MariaDB é frequentemente atualizado com novos recursos e correções de bugs.
6. **Licenciamento Open Source**: O MariaDB é licenciado sob a **GPL (GNU General Public License)**, garantindo que ele permaneça livre para uso e modificação.

## Quando usar MariaDB?

- Ambientes que precisam de alta performance e escalabilidade.
- Empresas ou projetos que buscam uma alternativa ao MySQL sem custos de licenciamento.
- Situações onde a segurança e atualizações contínuas são prioridade.
- Soluções que envolvam Big Data ou análise de dados em larga escala.

Se você já conhece MySQL, a transição para MariaDB será muito simples, tornando-o uma excelente escolha para projetos que exigem flexibilidade e desempenho.

## Mysqlclient

O `mysqlclient` é uma biblioteca Python que fornece uma interface para se comunicar com o banco de dados MySQL a partir de programas Python.

Ele é uma implementação do MySQL C API e é comumente usado em conjunto com o ORM (Object-Relational Mapping) Django para permitir que aplicativos Python se conectem e interajam com bancos de dados MySQL de forma eficiente e fácil.

## Instalação

### Dependências

#### Arch Linux

```bash
sudo pacman -S \
python-mysqlclient
```

#### Fedora

```bash
sudo dnf group install \
"Development Tools" # (dnf4).
```

```bash
sudo dnf install \
@development-tools # (dnf5) Fedora >= 41.
```

```bash
sudo dnf install \
mysql-devel \
pkgconfig
```

#### Ubuntu e derivados

```bash
sudo apt install \
python3-dev \
default-libmysqlclient-dev \
build-essential
```

Após realizar instalação das dependências:

```bash
uv add mysqlclient
```

---

## Env file

```env
DATABASE_URL=mysql://DBUSER:PASSWORD@HOSTNAME:PORT/DATABASE
```

---
