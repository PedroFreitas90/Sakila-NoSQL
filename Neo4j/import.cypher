load csv from "file:///country.csv" as line 
create (co :Country {country : line[1]})

load csv from "file:///city.csv" as line
match (co : Country)
where co.country = line[1]
create 	(ci : City {city: line[0]}),
		(ci)-[r:pertence_a]->(co)