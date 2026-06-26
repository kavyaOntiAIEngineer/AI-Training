# Remove duplicate records and filter active ones
records=[{"id":1,"name":"Alice","active":True},{"id":2,"name":"Bob","active":True},{"id":1,"name":"Alice","active":True}]
seen=[]
unique=[]
for r in records:
    if r not in seen:
        seen.append(r["id"])
        unique.append(r)
result= [r for r in unique if r["active"]]
print(result)