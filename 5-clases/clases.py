class Usuario:

    #atributos de clase
    username = 'invitado'
    email = ''



usuario1 = Usuario()

usuario1.username = 'jdavidsb'
usuario1.password = 12345
usuario1.email = 'juansalabote@gmail.com'

print(usuario1.username)
print(usuario1.__dict__)



