class Cnnn():
    #aqui comentaro

    _connection = pymysql.connect(host='localhost', user='root', password='asd123', database='academia_jam2023')
    _cursor = _connection.cursor()
    
    def __init__(self):
        self.Query = ""

    def query(self, tabla):
        tablasDB = {'cursos','usuarios','cursantes','asistencias'}
        if (tabla not in tablasDB):
            raise("El nombre introducido no es correcto")
        self.Query = f"Select * from {str(tabla)}"
        self._cursor.execute(self.Query)
        self._connection.commit()
        cursor = self._cursor
        self._cursor.close()
        self._connection.close()
        return cursor
    

