/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/ heroku_4bac0100237dacf /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE heroku_4bac0100237dacf;

DROP TABLE IF EXISTS approvals;
CREATE TABLE `approvals` (
  `Mail_Id` varchar(30) DEFAULT NULL,
  `Club_Name` varchar(40) DEFAULT NULL,
  `CurrentStatus` varchar(1) DEFAULT NULL,
  KEY `Mail_Id` (`Mail_Id`),
  CONSTRAINT `approvals_ibfk_1` FOREIGN KEY (`Mail_Id`) REFERENCES `students` (`Mail_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS clubheads;
CREATE TABLE `clubheads` (
  `Club_Head_Mail_Id` varchar(30) DEFAULT NULL,
  `Club_Title` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS clubmembers;
CREATE TABLE `clubmembers` (
  `Mail_Id` varchar(30) NOT NULL DEFAULT '',
  `Club_Name` varchar(60) NOT NULL DEFAULT '',
  PRIMARY KEY (`Mail_Id`,`Club_Name`),
  KEY `Club_Name` (`Club_Name`),
  CONSTRAINT `clubmembers_ibfk_1` FOREIGN KEY (`Mail_Id`) REFERENCES `students` (`Mail_id`) ON DELETE CASCADE,
  CONSTRAINT `clubmembers_ibfk_2` FOREIGN KEY (`Club_Name`) REFERENCES `clubs` (`Club_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS clubs;
CREATE TABLE `clubs` (
  `Title` varchar(50) DEFAULT NULL,
  `Club_Name` varchar(60) NOT NULL,
  `Info` varchar(2000) DEFAULT NULL,
  `Achievements` varchar(2000) DEFAULT NULL,
  `Year_Established` decimal(4,0) DEFAULT NULL,
  `Type_Of_Club` varchar(1) DEFAULT NULL,
  `Webstie` varchar(100) DEFAULT NULL,
  `Club_Head_Mail_Id` varchar(30) DEFAULT NULL,
  `Club_Head_Name` varchar(100) DEFAULT NULL,
  `events` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`Club_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS events;
CREATE TABLE `events` (
  `club_title` varchar(50) DEFAULT NULL,
  `club_event` varchar(2000) DEFAULT NULL,
  `dated` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS manages;
CREATE TABLE `manages` (
  `emp_id` int(11) NOT NULL,
  `employee_name` varchar(225) DEFAULT NULL,
  `manager_name` varchar(225) DEFAULT NULL,
  PRIMARY KEY (`emp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS meetings;
CREATE TABLE `meetings` (
  `host_mail_id` varchar(30) NOT NULL DEFAULT '',
  `student_mail_id` varchar(30) NOT NULL DEFAULT '',
  `meeting_time` time DEFAULT NULL,
  `meeting_date` date DEFAULT NULL,
  `link` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`host_mail_id`,`student_mail_id`),
  KEY `student_mail_id` (`student_mail_id`),
  CONSTRAINT `meetings_ibfk_1` FOREIGN KEY (`host_mail_id`) REFERENCES `students` (`Mail_id`) ON DELETE CASCADE,
  CONSTRAINT `meetings_ibfk_2` FOREIGN KEY (`student_mail_id`) REFERENCES `students` (`Mail_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS students;
CREATE TABLE `students` (
  `Mail_id` varchar(30) NOT NULL,
  `Full_Name` varchar(50) DEFAULT NULL,
  `LinkedIn` varchar(30) DEFAULT NULL,
  `Branch` varchar(5) DEFAULT NULL,
  `Roll_No` decimal(9,0) DEFAULT NULL,
  `Phone_No` decimal(10,0) DEFAULT NULL,
  `Current_Year` decimal(1,0) DEFAULT NULL,
  `Bio` varchar(4200) DEFAULT NULL,
  PRIMARY KEY (`Mail_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS works;
CREATE TABLE `works` (
  `emp_id` int(11) NOT NULL,
  `employee_name` varchar(225) DEFAULT NULL,
  `department_name` varchar(225) DEFAULT NULL,
  `job_title` varchar(225) DEFAULT NULL,
  `annual_salary` int(11) DEFAULT NULL,
  `notes` varchar(225) DEFAULT NULL,
  PRIMARY KEY (`emp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
