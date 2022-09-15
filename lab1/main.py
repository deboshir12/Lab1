import csv


f = open('result.txt','w',encoding='utf-16')
Tags_file = open('TAGS.txt','w',encoding='utf-16')


search = input('Search for: ')
flag = 0
c = 0
tags = []
m_sort = []

with open ('books.csv','r') as csvfile:
    
    table = csv.reader(csvfile,delimiter=';')
    count_str = 0
    
    for row in table: # 20 записей-ссылок 
        if c < 21 and c>0:
            f.write(str(c)+'. ' + row[3]+'. '+row[1]+' - '+ row[6][:4:]+ '\n')
        if len(row[1]) > 30:
            count_str += 1
            
            
        lower_case = row[3].lower()
        index = lower_case.find(search.lower())
        
        
        date_book = '' # проверка на дату книги
        if index != -1:
            date_book  = date_book + row[6]
        if ( index != -1) :
            if int(date_book[:4:]) > 2018:
                print(row[1])
                flag  = 1
                
                      
        
        for i in row[12].replace('# ','/ ').split('/ '): # все теги
            if i not in tags and c>0:
                tags.append(i)
                Tags_file.write(i+ '\n')
        if c>0:
            m_sort.append((int(row[8]),row[1]))       
        c+=1
        
        
if flag != 1:
    print('\n'+'Nothing found')
    
print('\n'+'The number of books with a title longer than 30 characters: '+str(count_str) + '\n')
print('All tags in file TAGS.txt, the most popular books in result.txt')
f.write('\n'+'\n'+ 'the most popular books : '+ '\n')


m_sort = sorted(m_sort,key= lambda x : x[0])

for row in range(len(m_sort)-1,len(m_sort)-22,-1):
    f.write(str(m_sort[row][1])+'\n')



f.close()
Tags_file.close()
