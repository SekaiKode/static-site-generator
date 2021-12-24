import os

isi = open("base.md", "r")
a = isi.read()

c = 'content/'
file = input('masukkan judul: ')

f = open(c + file + '.md', "w")
f.write(a)

f.close()
isi.close()