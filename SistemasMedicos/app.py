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

@app.route('/')
def bienvenida():
  return render_template('bienvenida.html')

@app.route('/pacientes.html')
def pacientes():
  return render_template('pacientes.html')

@app.route('/consulta.html')
def consulta():
  CC= mysql.connection.cursor()
  CC.execute('select * from pacientes')
  conpac= CC.fetchall()
  print(conpac)
  return render_template('consulta.html',listpac=conpac)


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
      cursor = mysql.connection.cursor()
      cursor.execute('SELECT COUNT(*) FROM consultas WHERE id_consultorio = 1 AND fecha_consulta = CURDATE()')
      num_consultasC1 = cursor.fetchone()
      cursor.execute('SELECT COUNT(*) FROM consultas WHERE id_consultorio = 2 AND fecha_consulta = CURDATE()')
      num_consultasC2 = cursor.fetchone()
      cursor.execute('SELECT COUNT(*) FROM consultas WHERE id_consultorio = 3 AND fecha_consulta = CURDATE()')
      num_consultasC3 = cursor.fetchone()
      
      if num_consultasC1[0] >= 50 or num_consultasC2[0] >= 50 or num_consultasC3[0] >= 50:
        flash('El médico ha alcanzado el límite de consultas permitidas para hoy en este consultorio.')
        cursor.close()
        return redirect(url_for('diagnosticos'))
      else:
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
        
        if dificultadRespirar == 'si' and perdidaGustoOlfato == 'si':
          id_enfermedad = 1
        elif dificultadRespirar == 'si' and perdidaGustoOlfato == 'no' and dolorPecho == 'si':
          id_enfermedad = 1
        elif dificultadRespirar == 'si' and perdidaGustoOlfato == 'no' and dolorPecho == 'no' and mareosConvulsiones == 'si':
          id_enfermedad = 6
        elif dificultadRespirar == 'si' and perdidaGustoOlfato == 'no' and dolorPecho == 'no' and mareosConvulsiones == 'no' and fiebreAlta == 'si':
          id_enfermedad = 2
        elif dificultadRespirar == 'si' and perdidaGustoOlfato == 'no' and dolorPecho == 'no' and mareosConvulsiones == 'no' and fiebreAlta == 'no':
          id_enfermedad = 3
        elif dificultadRespirar == 'no' and presionPecho == 'si' and mareos2 == 'si':
          id_enfermedad = 6
        elif dificultadRespirar == 'no' and presionPecho == 'si' and mareos2 == 'no' :
          id_enfermedad = 2
        elif dificultadRespirar == 'no' and presionPecho == 'no' and tos == 'no':
          id_enfermedad = 6
        elif dificultadRespirar == 'no' and presionPecho == 'no' and tos == 'si' and dolorGarganta == 'no':
          id_enfermedad = 5
        elif dificultadRespirar == 'no' and presionPecho == 'no' and tos == 'si' and dolorGarganta == 'si' and goteoNariz == 'no':
          id_enfermedad = 4
        elif dificultadRespirar == 'no' and presionPecho == 'no' and tos == 'si' and dolorGarganta == 'si' and goteoNariz == 'si':
          id_enfermedad = 3
          
        
        cursor.execute('SELECT id FROM pacientes WHERE curp = %s', (vcurp,))
        id = cursor.fetchone()
        
        cursor.execute('INSERT INTO sintomas (dificultadRespirar, presionPecho, perdidaGustoOlfato, dolorPecho, mareosConvulsiones, fiebreAlta, mareos2, tos, dolorGarganta, goteoNariz, id_paciente) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)', (dificultadRespirar, presionPecho, perdidaGustoOlfato, dolorPecho, mareosConvulsiones, fiebreAlta, mareos2, tos, dolorGarganta, goteoNariz, id))
        mysql.connection.commit()
        
        #sacar el id del ultimo diagnostico
        cursor.execute('SELECT MAX(id) FROM sintomas')
        id_sintomas = cursor.fetchone()
        id_consultorio = request.form['txtconsultorio']
        
        cursor.execute('INSERT INTO diagnosticos (id_sintoma, id_enfermedad) VALUES (%s, %s)', (id_sintomas, id_enfermedad))
        mysql.connection.commit()
        
        #sacar el id del ultimo diagnostico
        cursor.execute('SELECT MAX(id) FROM diagnosticos')
        id_diagnostico = cursor.fetchone()
        cursor.execute('INSERT INTO consultas (id_medico, id_diagnosticos, id_consultorio, fecha_consulta) VALUES (%s, %s, %s, CURDATE())', (1, id_diagnostico, id_consultorio))
        mysql.connection.commit()
      
        flash('Se registró el diagnóstico correctamente')
        return redirect(url_for('diagnosticos'))
      
      
      
@app.route('/diagnosticos')
def diagnosticos():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT p.nombre, p.ap, p.am, p.curp, p.fecha_nac, c.id_consultorio, e.enfermedad, c.fecha_consulta FROM pacientes p INNER JOIN sintomas s on p.id = s.id_paciente inner JOIN diagnosticos d on s.id = d.id_sintoma INNER JOIN consultas c on d.id = c.id_diagnosticos inner join enfermedades e on d.id_enfermedad = e.id')
    data = cursor.fetchall()

    pacientes = []

    for row in data:
        nombre = row[0]
        ap = row[1]
        am = row[2]
        curp = row[3]
        fecha_nac = row[4]
        id_consultorio = row[5]
        enfermedad = row[6]
        fecha_consulta = row[7]

        # Calcular la edad
        from datetime import datetime
        fecha_nacimiento = datetime.strptime(str(fecha_nac), '%Y-%m-%d')
        fecha_actual = datetime.now()
        edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

        # Crear un diccionario para cada paciente
        paciente = {
            'nombre': nombre,
            'ap': ap,
            'am': am,
            'curp': curp,
            'fecha_nac': edad,
            'id_consultorio': id_consultorio,
            'enfermedad': enfermedad,
            'fecha_consulta': fecha_consulta,
            'edad': edad  # Añadir la edad al diccionario
        }

        pacientes.append(paciente)
        
        cursor.close()

    return render_template('diagnosticos.html', pacientes=pacientes)


#Ejecucion del servidor en el puerto 5000
if __name__ == '__main__':
  app.run(port=1000,debug=True)