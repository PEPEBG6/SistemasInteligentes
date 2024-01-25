create database SistemasMedicos;

use SistemasMedicos;

create table especialidades(
id int not null primary key auto_increment,
especialidad varchar(100)
);

create table sintomas(
id int not null primary key auto_increment,
nom_sintoma varchar(100)
);

create table enfermedades(
id int not null primary key auto_increment,
enfermedad varchar(100)
);

create table consultorios(
id int not null primary key auto_increment,
nombre varchar(100)
);

create table pacientes(
id int not null primary key auto_increment,
nombre varchar(100),
ap varchar(100),
am varchar(100),
curp varchar(100),
fecha_nac date
);

create table medicos(
id int not null primary key auto_increment,
nombre varchar(100),
ap varchar(100),
am varchar(100),
id_especialidad int not null,
cedula varchar(100),
foreign key (id_especialidad) references especialidades (id) 
);

create table diagnosticos(
id int not null primary key auto_increment,
id_sintoma int not null,
id_enfermedad int not null,
foreign key (id_sintoma) references sintomas (id),
foreign key (id_enfermedad) references enfermedades (id)
);

create table consultas(
id int not null primary key auto_increment,
id_medico int not null,
id_paciente int not null,
id_diagnostico int not null,
id_consultorio int not null,
fecha_consulta date,
foreign key (id_medico) references medicos (id),
foreign key (id_paciente) references pacientes (id),
foreign key (id_diagnostico) references diagnosticos (id),
foreign key (id_consultorio) references consultorios (id)
);
