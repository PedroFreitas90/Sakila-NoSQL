-- Top 5 dos filmes mais alugados
match (f:Film)<-[a:filme_alugado]-(r:Rental)
return f, count(a) as number
order by number desc
limit 5

-- Top 3 das lojas que mais faturam
match (s:Store)<-[t:trabalha_em]-(st:Staff)<-[f:feito_por]-(p:Payment)
return s, sum(p.amount) as number
order by number desc
limit 3

-- Top 3 dos filmes que tiveram alugados por mais tempo
match(r:Rental)-[:filme_alugado]->(f:Film)
where exists(r.return_date) return f.title, (duration.between(datetime(r.rental_date), datetime(r.return_date))) as dur_avg
order by dur_avg desc
limit 3

-- Top 5 dos distritos com mais clientes
MATCH (c:Customer)-[r:vive_em]->(a:Address)
return count(c) as num_customer, a.district
order by num_customer desc
limit 5

-- Top 5 dos funcionários que alugaram mais filmes
match(r:Rental)<-[:alugado]-(p:Payment)-[:feito_por]->(s:Staff)
return count(r), s.username

-- Top 3 dos atores que participou em mais filmes
match(f:Film)-[:com_participacao_de]->(a:Actor)
return count(f) as num_films,a
order by num_films desc
limit 5

-- Top 5 das categorias mais alugadas
match(r:Rental)-[:filme_alugado]->(f:Film)-[:com_categoria]->(c:Category) 
return count(f) as num_films,c
order by num_films desc
limit 5
