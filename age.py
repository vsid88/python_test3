def age(emp):
    return emp.get('age')
emp = [{"name" : "Tina", "age" : "40", "DoB" : "1990-03-10", "job": "Devops Engineer", "address":{"city": "New york", "country": "USA"}}, {"name" : "Tim", "age" : "35", "DoB" : "1985-02-21", "job": "Devoloper", "address":{"city": "Sydney", "country": "Australia"}}]
emp.sort(key=age)
print(emp[0]['name'], '\n', emp[0]['age'])
