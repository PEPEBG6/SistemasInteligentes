drop database SistemasMedicos;

create database SistemasMedicos;

use SistemasMedicos;

create table especialidades(
id int not null primary key auto_increment,
especialidad varchar(100)
);

insert into especialidades(especialidad)
values
('Infectología');

create table enfermedades(
id int not null primary key auto_increment,
enfermedad varchar(100)
);

create table consultorios(
id int not null primary key auto_increment,
nombre varchar(100)
);

insert into consultorios(nombre)
values
('Consultorio 1'),
('Consultorio 2'),
('Consultorio 3');

create table pacientes(
id int not null primary key auto_increment,
nombre varchar(100),
ap varchar(100),
am varchar(100),
curp varchar(100),
fecha_nac date
);

create table sintomas(
id int not null primary key auto_increment,
dificultadRespirar varchar(20),
presionPecho varchar(20),
perdidaGustoOlfato varchar(20),
dolorPecho varchar(20),
mareosConvulsiones varchar(20),
fiebreAlta varchar(20),
mareos2 varchar(20),
tos varchar(20),
dolorGarganta varchar(20),
goteoNariz varchar(20),
id_paciente int not null,
foreign key (id_paciente) references pacientes (id)
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

insert into medicos(nombre,ap,am,id_especialidad,cedula)
values
('José Alberto','Gómez','Utrera','1','JAGU2111');

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


select * from especialidades;
select * from consultorios;
select * from pacientes;
select * from medicos;