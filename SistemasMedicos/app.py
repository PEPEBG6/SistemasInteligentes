#importacion del framework
from flask import Flask, request, session, render_template, redirect, url_for, flash
from flask_mysqldb import MySQL


#Inicializacion del APP
app = Flask(__name__, static_folder='public', template_folder='templates')
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='consultasmed'
app.secret_key= 'mysecrety'
mysql= MySQL(app)

#Declaracion de ruta http://localhost:5000
@app.route('/')
def bienvenida():
  return render_template('bienvenida.html')

@app.route('/pacientes.html')
def pacientes():
  return render_template('pacientes.html')





@app.route('/paciente',methods=['POST'])
def paciente():
    if request.method == 'POST':
        Vnombre = request.form['txtNombre']
        Vap = request.form['txtAp']
        Vam = request.form['txtAm']
        Vcurp = request.form['txtCURP']
        Vcurp = Vcurp.upper()
        VfechaNac = request.form['txtFN']

        # Verificar si la CURP ya existe en la base de datos
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM pacientes WHERE curp = %s', (Vcurp,))
        paciente_existente = cursor.fetchone()

        if paciente_existente:
            flash('La CURP ya está registrada')
        else:
            # Insertar el nuevo paciente si la CURP no está duplicada
            cursor.execute('INSERT INTO pacientes (nombre, ap, am, curp, fecha_nac) VALUES (%s, %s, %s, %s, %s)', (Vnombre, Vap, Vam, Vcurp, VfechaNac))
            mysql.connection.commit()
            flash('Se registró al paciente correctamente')

    return redirect(url_for('pacientes'))



@app.route('/consulta')
def form():
  cs= mysql.connection.cursor()
  cs.execute('select curp, fecha_nac from pacientes')
  #como concateno el nombre completo en la consulta
  data=cs.fetchall()
  return render_template('formulario.html',listpacientes=data)


@app.route('/diagnostico',methods=['POST'])
def diagnostico():
    if request.method == 'POST':     
      vcurp = request.form['txtCurp']
      dificultadRespirar = request.form.get('respuesta1')
      presionPecho = request.form.get('respuesta2')
      perdidaGustoOlfato = request.form.get('respuesta3')
      dolorPecho = request.form.get('respuesta4')
      mareosConvulsiones = request.form.get('respuesta5')
      fiebreAlta = request.form.get('respuesta6')
      mareos2 = request.form.get('respuesta7')
      tos = request.form.get('respuesta8')
      dolorGarganta = request.form.get('respuesta9')
      goteoNariz = request.form.get('respuesta10')
      
      cursor = mysql.connection.cursor()
      cursor.execute('SELECT id FROM pacientes WHERE curp = %s', (vcurp,))
      id = cursor.fetchone()
      
      cursor.execute('INSERT INTO sintomas (dificultadRespirar, presionPecho, perdidaGustoOlfato, dolorPecho, mareosConvulsiones, fiebreAlta, mareos2, tos, dolorGarganta, goteoNariz, id_paciente) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)', (dificultadRespirar, presionPecho, perdidaGustoOlfato, dolorPecho, mareosConvulsiones, fiebreAlta, mareos2, tos, dolorGarganta, goteoNariz, id))
      mysql.connection.commit()
      
      #sacar el id del ultimo diagnostico
      cursor.execute('SELECT MAX(id) FROM sintomas')
      id_sintomas = cursor.fetchone()
      id_consultorio = request.form['txtconsultorio']
      id_enfermedad = request.form['txtenfermedad']
      print(id_enfermedad)
      print("---------------------------------------------------------------------------------------------------------")
      
      cursor.execute('INSERT INTO diagnosticos (id_sintoma, id_enfermedad) VALUES (%s, %s)', (id_sintomas, id_enfermedad))
      mysql.connection.commit()
      
      #sacar el id del ultimo diagnostico
      cursor.execute('SELECT MAX(id) FROM diagnosticos')
      id_diagnostico = cursor.fetchone()
      #sacar la fecha actual
      cursor.execute('INSERT INTO consultas (id_medico, id_diagnosticos, id_consultorio, fecha_consulta) VALUES (%s, %s, %s, , CURDATE()))', (1, id_diagnostico, id_consultorio ))
      mysql.connection.commit()
      

      
      
      flash('Se registró el diagnostico correctamente')
      return redirect(url_for('bienvenida'))
      
       

#Ejecucion del servidor en el puerto 5000
if __name__ == '__main__':
  app.run(port=1000,debug=True)