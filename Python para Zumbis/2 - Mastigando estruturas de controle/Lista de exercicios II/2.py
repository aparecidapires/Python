'''
Determine se um ano é bissexto. Verifique no Google como fazer isso...
'''

ano = int(input('Digite o ano: '))
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print ('O ano "%d" é bissexto' %ano)
else:
    print ('O ano %d não é bissexto' %ano)

