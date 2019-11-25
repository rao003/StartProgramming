-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Erstellungszeit: 13. Jun 2019 um 18:33
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
-- Tabellenstruktur für Tabelle `zimmer`
--

CREATE TABLE `zimmer` (
  `id` int(11) NOT NULL,
  `zimmernummer` int(11) NOT NULL,
  `kategorie` varchar(20) NOT NULL,
  `preis_nacht` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 ROW_FORMAT=COMPACT;

--
-- Daten für Tabelle `zimmer`
--

INSERT INTO `zimmer` (`id`, `zimmernummer`, `kategorie`, `preis_nacht`) VALUES
(1, 201, 'standard', 59),
(2, 202, 'standard', 59),
(3, 203, 'standard', 67),
(4, 204, 'standard', 65),
(5, 205, 'standard', 44),
(6, 206, 'standard', 79),
(7, 207, 'standard', 79),
(8, 208, 'standard', 51),
(9, 209, 'standard', 49),
(10, 301, 'deluxe', 119),
(11, 302, 'deluxe', 109),
(12, 303, 'deluxe', 135),
(13, 304, 'deluxe', 159),
(14, 305, 'deluxe', 150),
(15, 401, 'Suite', 559);

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `zimmer`
--
ALTER TABLE `zimmer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `zimmernummer` (`zimmernummer`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `zimmer`
--
ALTER TABLE `zimmer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
