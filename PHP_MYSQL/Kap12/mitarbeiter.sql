-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Erstellungszeit: 16. Jul 2018 um 13:24
-- Server-Version: 10.1.21-MariaDB
-- PHP-Version: 7.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `falconbyte`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `Mitarbeiter`
--

CREATE TABLE `Mitarbeiter` (
  `name` varchar(30) NOT NULL,
  `vorname` varchar(30) NOT NULL,
  `personalnummer` int(11) NOT NULL,
  `gehalt` decimal(8,2) NOT NULL,
  `geburtstag` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `Mitarbeiter`
--

INSERT INTO `Mitarbeiter` (`name`, `vorname`, `personalnummer`, `gehalt`, `geburtstag`) VALUES
('Picard', 'Jean-Luc', 1234, '10000.00', '1988-10-03'),
('Riker', 'William T.', 2100, '7000.00', '1998-10-04'),
('La Forge', 'Geordi', 2120, '5000.00', '1999-01-03'),
('Troi', 'Deanna', 2730, '5000.00', '1997-12-20'),
('Barclay', 'Reginald', 2777, '2000.00', '1997-03-21');

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `Mitarbeiter`
--
ALTER TABLE `Mitarbeiter`
  ADD PRIMARY KEY (`personalnummer`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
