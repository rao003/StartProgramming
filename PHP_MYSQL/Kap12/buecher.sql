-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Erstellungszeit: 15. Jul 2018 um 19:50
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
-- Tabellenstruktur für Tabelle `buecher`
--

CREATE TABLE `buecher` (
  `id` int(11) NOT NULL,
  `titel` varchar(40) NOT NULL,
  `autor` varchar(30) NOT NULL,
  `erscheinungsjahr` int(11) NOT NULL,
  `bewertung` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `buecher`
--

INSERT INTO `buecher` (`id`, `titel`, `autor`, `erscheinungsjahr`, `bewertung`) VALUES
(1, 'Don Quijote', 'Miguel de Cervantes', 1615, '****'),
(2, 'Der Herr der Ringe', 'John R. R. Tolkien', 1955, '*****'),
(3, 'Harry Potter und der Stein der Weisen', 'Joanne K. Rowling', 1997, '****'),
(4, 'Der Alchimist', 'Paulo Coelho', 1988, '*****'),
(5, 'Sakrileg - Der Da Vinci Code', 'Dan Brown', 2003, '***'),
(6, 'Der Adler ist gelandet', 'Jack Higgins', 1975, '****'),
(7, 'Der Name der Rose', 'Umberto Echo', 1980, '*****'),
(8, 'Faust - der Tragödie erster Teil', 'J.W. Goethe', 1808, '*****');

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `buecher`
--
ALTER TABLE `buecher`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `buecher`
--
ALTER TABLE `buecher`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
