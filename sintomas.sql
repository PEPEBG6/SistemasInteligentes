-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jan 26, 2024 at 03:31 PM
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
(16, 'si', NULL, 'si', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 5);

--
-- Indexes for dumped tables
--

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
-- AUTO_INCREMENT for table `sintomas`
--
ALTER TABLE `sintomas`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `sintomas`
--
ALTER TABLE `sintomas`
  ADD CONSTRAINT `a` FOREIGN KEY (`id_paciente`) REFERENCES `pacientes` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
