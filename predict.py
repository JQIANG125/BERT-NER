from bert import Ner

model = Ner("/content/out")
textlist=[]
labellist=[]
with open ('/content/data.txt','a+') as file:
	for i in file:
		textlist.append(i[0:-1])

for i in textlist:
	word=model.predict(i)
	print(word)
	labellist.append(word)
with open('/content/label.txt','a+') as label_file:
	for i in labellist:
		a=''
		for j in i:
			a=a+j['tag']
		a=a+'\n'
		label_file.write(a)



