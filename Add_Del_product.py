import json

fd = open("records.json",'r')
r = fd.read()
fd.close()

records = json.loads(r)

print("What you want ? [All/Add/Del]\n")
choose=str(input("Select your choice:"))
if(choose == "All"):
    print("ALL PRODUCTS\n",records)
elif(choose == "Add"): #### ADD
    prod_id = str(input("Enter product id:"))
    name = str(input("Enter name:"))
    pr = int(input("Enter price:"))
    qn = int(input("Enter quantity:"))
    records[prod_id] = {'name': name, 'pr': pr, 'qn': qn}
    js = json.dumps(records)
    fd = open("records.json",'w')
    fd.write(js)
    fd.close()
    print("AFTER ADD NEW PRODUCT \n\n", records)
elif(choose == "Del"): ### DEL
    prod_id_del = str(input("Enter Product Id:"))
    del records[prod_id_del]
    print("AFTER DELETE A PRODUCT \n\n", records)
else:
    print("Sorry,Wrong Input (•_•)")


