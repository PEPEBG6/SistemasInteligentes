drop database sistema_orientacion;

create database sistema_orientacion;

use sistema_orientacion;

create table estudiantes(
id int not null primary key auto_increment,
nombre varchar(100),
ap varchar(100),
am varchar(100)
);

create table materias(
id int not null primary key auto_increment,
materia varchar(100)
);

create table carreras(
id int not null primary key auto_increment,
carrera varchar(100)
);

create table grupos(
id int not null primary key auto_increment,
grupo varchar(100)
);

create table periodos(
id int not null primary key auto_increment,
periodo varchar(100)
);

create table parciales(
id int not null primary key auto_increment,
parcial varchar(100)
);

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