from datetime import datetime

#print(dir(datetime))
suAn = datetime.now()
#print(suAn)

import datetime
#print(dir(datetime.datetime))

suAn2 = datetime.datetime.today()
#print(suAn2)

"""
print(suAn2.day)
print(suAn2.month)
print(suAn2.year)
print(suAn2.hour)
print(suAn2.minute)
print(suAn2.second)

"""

# ctime
tarih_ctime = datetime.datetime.ctime(suAn2)
#print(tarih_ctime)

# strftime
#tarih_strftime = datetime.datetime.strftime(suAn2, '%c')
#tarih_strftime = datetime.datetime.strftime(suAn2, '%a')
#tarih_strftime = datetime.datetime.strftime(suAn2, '%A')
#tarih_strftime = datetime.datetime.strftime(suAn2, '%b')
#tarih_strftime = datetime.datetime.strftime(suAn2, '%B')
#tarih_strftime = datetime.datetime.strftime(suAn2, '%m')
#tarih_strftime = datetime.datetime.strftime(suAn2, '%y')
#tarih_strftime = datetime.datetime.strftime(suAn2, '%Y')
#tarih_strftime = datetime.datetime.strftime(suAn2, '%x')
tarih_strftime = datetime.datetime.strftime(suAn2, '%X')
#print(tarih_strftime)

import locale
# locale -a
loca = locale.setlocale(locale.LC_ALL, 'tr_TR')
#print(loca)

tarih_strftime = datetime.datetime.strftime(suAn2, '%B')
#print(tarih_strftime)

tarih_strftime = datetime.datetime.strftime(suAn2, '%d %B %Y')
#print(tarih_strftime)

# strptime
gun = datetime.datetime.strftime(suAn, '%d')
ay = datetime.datetime.strftime(suAn, '%B')
yil = datetime.datetime.strftime(suAn, '%Y')
s = datetime.datetime.strftime(suAn, '%H')
m = datetime.datetime.strftime(suAn, '%M')
sn = datetime.datetime.strftime(suAn, '%S')
tam_tarih = str(gun) + ' ' + str(ay) + ' '  + str(yil) + ' '  + str(s +':' + m + ':' + sn)
#print(type(tam_tarih))
#print(tam_tarih)
stringTarih = '19 Mayıs 2019 12:34:44'
tarih_strptime = datetime.datetime.strptime(stringTarih, '%d %B %Y %H:%M:%S')
#print(tarih_strptime)


import os

# fromtimestamp

degisZamani = os.stat('example').st_mtime
#print(type(degisZamani))
degisiklikTarihi = datetime.datetime.fromtimestamp(degisZamani)
#print(degisiklikTarihi)


# timestamp
"""
Örneğin, bir dosya oluşturdunuz, bu dosyaya bir zaman etiketi (buna damga diyorlarmış) 
oluşturmak gerektiğinde bu metod kullanılabilir. Uygulama geliştirirken ihtiyaçlarınız doğrultusunda 
kullanabileceğiniz güzel bir özellik

"""

tarih = datetime.datetime.now()
zamanEtiketi = datetime.datetime.timestamp(tarih)
#print(zamanEtiketi)
#print(type(zamanEtiketi))
tarih = datetime.datetime.fromtimestamp(zamanEtiketi)
#print(tarih)


# Elimizde bu şekilde bir string tarih Objesi var, ama bunun type bilgisi aldığımızda string olduu görülecek
stringTarih = '19 05 2019 19:19:19'
#print(type(stringTarih))

gun, ay, yil, saat = stringTarih.split(' ')
#print(gun, ay, yil, saat)

tarih = datetime.datetime(int(yil), int(ay), int(gun))
#tarih = datetime.datetime(2019, 5, 19, 19, 19, 19)
#print(tarih)
#print(type(tarih))


suAn2 = datetime.datetime.today()
tarih = datetime.datetime(2021, 5, 19)
fark = suAn2 - tarih
#print(fark)



# ileri tarih timedelta
fark1 = datetime.timedelta(days=20)
#print(fark1)
ileriFark = suAn2 + fark1
#print(ileriFark)

# geçmiş tarihi timedelta
fark1 = datetime.timedelta(days=20)
print(fark1)
gecmisFark = suAn2 - fark1
print(gecmisFark)