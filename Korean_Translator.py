dictionary = {'크다' : 'besar', '배' : 'kapal'}
y = 1
gen_statement = 'Kata tidak ditemukan'
while y == 1:
  print('')
  print('Halo selamat datang di Korean Translator')
  print('------------------------------------------')
  print('Silahkan pilih bahasa')
  print('1. 한국어')
  print('2. Bahasa')
  print('3. Exit')
  n_awal = int(input('>> '))

  if n_awal == 1:
    print('Silahkan tuliskan kata =', end=' ')
    n_kata = input()    
    for i, j in dictionary.items():
      if i == n_kata:
        gen_statement = 'Translation = '+ j
    print(gen_statement)
  elif n_awal == 2:
    print('Silahkan tuliskan kata =', end=' ')
    n_kata = input()    
    for i, j in dictionary.items():
      if j == n_kata:
        gen_statement = 'Translation = '+ i
    print(gen_statement)
  else:
    break
  print('')
  print('--------------------------------------------------------')
  print('Apakah anda masih ingin menggunakan Korean Translator?')
  print('1. Ya')
  print('2. Tidak')
  y = int(input('>> '))
print('Terima kasih telah menggunakan Korean Translator')