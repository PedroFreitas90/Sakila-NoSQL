#!/usr/bin/env python3
import re
import io
import binascii
import cx_Oracle
import datetime

tabelas = {}
tabelas["rental"] = "insert into rental(rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, last_update) values"
tabelas["film_category"] = "insert into film_category(film_id, category_id, last_update) values"
tabelas["language"] = "insert into language(language_id, name, last_update) values"
tabelas["inventory"] = "insert into inventory(inventory_id, film_id, store_id, last_update) values"
tabelas["actor"] = "insert into actor(actor_id, first_name, last_name, last_update) values"
tabelas["category"] = "insert into category(category_id, name, last_update) values"
tabelas["country"] = "insert into country(country_id, country, last_update) values"
tabelas["city"] = "insert into city(city_id, city, country_id, last_update) values"
tabelas["address"] = "insert into address(address_id, address, address2, district, city_id, postal_code, phone, last_update) values"
tabelas["store"] = "insert into store(store_id, manager_staff_id, address_id, last_update) values"
tabelas["film_text"] = "insert into film_text(film_id, title, description) values"
tabelas["customer"] = "insert into customer(customer_id, store_id, first_name, last_name, email, address_id, active, create_date, last_update) values"
tabelas["film"] = "insert into film(film_id, title, description, release_year, language_id, original_language_id,rental_duration,rental_rate, length, replacement_cost, rating, special_features, last_update) values"
tabelas["film_actor"] = "insert into film_actor(actor_id, film_id, last_update) values"
tabelas["payment"] = "insert into payment(payment_id, customer_id, staff_id, rental_id, amount, payment_date, last_update) values"
tabelas["staff"] = "insert into staff(staff_id,first_name,last_name,address_id,email,store_id,active,username,password,last_update) values"
#inserir = 0 # indica se está a percorrer pa inserir uma dada tabela. 0 significa que não

def leLinhas(inserir):
	conn = cx_Oracle.connect('final/123@localhost:1521/orcl')
	mycursor = conn.cursor()	
	with open("sakila-data (1).sql") as file:
		for line in file:
			after = re.search("VALUES",line)
			if(after is not None):
				firstLine = line.split("VALUES")
				tabela = line.split(" ") #obtem a tabela que vamos povoar
				chave = tabela[2].split("`") #tira-lhe as pelicas se tiver
				if(len(chave)>1): 
					c = chave[1]
				else:
					c = chave[0]
				inicio = tabelas[c]
				inserir = 1 #indica que vamos começar a povoar
				line = firstLine[1]
			if(inserir==1):
				if(re.search(";",line) is not None):
					inserir = 0
					l = line.split(';')
					line = l[0]
				else:
					virgulas = line.split(",\n")
					line = virgulas[0]
				if(re.match("customer",c) is not None):
					match = re.search(r'\'\d{4}\-\d{2}\-\d{2} \d{2}\:\d{2}\:\d{2}\'', line)
					nova = match.group()
					nData = 'TO_DATE(' + match.group() + ",'" + 'yyyy/mm/dd hh24:mi:ss\')'
					nData.lstrip("T")
					line = line.replace(nova,nData)
					run = inicio + line
				elif(re.match("film",c) is not None and re.match("film_",c) is None):
					match = re.search(r'\d{1,2}\.\d{2}', line)
					nova = match.group()
					line = line.replace("'" + nova +"'",nova)
					match2 = re.search(r'\'\d{1,2}\.\d{2}\'', line)
					nova2 = match2.group()
					n = nova2.split("'")
					i = n[1]
					line = line.replace(nova2, i)
					run = inicio + line
				elif(re.match("payment",c) is not None):
					campos = line.split(",");
					newN = re.search(r'\d+.\d+',campos[4]).group() #convertTonumber
					newDate = 'TO_DATE(' + campos[5] + ',' + "'yyyy/mm/dd hh24:mi:ss')"
					run = inicio + campos[0] + "," + campos[1] + "," + campos[2] + "," + campos[3] +"," + newN +"," + newDate + "," + campos[6]
				elif(re.match("rental",c) is not None):
					campos = line.split(",");
					newDate = 'TO_DATE(' + campos[1] + ',' + "'yyyy/mm/dd hh24:mi:ss')"
					newD = 'TO_DATE(' + campos[4] + ',' + "'yyyy/mm/dd hh24:mi:ss')"
					run = inicio + campos[0] + "," + newDate + "," + campos[2] + "," + campos[3] +"," + newD +"," + campos[5] + "," + campos[6]
				elif(re.match("staff",c) is not None):
					campos = line.split(",");
					new10 = campos[10].split(")")
					newT = 'TO_TIMESTAMP(' + new10[0] + ',' + "'yyyy/mm/dd hh24:mi:ss.FF')"
					run = inicio + campos[0] + "," + campos[1] + "," + campos[2] + "," + campos[3] +"," + campos[5] + "," + campos[6] + "," + campos[7] + "," + campos[8]  + "," + campos[9] + "," + newT + ")"
				else:
					nLine = line.replace(r"''","' '")
					run = inicio + nLine
				print(run)
				mycursor.execute(run)
	conn.commit()
	mycursor.close()
	conn.close()
	

leLinhas(0)

