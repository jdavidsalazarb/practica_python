class Usuario:

    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email


usuario1 = Usuario('jdavidsb','@12es2!!', 'juansalabote@gmail.com')



print(usuario1.username)

print(usuario1.__dict__)