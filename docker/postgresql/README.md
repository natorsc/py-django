# PostgreSQL

O **PostgreSQL** é um sistema de gerenciamento de banco de dados relacional de código aberto, conhecido por ser altamente poderoso, confiável e extensível.

Ele é amplamente utilizado tanto em aplicações pequenas quanto em sistemas corporativos de grande escala.

Criado originalmente em 1986 na Universidade da Califórnia em Berkeley, ele evoluiu ao longo dos anos para se tornar um dos SGBDs mais robustos e populares no mercado.

## Principais características do PostgreSQL:

1. **Suporte a SQL Padrão e Extensões Avançadas**: Ele segue estritamente os padrões da linguagem SQL, mas também oferece extensões como manipulação de JSON, consultas geoespaciais e muito mais.
2. **Banco de Dados Relacional e Orientado a Objetos**: Além de tabelas relacionais, o PostgreSQL suporta tipos de dados personalizados, herança de tabelas e armazenamento de objetos.
3. **Alta Extensibilidade**: Permite criar funções, operadores e tipos de dados personalizados. É possível até adicionar extensões como PostGIS para trabalhar com dados geoespaciais.
4. **Conformidade ACID**: Garantia de que as transações sejam atômicas, consistentes, isoladas e duráveis, oferecendo alta confiabilidade para aplicações críticas.
5. **Tipos de Dados Avançados**: Suporte a tipos como **JSON/JSONB**, **UUID**, **Array**, **HSTORE** (key-value) e outros, permitindo flexibilidade no design do banco de dados.
6. **Alta Performance e Confiabilidade**: Oferece recursos como **índices B-Tree, GiST, GIN, BRIN**, controle eficiente de concorrência (MVCC) e replicação nativa.
7. **Extensas Ferramentas de Replicação e Escalabilidade**: Suporte para replicação síncrona, assíncrona, e soluções como partições (sharding) para lidar com grandes volumes de dados.
8. **Comunidade e Open Source**: É mantido por uma comunidade global ativa, com constantes atualizações e melhorias, sem custos de licenciamento.

## Quando usar PostgreSQL?

- **Sistemas que exigem alta confiabilidade e consistência**: Ideal para sistemas financeiros, ERP e outras aplicações onde a perda ou inconsistência de dados não é aceitável.
- **Aplicações com dados não estruturados e estruturados**: O suporte nativo a JSON/JSONB é perfeito para aplicações híbridas que precisam lidar com documentos e dados relacionais.
- **Projetos que necessitam de extensibilidade**: Ótimo para sistemas personalizados onde o banco de dados precisa se adaptar ao negócio, como suporte a tipos de dados específicos ou lógica de negócios no banco.
- **Soluções que exigem análises geoespaciais**: Com a extensão **PostGIS**, o PostgreSQL é amplamente usado em sistemas GIS (Geographic Information Systems).

O PostgreSQL é reconhecido como um dos SGBDs mais avançados do mundo, sendo adotado por gigantes como Apple, Spotify e Instagram, graças à sua robustez, escalabilidade e suporte a uma ampla variedade de aplicações.

## Psycopg

```bash
uv add psycopg-binary
```

## Env file

```env
DATABASE_URL=postgresql://DBUSER:PASSWORD@HOSTNAME:PORT/DATABASE
```

---
