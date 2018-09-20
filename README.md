# Roteiro

* Instale o postgresql
* Instale o PGAdmin4
* Crie o banco de dados rc3
* Importe a tabela de cep (arquivo cep.backup)

## Instalação da biblioteca 


```bash
pip install py-postgresql
```

## Comandos

```sql
select * from cep

select * from cep where cep = '74190100'

insert into cep (cep, municipio, uf, logradouro, bairro) values ('74123456', 'Goiania', 'GO', 'Rua 1', 'Centro teste')
```