-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jan 26, 2024 at 08:12 PM
-- Server version: 8.0.30
-- PHP Version: 8.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `consultasmed`
--

-- --------------------------------------------------------

--
-- Table structure for table `consultas`
--

CREATE TABLE `consultas` (
  `id` int NOT NULL,
  `id_medico` int NOT NULL,
  `id_diagnosticos` int NOT NULL,
  `id_consultorio` int NOT NULL,
  `fecha_consulta` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `consultas`
--

INSERT INTO `consultas` (`id`, `id_medico`, `id_diagnosticos`, `id_consultorio`, `fecha_consulta`) VALUES
(11, 1, 2, 2, '2024-01-26'),
(12, 1, 3, 2, '2024-01-26'),
(13, 1, 4, 1, '2024-01-26'),
(14, 1, 5, 3, '2024-01-26'),
(15, 1, 6, 3, '2024-01-26'),
(16, 1, 7, 2, '2024-01-26'),
(17, 1, 8, 2, '2024-01-26');

-- --------------------------------------------------------

--
-- Table structure for table `consultorios`
--

CREATE TABLE `consultorios` (
  `id` int NOT NULL,
  `nombre` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `consultorios`
--

INSERT INTO `consultorios` (`id`, `nombre`) VALUES
(1, 'pediatria'),
(2, 'general'),
(3, 'tres');

-- --------------------------------------------------------

--
-- Table structure for table `diagnosticos`
--

CREATE TABLE `diagnosticos` (
  `id` int NOT NULL,
  `id_sintoma` int NOT NULL,
  `id_enfermedad` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `diagnosticos`
--

INSERT INTO `diagnosticos` (`id`, `id_sintoma`, `id_enfermedad`) VALUES
(1, 18, 1),
(2, 19, 1),
(3, 22, 1),
(4, 23, 4),
(5, 24, 3),
(6, 25, 6),
(7, 26, 1),
(8, 27, 4);

-- --------------------------------------------------------

--
-- Table structure for table `enfermedades`
--

CREATE TABLE `enfermedades` (
  `id` int NOT NULL,
  `enfermedad` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `enfermedades`
--

INSERT INTO `enfermedades` (`id`, `enfermedad`) VALUES
(1, 'covid-19\r\n'),
(2, 'influenza'),
(3, 'gripe'),
(4, 'resfriado común'),
(5, 'Covid-19 o Infección respiratoria'),
(6, 'Probablemente otro tipo de enfermedad, consulte a otro especialista');

-- --------------------------------------------------------

--
-- Table structure for table `especialidades`
--

CREATE TABLE `especialidades` (
  `id` int NOT NULL,
  `especialidad` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `especialidades`
--

INSERT INTO `especialidades` (`id`, `especialidad`) VALUES
(1, 'Medico general');

-- --------------------------------------------------------

--
-- Table structure for table `medicos`
--

CREATE TABLE `medicos` (
  `id` int NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `ap` varchar(100) DEFAULT NULL,
  `am` varchar(100) DEFAULT NULL,
  `id_especialidad` int NOT NULL,
  `cedula` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `medicos`
--

INSERT INTO `medicos` (`id`, `nombre`, `ap`, `am`, `id_especialidad`, `cedula`) VALUES
(1, 'Diego', 'Zamora', 'Narvaez', 1, '12122121212');

-- --------------------------------------------------------

--
-- Table structure for table `pacientes`
--

CREATE TABLE `pacientes` (
  `id` int NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `ap` varchar(100) DEFAULT NULL,
  `am` varchar(100) DEFAULT NULL,
  `curp` varchar(100) DEFAULT NULL,
  `fecha_nac` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `pacientes`
--

INSERT INTO `pacientes` (`id`, `nombre`, `ap`, `am`, `curp`, `fecha_nac`) VALUES
(5, 'Diego ', 'Zamora', 'Narvaez', 'ZAND021217HQTMRGA1', '2002-12-17'),
(6, 'asd', 'asd', 'asd', 'xAND9012834E09284S', '1969-01-26'),
(8, 'asda', 'dasd', 'asd', 'ZAND021217HQTMRGA2', '2014-01-08'),
(9, 'asdasddad', 'adadad', 'sadadads', 'A21342343424324234', '2000-07-29');

-- --------------------------------------------------------

--
-- Table structure for table `sintomas`
--

CREATE TABLE `sintomas` (
  `id` int NOT NULL,
  `dificultadRespirar` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `presionPecho` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `perdidaGustoOlfato` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `dolorPecho` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `mareosConvulsiones` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `fiebreAlta` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `mareos2` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `tos` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `dolorGarganta` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `goteoNariz` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `id_paciente` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `sintomas`
--

INSERT INTO `sintomas` (`id`, `dificultadRespirar`, `presionPecho`, `perdidaGustoOlfato`, `dolorPecho`, `mareosConvulsiones`, `fiebreAlta`, `mareos2`, `tos`, `dolorGarganta`, `goteoNariz`, `id_paciente`) VALUES
(12, 'si', NULL, 'si', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 5),
(13, 'no', 'no', NULL, NULL, NULL, NULL, NULL, 'no', NULL, NULL, 5),
(14, 'si', NULL, 'si', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 5),
(15, 'si', NULL, 'si', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 5),
(16, 'si', NULL, 'si', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 5),
(17, 'si', NULL, 'si', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 5),
(18, 'si', NULL, 'si', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 5),
(19, 'si', NULL, 'si', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 5),
(20, 'si', NULL, 'si', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 5),
(21, 'si', NULL, 'si', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 5),
(22, 'si', NULL, 'si', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 5),
(23, 'no', 'no', NULL, NULL, NULL, NULL, NULL, 'si', 'si', 'no', 8),
(24, 'si', NULL, 'no', 'no', 'no', 'no', NULL, NULL, NULL, NULL, 6),
(25, 'no', 'no', NULL, NULL, NULL, NULL, NULL, 'no', NULL, NULL, 6),
(26, 'si', NULL, 'si', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 9),
(27, 'no', 'no', NULL, NULL, NULL, NULL, NULL, 'si', 'si', 'no', 9);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `consultas`
--
ALTER TABLE `consultas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_medico` (`id_medico`),
  ADD KEY `id_consultorio` (`id_consultorio`),
  ADD KEY `zs` (`id_diagnosticos`);

--
-- Indexes for table `consultorios`
--
ALTER TABLE `consultorios`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `diagnosticos`
--
ALTER TABLE `diagnosticos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_sintoma` (`id_sintoma`),
  ADD KEY `id_enfermedad` (`id_enfermedad`);

--
-- Indexes for table `enfermedades`
--
ALTER TABLE `enfermedades`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `especialidades`
--
ALTER TABLE `especialidades`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `medicos`
--
ALTER TABLE `medicos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_especialidad` (`id_especialidad`);

--
-- Indexes for table `pacientes`
--
ALTER TABLE `pacientes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `curp` (`curp`);

--
-- Indexes for table `sintomas`
--
ALTER TABLE `sintomas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `a` (`id_paciente`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `consultas`
--
ALTER TABLE `consultas`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `consultorios`
--
ALTER TABLE `consultorios`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `diagnosticos`
--
ALTER TABLE `diagnosticos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `enfermedades`
--
ALTER TABLE `enfermedades`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `especialidades`
--
ALTER TABLE `especialidades`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `medicos`
--
ALTER TABLE `medicos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `pacientes`
--
ALTER TABLE `pacientes`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `sintomas`
--
ALTER TABLE `sintomas`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `consultas`
--
ALTER TABLE `consultas`
  ADD CONSTRAINT `consultas_ibfk_1` FOREIGN KEY (`id_medico`) REFERENCES `medicos` (`id`),
  ADD CONSTRAINT `consultas_ibfk_4` FOREIGN KEY (`id_consultorio`) REFERENCES `consultorios` (`id`),
  ADD CONSTRAINT `zs` FOREIGN KEY (`id_diagnosticos`) REFERENCES `diagnosticos` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `diagnosticos`
--
ALTER TABLE `diagnosticos`
  ADD CONSTRAINT `diagnosticos_ibfk_1` FOREIGN KEY (`id_sintoma`) REFERENCES `sintomas` (`id`),
  ADD CONSTRAINT `diagnosticos_ibfk_2` FOREIGN KEY (`id_enfermedad`) REFERENCES `enfermedades` (`id`);

--
-- Constraints for table `medicos`
--
ALTER TABLE `medicos`
  ADD CONSTRAINT `medicos_ibfk_1` FOREIGN KEY (`id_especialidad`) REFERENCES `especialidades` (`id`);

--
-- Constraints for table `sintomas`
--
ALTER TABLE `sintomas`
  ADD CONSTRAINT `a` FOREIGN KEY (`id_paciente`) REFERENCES `pacientes` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
