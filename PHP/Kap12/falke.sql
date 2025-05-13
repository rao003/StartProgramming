-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Erstellungszeit: 11. Jun 2018 um 19:40
-- Server-Version: 10.1.21-MariaDB
-- PHP-Version: 7.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `ersteDB`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `falken`
--

CREATE TABLE `falken` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `rasse` varchar(100) NOT NULL,
  `alterTier` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `falken`
--

INSERT INTO `falken` (`id`, `name`, `rasse`, `alterTier`) VALUES
(1, 'Drago', 'Turmfalke', 12),
(2, 'Merlin', 'Turmfalke', 10),
(3, 'Redhead', 'Rotfußfalke', 5),
(4, 'Lancelot', 'Silberfalke', 7),
(5, 'Parzival', 'Buntfalke', 1);

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `falken`
--
ALTER TABLE `falken`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `falken`
--
ALTER TABLE `falken`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
