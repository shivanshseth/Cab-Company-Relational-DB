-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: Company
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON * . * TO 'admin'@'localhost';

CREATE USER IF NOT EXISTS 'rider'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON * . * TO 'rider'@'localhost';

CREATE USER IF NOT EXISTS 'driver'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON * . * TO 'driver'@'localhost';

DROP DATABASE IF EXISTS `CAB_SERVICE`;
CREATE SCHEMA `CAB_SERVICE`;
USE `CAB_SERVICE`;

DROP TABLE IF EXISTS `PERSON`;
CREATE TABLE `PERSON` (
  `SSN` varchar(15) NOT NULL,
  `First_name` varchar(20) NOT NULL,
  `Last_name` varchar(20) NOT NULL,
  `Year` int(4) NOT NULL,
  `Month` int(4) NOT NULL,
  `Day` int(4) NOT NULL,
  `Contact` bigint(10) NOT NULL,
  PRIMARY KEY (`SSN`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `PERSON` WRITE;
INSERT INTO `PERSON` VALUES ('1341-3108-1298' ,'Raju' ,'Rajput', '1985' ,'12' ,'23' ,'9873245782'), ('1298-3108-1298' ,'Ramesh' ,'Patel', '1982' ,'12' ,'23' ,'9873283782'),('2384-4393-3698' ,'Yeet' ,'Boi' ,'1999' ,'1' ,'15' ,'7563283782'), ('3423-1234-3238' ,'Gameboy' ,'Mangale' ,'1999' ,'1' ,'15' ,'7563252782');
UNLOCK TABLES;


DROP TABLE IF EXISTS `SHIFT`;
CREATE TABLE `SHIFT` (
  `Shift_id` int NOT NULL AUTO_INCREMENT,
  `Start_time` time(6) NOT NULL,
  `End_time` time(6) NOT NULL,
  
  PRIMARY KEY (`Shift_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `SHIFT` WRITE;
INSERT INTO `SHIFT` VALUES ('1' ,'15:00' ,'23:00'), ('2' ,'06:00' ,'13:00');
UNLOCK TABLES;


DROP TABLE IF EXISTS `DRIVER`;
CREATE TABLE `DRIVER` (
  `SSN` varchar(15) NOT NULL,
  `Availability` char(5) NOT NULL,
  `License_number` varchar(15) NOT NULL,  
  PRIMARY KEY (`SSN`),
  UNIQUE KEY `License_number` (`License_number`),
  FOREIGN Key (`SSN`) REFERENCES `PERSON` (`SSN`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `DRIVER` WRITE;
INSERT INTO `DRIVER` VALUES ('1298-3108-1298' ,'True', '9313-2384-1383'), ('1341-3108-1298', 'True', '3412-4341-3412');
UNLOCK TABLES;


DROP TABLE IF EXISTS `RIDER`;
CREATE TABLE `RIDER` (
  `SSN` varchar(15) NOT NULL,
  PRIMARY KEY (`SSN`) ,
  FOREIGN Key (`SSN`) REFERENCES `PERSON` (`SSN`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `RIDER` WRITE;
INSERT INTO `RIDER` VALUES ('2384-4393-3698'), ('3423-1234-3238');
UNLOCK TABLES;


DROP TABLE IF EXISTS `REQUEST`;
CREATE TABLE `REQUEST` (
  `Request_id` int(11) NOT NULL,  
  `Request_time` time(6) NOT NULL,
  `Rider_SSN` varchar(15) NOT NULL,
  PRIMARY KEY (`Request_id`),
  FOREIGN Key (`Rider_SSN`) REFERENCES `RIDER` (`SSN`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `REQUEST` WRITE;
INSERT INTO `REQUEST` VALUES ('1','18:00','2384-4393-3698');
UNLOCK TABLES;


DROP TABLE IF EXISTS `RIDE_STATUS`;
CREATE TABLE `RIDE_STATUS` (
  `Status_time` time(6) NOT NULL,
  `Rider_SSN` varchar(15) NOT NULL,
  `Status_details` char(20) DEFAULT NULL,
  PRIMARY KEY (`Status_time`,`Rider_SSN`),
  FOREIGN Key (`Rider_SSN`) REFERENCES `RIDER` (`SSN`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `RIDE_STATUS` WRITE;
INSERT INTO `RIDE_STATUS` VALUES ('2384-4393-3698', '18:30' ,'Travelling');
UNLOCK TABLES;


DROP TABLE IF EXISTS `CAR_MODEL`;
CREATE TABLE `CAR_MODEL` (
  `Model_id` varchar(10) NOT NULL,
  `Company` varchar(20) NOT NULL,
  `Class` varchar(10) DEFAULT NULL,

  PRIMARY KEY (`Model_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `CAR_MODEL` WRITE;
INSERT INTO `CAR_MODEL` VALUES ('asdf' ,'Suzuki' ,'Sedan'), ('qwer', 'Audi', 'SUV'), ('nano', 'Tata', 'Micro');
UNLOCK TABLES;

DROP TABLE IF EXISTS `CAB`;
CREATE TABLE `CAB` (
  `VRN` varchar(11) NOT NULL,
  `Manufacture_Year` int(4) NOT NULL,
  `Availability` char(5) NOT NULL,
  `Model_id` varchar(10) NOT NULL,
  
  PRIMARY KEY (`VRN`),
  FOREIGN Key (`Model_id`) REFERENCES `CAR_MODEL` (`Model_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `CAB` WRITE;
INSERT INTO `CAB` VALUES ('TS08UB3193','2009','True','asdf'), ('TS18ZB4393','2007','True','qwer'), ('TS75BT3421','2007','True','nano');
UNLOCK TABLES;


DROP TABLE IF EXISTS `RIDE`;
CREATE TABLE `RIDE` (
  `Request_id` int(11) NOT NULL,
  `Ride_start` time(6) NOT NULL,
  `Ride_end` time(6),
  `Starting_pos` varchar(50) NOT NULL,
  `Ending_pos` varchar(50) NOT NULL,
  `Shift_id` int(15) NOT NULL,
  `Cab_VRN` varchar(11) NOT NULL,
  `Driver_SSN` varchar(15) NOT NULL,
  PRIMARY KEY (`Request_id`),
  FOREIGN Key (`Request_id`) REFERENCES `REQUEST` (`Request_id`) ON DELETE CASCADE,
  FOREIGN Key (`Shift_id`) REFERENCES `SHIFT` (`Shift_id`) ON DELETE CASCADE,
  FOREIGN Key (`Cab_VRN`) REFERENCES `CAB` (`VRN`) ON DELETE CASCADE,
  FOREIGN Key (`Driver_SSN`) REFERENCES `DRIVER` (`SSN`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `RIDE` WRITE;
INSERT INTO `RIDE` VALUES ('1','18:10' ,'18:40','21/3,PaitApartments,Gachibowli' ,'PVR Mall,Gachibowli','1','1298-3108-1298','TS08UB3193');
UNLOCK TABLES;


DROP TABLE IF EXISTS `EMERGENCY_CONTACT`;
CREATE TABLE `EMERGENCY_CONTACT` (
  `Contact` bigint(10) NOT NULL,
  `Rider_SSN` varchar(15) NOT NULL,
  PRIMARY KEY (`Contact`,`Rider_SSN`),
  FOREIGN Key (`Rider_SSN`) REFERENCES `RIDER` (`SSN`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `EMERGENCY_CONTACT` WRITE;
INSERT INTO `EMERGENCY_CONTACT` VALUES ('7000010110','2384-4393-3698'),('7000010115','2384-4393-3699');
UNLOCK TABLES;



DROP TABLE IF EXISTS `DRIVER_SHIFT`;
CREATE TABLE `DRIVER_SHIFT` (
  `Driver_SSN` varchar(15) NOT NULL,
  `Shift_id` int NOT NULL,
  
  PRIMARY KEY (`Driver_SSN`,`Shift_id`),
  FOREIGN Key (`Shift_id`) REFERENCES `SHIFT` (`Shift_id`) ON DELETE CASCADE,
  FOREIGN Key (`Driver_SSN`) REFERENCES `DRIVER` (`SSN`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `DRIVER_SHIFT` WRITE;
INSERT INTO `DRIVER_SHIFT` VALUES ('1298-3108-1298', '1'), ('1298-3108-1298', '2'), ('1341-3108-1298', '2');
UNLOCK TABLES;

DROP TABLE IF EXISTS `CAB_SHIFT`;
CREATE TABLE `CAB_SHIFT` (
  `VRN` varchar(11) NOT NULL,
  `Shift_id` int NOT NULL,

  PRIMARY KEY (`VRN`,`Shift_id`),
  FOREIGN Key (`VRN`) REFERENCES `CAB` (`VRN`) ON DELETE CASCADE,
  FOREIGN Key (`Shift_id`) REFERENCES `SHIFT` (`Shift_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `CAB_SHIFT` WRITE;
INSERT INTO `CAB_SHIFT` VALUES ('TS08UB3193','1'), ('TS18ZB4393', '2'), ('TS75BT3421', '1'), ('TS08UB3193','2');
UNLOCK TABLES;


DROP TABLE IF EXISTS `ACCIDENT`;
CREATE TABLE `ACCIDENT` (
  `Accident_time` time(6) NOT NULL,
  `Driver_SSN` varchar(15) NOT NULL,
  `Location` varchar(50) NOT NULL,
  
  PRIMARY KEY (`Accident_time`,`Driver_SSN`),
  FOREIGN Key (`Driver_SSN`) REFERENCES `DRIVER` (`SSN`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `ACCIDENT` WRITE;
INSERT INTO `ACCIDENT` VALUES ('23:00','1298-3108-1298','The Shire, Yeetland, Hyderabad');
UNLOCK TABLES;


DROP TABLE IF EXISTS `CAB_COLOR`;
CREATE TABLE `CAB_COLOR` (
  `VRN` varchar(11) NOT NULL,
  `COLOR` varchar(15) NOT NULL,
  
  PRIMARY KEY (`VRN`,`COLOR`),
  FOREIGN Key (`VRN`) REFERENCES `CAB` (`VRN`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `CAB_COLOR` WRITE;
INSERT INTO `CAB_COLOR` VALUES ('TS08UB3193', 'Red'), ('TS08UB3193','Blue'), ('TS18ZB4393', 'Black'), ('TS75BT3421', 'Black');
UNLOCK TABLES;