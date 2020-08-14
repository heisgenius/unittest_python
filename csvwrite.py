
with open ('123.csv','a+') as file:
    file.write('pwd'+',')
    file.write('uphone'+'\n')
    for i in range(1,100):
        file.write('123456' + ',')
        file.write('1234'+str( i)+'\n')

    file.close()