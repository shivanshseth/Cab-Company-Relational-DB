--Table structure for table `DEPARTMENT`
DROP DATABASE IF EXISTS `CAB_SERVICE`;
CREATE SCHEMA `CAB_SERVICE`;
USE `CAB_SERVICE`;
DROP TABLE IF EXISTS `DEPARTMENT`;

CREATE TABLE `PERSON` (
  `SSN` varchar(15) NOT NULL,
  `First_name` varchar(20) NOT NULL,
  `Last_name` varchar(20) NOT NULL,
  `Year` int(4) NOT NULL,
  `Month` int(4) NOT NULL,
  `Date` int(4) NOT NULL,
  `Contact` int(10) NOT NULL,
  PRIMARY KEY (`SSN`),
  --CONSTRAINT `DEPARTMENT_ibfk_1` FOREIGN KEY (`Mgr_ssn`) REFERENCES `EMPLOYEE` (`Ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


--
-- Dumping data for table `DEPARTMENT`
--

LOCK TABLES `PERSON` WRITE;
INSERT INTO `PERSON` VALUES ('Headquarters',1,'888665555','1981-06-19'),('Administration',4,'987654321','1995-01-01'),('Research',5,'333445555','1988-05-22');
UNLOCK TABLES;

--
-- Table structure for table `DEPENDENT`
--

DROP TABLE IF EXISTS `RIDE_STATUS`;

CREATE TABLE `RIDE_STATUS` (
  `Status_time` time(9) NOT NULL,
  `Rider_SSN` varchar(15) NOT NULL,
  `Status_details` char(20) DEFAULT NULL,
  PRIMARY KEY (`Status_time`,`Rider_SSN`),
  --CONSTRAINT `DEPENDENT_ibfk_1` FOREIGN KEY (`Essn`) REFERENCES `EMPLOYEE` (`Ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


--
-- Dumping data for table `DEPENDENT`
--

LOCK TABLES `RIDE_STATUS` WRITE;

INSERT INTO `RIDE_STATUS` VALUES ('123456789','Alice','F','1988-12-30','Daughter'),('123456789','Elizabeth','F','1967-05-05','Spouse'),('123456789','Michael','M','1988-01-04','Son'),('333445555','Alice','F','1986-04-05','Daughter'),('333445555','Joy','F','1958-05-03','Spouse'),('333445555','Theodore','M','1983-10-25','Son'),('987654321','Abner','M','1942-02-28','Spouse');

UNLOCK TABLES;

--
-- Table structure for table `DEPT_LOCATIONS`
--

DROP TABLE IF EXISTS `RIDE`;

CREATE TABLE `RIDE` (
  `Request_id` int(11) NOT NULL,
  `Ride_start` time(15) NOT NULL,
  `Ride_end` time(15) NOT NULL,
  `Starting_pos` varchar(15) NOT NULL,
  `Ending_pos` varchar(15) NOT NULL,
  `Shift_id` int(11) NOT NULL,
  `Cab_VRN` varchar(11) NOT NULL,
  `Driver_SSN` varchar(15) NOT NULL,
  PRIMARY KEY (`Request_id`),
  --CONSTRAINT `DEPT_LOCATIONS_ibfk_1` FOREIGN KEY (`Dnumber`) REFERENCES `DEPARTMENT` (`Dnumber`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


--
-- Dumping data for table `DEPT_LOCATIONS`
--

LOCK TABLES `RIDE` WRITE;

INSERT INTO `RIDE` VALUES (1,'Houston'),(4,'Stafford'),(5,'Bellaire'),(5,'Houston'),(5,'Sugarland');

UNLOCK TABLES;

--
-- Table structure for table `EMPLOYEE`
--

DROP TABLE IF EXISTS `RIDER`;
CREATE TABLE `RIDER` (
  `SSN` varchar(15) NOT NULL,
  PRIMARY KEY (`SSN`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


--
-- Dumping data for table `EMPLOYEE`
--

LOCK TABLES `RIDER` WRITE;

INSERT INTO `RIDER` VALUES ('John','B','Smith','123456789','1965-01-09','731 Fondren, Houston, TX','M',30000.00,'333445555',5),('Franklin','T','Wong','333445555','1955-12-08','638 Voss, Houston, TX','M',40000.00,'888665555',5),('Joyce','A','English','453453453','1972-07-31','5631 Rice, Houston, TX','F',25000.00,'333445555',5),('Ramesh','K','Narayan','666884444','1962-09-15','975 Fire Oak, Humble, TX','M',38000.00,'333445555',5),('James','E','Borg','888665555','1937-11-10','450 Stone, Houston, TX','M',55000.00,'NULL',1),('Jennifer','S','Wallace','987654321','1941-06-20','291 Berry, Bellaire, TX','F',43000.00,'888665555',4),('Ahmad','V','Jabbar','987987987','1969-03-29','980 Dallas, Houston, TX','M',25000.00,'987654321',4),('Alicia','J','Zelaya','999887777','1968-01-19','3321 Castle, Spring, TX','F',25000.00,'987654321',4);

UNLOCK TABLES;

--
-- Table structure for table `PROJECT`
--

DROP TABLE IF EXISTS `REQUEST`;
CREATE TABLE `REQUEST` (
  `Request_id` int(11) NOT NULL,
  `Request_time` time(15) NOT NULL,
  `Rider_SSN` varchar(15) NOT NULL,
  PRIMARY KEY (`Request_id`),
  --CONSTRAINT `PROJECT_ibfk_1` FOREIGN KEY (`Dnum`) REFERENCES `DEPARTMENT` (`Dnumber`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `PROJECT`
--

LOCK TABLES `REQUEST` WRITE;

INSERT INTO `REQUEST` VALUES ('ProductX',1,'Bellaire',5),('ProductY',2,'Sugarland',5),('ProductZ',3,'Houston',5),('Computerization',10,'Stafford',4),('Reorganization',20,'Houston',1),('Newbenefits',30,'Stafford',4);

UNLOCK TABLES;

--
-- Table structure for table `WORKS_ON`
--

DROP TABLE IF EXISTS `EMERGENCY_CONTACT`;

CREATE TABLE `EMERGENCY_CONTACT` (
  `Contact` int(10) DEFAULT NULL,
  `Rider_SSN` varchar(15) NOT NULL,
  PRIMARY KEY (`Contact`,`Rider_SSN`),
  --CONSTRAINT `WORKS_ON_ibfk_1` FOREIGN KEY (`Essn`) REFERENCES `EMPLOYEE` (`Ssn`),
  --CONSTRAINT `WORKS_ON_ibfk_2` FOREIGN KEY (`Pno`) REFERENCES `PROJECT` (`Pnumber`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
--
-- Dumping data for table `WORKS_ON`
--

LOCK TABLES `WORKS_ON` WRITE;

INSERT INTO `WORKS_ON` VALUES ('123456789',1,32.5),('123456789',2,7.5),('333445555',2,10.0),('333445555',3,10.0),('333445555',10,10.0),('333445555',20,10.0),('453453453',1,20.0),('453453453',2,20.0),('666884444',3,40.0),('888665555',20,NULL),('987654321',20,15.0),('987654321',30,20.0),('987987987',10,35.0),('987987987',30,5.0),('999887777',10,10.0),('999887777',30,30.0);

UNLOCK TABLES;


DROP TABLE IF EXISTS `DRIVER`;

CREATE TABLE `DRIVER` (
  `SSN` varchar(15) NOT NULL,
  `Availability` int(1) NOT NULL,
  `Licence_number` varchar(15) NOT NULL,  
  PRIMARY KEY (`SSN`),
  --CONSTRAINT `DEPT_LOCATIONS_ibfk_1` FOREIGN KEY (`Dnumber`) REFERENCES `DEPARTMENT` (`Dnumber`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


--
-- Dumping data for table `DEPT_LOCATIONS`
--

LOCK TABLES `DRIVER` WRITE;

INSERT INTO `DRIVER` VALUES (1,'Houston'),(4,'Stafford'),(5,'Bellaire'),(5,'Houston'),(5,'Sugarland');

UNLOCK TABLES;


DROP TABLE IF EXISTS `DRIVER-SHIFT`;

CREATE TABLE `DRIVER-SHIFT` (
  `Shift_id` varchar(15) NOT NULL,
  `Driver_SSN` varchar(15) NOT NULL,
  
  PRIMARY KEY (`SSN`),
  --CONSTRAINT `DEPT_LOCATIONS_ibfk_1` FOREIGN KEY (`Dnumber`) REFERENCES `DEPARTMENT` (`Dnumber`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


--
-- Dumping data for table `DEPT_LOCATIONS`
--

LOCK TABLES `DRIVER` WRITE;

INSERT INTO `DRIVER` VALUES (1,'Houston'),(4,'Stafford'),(5,'Bellaire'),(5,'Houston'),(5,'Sugarland');

UNLOCK TABLES;

