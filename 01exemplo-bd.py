import postgresql 

db = postgresql.open("pq://postgres:123456@localhost/rc3")
consultar = db.prepare("SELECT * from cep")
dados = consultar()

for row in dados:
    print("CEP: {} MUNICIPIO: {}".format(row["cep"], row["municipio"]))