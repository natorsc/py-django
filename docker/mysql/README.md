# MySQL

O MySQL é um sistema de gerenciamento de banco de dados relacional de código aberto amplamente utilizado.

Ele é especialmente popular para aplicativos da web e é uma parte essencial do LAMP (Linux, Apache, MySQL, PHP/Python/Perl), um conjunto de software comumente usado para executar servidores web.

O MySQL é conhecido por sua confiabilidade, escalabilidade e facilidade de uso, tornando-o uma escolha popular para desenvolvedores e organizações que precisam de um banco de dados robusto.

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
