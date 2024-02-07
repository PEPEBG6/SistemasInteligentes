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


def calcular_estado_alumno(conalum):
    materias_con_porcentaje = []
    
    for carga in conalum:
        # Calcular el porcentaje de calificaciones por encima de 7.00 para cada parcial
        calificaciones = carga[3:6]
        calificaciones_aprobadas = [calificacion for calificacion in calificaciones if calificacion >= 7.0]
        porcentaje_aprobacion = (len(calificaciones_aprobadas) / len(calificaciones)) * 100
        carga_con_porcentaje = carga + (porcentaje_aprobacion,) 
        materias_con_porcentaje.append(carga_con_porcentaje)
    
    # Contar el número de materias aprobadas
    num_materias_aprobadas = sum(1 for carga in materias_con_porcentaje if carga[-1] >= 70)  
    num_materias_totales = len(materias_con_porcentaje)
    
    # Calcular la probabilidad de estar en baja académica
    probabilidad_baja_academica = (num_materias_totales - num_materias_aprobadas) / num_materias_totales
    
    return materias_con_porcentaje, probabilidad_baja_academica



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
        
        # Calcular el estado del alumno y el porcentaje de poder aprobar
        conalum, probabilidad_baja_academica = calcular_estado_alumno(conalum)
        
        return render_template('index.html', listalum=conalum, probabilidad_baja_academica=probabilidad_baja_academica)
    else:
        return render_template('index.html')
    


#Ejecucion del servidor en el puerto 5000
if __name__ == '__main__':
  app.run(port=1000,debug=True)
