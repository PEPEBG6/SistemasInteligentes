#importacion del framework
from flask import Flask, request, session, render_template, redirect, url_for, flash
from flask_mysqldb import MySQL


#Inicializacion del APP
app = Flask(__name__, static_folder='public', template_folder='templates')
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='SistemasMedicos'
app.secret_key= 'mysecrety'
mysql= MySQL(app)

#Declaracion de ruta http://localhost:5000
@app.route('/')
def bienvenida():
  
  return render_template('bienvenida.html')

@app.route('/pacientes.html')
def pacientes():

  return render_template('pacientes.html')

@app.route('/consulta.html')
def consulta():
  CC= mysql.connection.cursor();
  CC.execute('select * from pacientes')
  conpac= CC.fetchall()
  print(conpac)
  return render_template('consulta.html',listpac=conpac)





@app.route('/paciente',methods=['POST'])
def paciente():
  if request.method == 'POST':

    
    Vnombre=request.form['txtNombre']
    Vap=request.form['txtAp']
    Vam=request.form['txtAm']
    Vcurp=request.form['txtCURP']
    VfechaNac=request.form['txtFN']
    

    
    cs= mysql.connection.cursor()
    cs.execute('insert into pacientes (nombre,ap,am,curp,fecha_nac) values(%s,%s,%s,%s,%s)',(Vnombre,Vap,Vam,Vcurp,VfechaNac))
    mysql.connection.commit()

  flash('Se registro paciente')
  return redirect(url_for('pacientes'))



#Ejecucion del servidor en el puerto 5000
if __name__ == '__main__':
  app.run(port=1000,debug=True)