#importacion del framework
from flask import Flask, request, session, render_template, redirect, url_for, flash
from flask_mysqldb import MySQL


#Inicializacion del APP
app = Flask(__name__, static_folder='public', template_folder='templates')
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='sistema_orientacion'
app.secret_key= 'mysecrety'
mysql= MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        matricula = request.form['student_id']
        CC = mysql.connection.cursor()
        CC.execute('''SELECT e.id AS Matricula, e.nombre AS Nombre, m.materia AS Materia, 
                            MAX(CASE WHEN p.parcial = 'Parcial 1' THEN ca.calificacion END) AS Parcial1,
                            MAX(CASE WHEN p.parcial = 'Parcial 2' THEN ca.calificacion END) AS Parcial2,
                            MAX(CASE WHEN p.parcial = 'Parcial 3' THEN ca.calificacion END) AS Parcial3
                      FROM cargas_academicas AS ca
                      INNER JOIN cargas_estudiantes AS ce ON ca.id_carga_estudiante = ce.id
                      INNER JOIN estudiantes AS e ON ce.id_estudiante = e.id
                      INNER JOIN materias AS m ON ca.id_materia = m.id
                      INNER JOIN parciales AS p ON ca.id_parcial = p.id
                      WHERE e.id = %s
                      GROUP BY e.id, e.nombre, m.materia''', (matricula,))
        conalum = CC.fetchall()
        
        # Calcular el estado del alumno
        estado_alumno = calcular_estado_alumno(conalum)
        
        return render_template('index.html', listalum=conalum, estado_alumno=estado_alumno)
    else:
        return render_template('index.html')
    

def calcular_estado_alumno(conalum):
    # Obtener las calificaciones de los parciales
    calificaciones = [carga[3:6] for carga in conalum]
    # Lista para almacenar el estado de aprobación de cada materia
    materias_aprobadas = []
    
    for carga in calificaciones:
        # Verificar si todas las calificaciones son mayores o iguales a 7.0 en cada materia
        aprobada = all(calificacion >= 7.0 for calificacion in carga)
        materias_aprobadas.append(aprobada)
    
    # Contar el número de materias aprobadas
    num_materias_aprobadas = sum(materias_aprobadas)
    num_materias_totales = len(materias_aprobadas)
    
    # Verificar si el alumno tiene menos de la mitad de materias aprobadas y alguna calificación menor a 7.0
    if num_materias_aprobadas < num_materias_totales / 2 and any(any(calificacion < 7.0 for calificacion in carga) for carga in calificaciones):
        return "Baja Académica"
    # Verificar si todas las calificaciones son mayores o iguales a 7.0
    elif all(all(calificacion >= 7.0 for calificacion in carga) for carga in calificaciones):
        return "Exento"
    # Verificar si al menos una calificación es mayor o igual a 7.0 y las otras dos son menores a 7.0
    elif any(any(calificacion >= 7.0 for calificacion in carga) for carga in calificaciones):
        # Contar la cantidad de parciales aprobados
        aprobados = sum(any(calificacion >= 7.0 for calificacion in carga) for carga in calificaciones)
        # Verificar si el alumno puede realizar finales
        if aprobados < 3:
            return "Tendrá Finales"
        else:
            return "Baja Academica"
    else:
        return "Indefinido"








#Ejecucion del servidor en el puerto 5000
if __name__ == '__main__':
  app.run(port=1000,debug=True)