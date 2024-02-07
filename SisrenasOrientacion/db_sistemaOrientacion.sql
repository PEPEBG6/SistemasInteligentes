drop database sistema_orientacion;

create database sistema_orientacion;

use sistema_orientacion;

create table estudiantes(
id int not null primary key auto_increment,
nombre varchar(100),
ap varchar(100),
am varchar(100)
);

insert into estudiantes(nombre,ap,am)
values
('Jose Luis','Bernardo','Gutierrez'),
('Jose Andres','Hernadez','Valdez'),
('Jose Alberto','Gomez','Utrera'),
('Juan Pablo','Perez','Valadez'),
('Maria Monserrat','Campuzano','Leon'),
('Paola','Duran','Castillo'),
('Sofia','Garcia','Perez'),
('Johan Israel','Mauricio','Hernandez'),
('Diego','Reyes','Pedraza'),
('Alvaro','Zuñiga','Torres');

create table materias(
id int not null primary key auto_increment,
materia varchar(100)
);
insert into materias(materia)
values
('Matematicas'),
('Español'),
('Física'),
('Redes'),
('Base de Datos'),
('Programación'),
('Habilidades Gerenciales'),
('Gestion de Proyectos'),
('Filosofia'),
('Ingles');

create table carreras(
id int not null primary key auto_increment,
carrera varchar(100)
);
insert into carreras(carrera)
values
('Negocios'),
('Administracion de Empresas'),
('Automotriz'),
('Mecatronica'),
('Manufactura'),
('Sistemas'),
('Telecomunicaciones');

create table grupos(
id int not null primary key auto_increment,
grupo varchar(100)
);
insert into grupos(grupo)
values
('N181'),
('AE181'),
('A181'),
('ME181'),
('MA181'),
('S181'),
('T181');

create table periodos(
id int not null primary key auto_increment,
periodo varchar(100)
);
insert into periodos(periodo)
values
('E-A'),
('M-A'),
('S-D');

create table parciales(
id int not null primary key auto_increment,
parcial varchar(100)
);
insert into parciales(parcial)
values
('Parcial 1'),
('Parcial 2'),
('Parcial 3');

create table cargas_estudiantes(
id int not null primary key auto_increment,
id_estudiante int not null,
id_carrera int not null,
id_grupo int not null,
id_periodo int not null,
foreign key (id_estudiante) references estudiantes (id) on delete cascade on update cascade,
foreign key (id_carrera) references carreras (id) on delete cascade on update cascade,
foreign key (id_grupo) references grupos (id) on delete cascade on update cascade,
foreign key (id_periodo) references periodos (id) on delete cascade on update cascade
);
insert into cargas_estudiantes(id_estudiante, id_carrera, id_grupo, id_periodo)
values
(1,1,1,1),
(2,2,2,1),
(3,3,3,1),
(4,4,4,1),
(5,5,5,1),
(6,6,6,1),
(7,7,7,1),
(8,1,1,1),
(9,2,2,1),
(10,3,3,1);

select * from cargas_estudiantes;

create table cargas_academicas(
id int not null primary key auto_increment,
id_carga_Estudiante int not null,
id_materia int not null,
id_parcial int not null,
calificacion decimal(10,2),
foreign key (id_carga_Estudiante) references cargas_estudiantes (id) on delete cascade on update cascade,
foreign key (id_materia) references materias (id) on delete cascade on update cascade,
foreign key (id_parcial) references parciales (id) on delete cascade on update cascade
);
insert into cargas_academicas(id_carga_estudiante, id_materia,id_parcial,calificacion)
values
(1,1,1,'8.5'),
(1,1,2,'7.5'),
(1,1,3,'6.3'),

(1,2,1,'7.5'),
(1,2,2,'7.0'),
(1,2,3,'8.3'),

(1,3,1,'10.0'),
(1,3,2,'9.5'),
(1,3,3,'9.0'),

(1,4,1,'6.5'),
(1,4,2,'6.9'),
(1,4,3,'6.8'),

(1,5,1,'8.0'),
(1,5,2,'7.9'),
(1,5,3,'9.1'),

(1,6,1,'6.5'),
(1,6,2,'5.8'),
(1,6,3,'7.1'),

(1,7,1,'8.0'),
(1,7,2,'8.2'),
(1,7,3,'8.3'),

(2,1,1,'8.5'),
(2,1,2,'8.5'),
(2,1,3,'8.3'),
(2,2,1,'7.5'),
(2,2,2,'7.0'),
(2,2,3,'8.3'),
(2,3,1,'10.0'),
(2,3,2,'9.5'),
(2,3,3,'9.0'),
(2,4,1,'8.5'),
(2,4,2,'9.9'),
(2,4,3,'7.8'),
(2,5,1,'8.0'),
(2,5,2,'7.9'),
(2,5,3,'9.1'),
(2,6,1,'8.5'),
(2,6,2,'7.8'),
(2,6,3,'7.1'),
(2,7,1,'8.0'),
(2,7,2,'8.2'),
(2,7,3,'8.3'),

(3,1,1,'6.5'),
(3,1,2,'5.5'),
(3,1,3,'6.3'),
(3,2,1,'5.5'),
(3,2,2,'4.0'),
(3,2,3,'3.3'),
(3,3,1,'5.0'),
(3,3,2,'6.5'),
(3,3,3,'6.0'),
(3,4,1,'5.5'),
(3,4,2,'7.9'),
(3,4,3,'5.8'),
(3,5,1,'6.0'),
(3,5,2,'4.9'),
(3,5,3,'3.1'),
(3,6,1,'7.5'),
(3,6,2,'6.8'),
(3,6,3,'7.1'),
(3,7,1,'4.0'),
(3,7,2,'5.2'),
(3,7,3,'6.3');

        
select * from cargas_academicas;
select * from cargas_estudiantes;
select * from estudiantes;
select * from materias;
select * from parciales;

select e.id as Matricula, e.nombre as Nombre, m.materia as Materia, p.parcial as Parcial, ca.calificacion as Calificacion from cargas_academicas as ca
inner join cargas_estudiantes as ce
on ca.id_carga_Estudiante=ce.id
inner join estudiantes as e
on ce.id_estudiante=e.id
inner join materias as m
on ca.id_materia=m.id
inner join parciales as p
on ca.id_parcial=p.id
where e.id=1;
