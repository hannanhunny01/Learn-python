with open('dados.txt','r') as file:
    text = file.read().strip().replace('\n','')
    
    
    text2 = file.read().replace('/','\n')
    
    print(type(text))
   # print(text)
    
    #text_file = open("filter.txt", "w")
 
#write string to file
#text_file.write(text)
 
#close file
#text_file.close()
    
#with open('filter.txt','r') as file:
#    text5 = file.read().replace('/','\n')
#    print(type(text5))
#    text5.strip()
#    print(text5)

#    filtereddata = open("filterfianl.txt", "w")
#    filtereddata.write(text5)
#    filtereddata.close()

#with open('filterfianl.txt','r') as file:
#    text10 = file.read().replace(' ','')
#    print(text10)

#    filtereddata = open("filterfinal.txt", "w")
#    filtereddata.write(text10)
#    filtereddata.close()
  
file2 = open('filterfinal.txt','r')
count =0
for line in file2:
  if line.count('-') <= 7:
    print(line)
  
      
    
    
    
  
   

    