import json

fd = open("records.json",'r')
r = fd.read()
fd.close()

records = json.loads(r)

print(records)

ui_prod  = str(input("Enter the product_Id: "))
ui_quant = int(input("Enter the quantity: "))

print("**********************")
print("Product: ", records[ui_prod]['name'])
print("Price: ", records[ui_prod]['pr'])
print("Billing Amount: ", records[ui_prod]['pr'] * ui_quant)
print("**********************")

records[ui_prod]['qn'] = records[ui_prod]['qn'] - ui_quant

js = json.dumps(records)

fd = open("records.json",'w')
fd.write(js)
fd.close()

{'prod' : ui_prod, 'qn' : ui_quant, 'amount': records[ui_prod]['pr'] * ui_quant}
fd = open("sales.json",'r')
r = fd.read()
fd.close()

sales = json.loads(r)
# sales = {ui_prod+"_tran_"+str(records[ui_prod]['pr'] * ui_quant): {'prod' : ui_prod, 'qn' : ui_quant, 'prod_name':records[ui_prod]['name'], 'amount': records[ui_prod]['pr'] * ui_quant}}
sales[ui_prod+"_tran_"+str(records[ui_prod]['pr'] * ui_quant)]={'prod' : ui_prod, 'qn' : ui_quant, 'prod_name':records[ui_prod]['name'], 'amount': records[ui_prod]['pr'] * ui_quant}
sale = json.dumps(sales)

fd = open("sales.json",'w')
fd.write(sale)
fd.close()


print(records)
