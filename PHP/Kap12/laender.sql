-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Erstellungszeit: 23. Jun 2018 um 15:54
-- Server-Version: 10.1.21-MariaDB
-- PHP-Version: 7.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `DatenbankX1`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `laender`
--

CREATE TABLE `laender` (
  `nummer` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `einwohner` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `laender`
--

INSERT INTO `laender` (`nummer`, `name`, `einwohner`) VALUES
(1, 'Deutschland', 82000000),
(2, 'England', 53000000),
(3, 'Island', 330000),
(4, 'Österreich', 8800000),
(5, 'Italien', 60000000),
(6, 'USA', 325000000),
(7, 'Russland', 144000000),
(8, 'Spanien', 46000000),
(9, 'Schweiz', 8000000),
(10, 'Griechenland', 10000000);

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `laender`
--
ALTER TABLE `laender`
  ADD PRIMARY KEY (`nummer`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
