-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: j6b104.p.ssafy.io    Database: diete
-- ------------------------------------------------------
-- Server version	8.0.28-0ubuntu0.20.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users_user`
--

DROP TABLE IF EXISTS `users_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_general_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `name` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `birthDate` date NOT NULL,
  `height` decimal(4,1) NOT NULL,
  `weight` decimal(4,1) NOT NULL,
  `activity` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `gender` int NOT NULL,
  `preference` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `kcal` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user`
--

LOCK TABLES `users_user` WRITE;
/*!40000 ALTER TABLE `users_user` DISABLE KEYS */;
INSERT INTO `users_user` VALUES (1,'pbkdf2_sha256$260000$7d6bl0d3FDlIP2DOcTb8J9$hpi684zajZtF4AvrU4yhQEJMw3txAtyIWYeAF3TeRgE=',NULL,0,'admin','','','',0,1,'2022-04-06 06:18:01.905684','관리자','1900-01-01',170.0,70.0,'보통',1,'채소',2002),(2,'pbkdf2_sha256$260000$78YpnJWrQjbVmje1pyFSXt$NPLtB6YLiNDCAAFRXlXMMXC0GNwkwx/cTzylrL8nDV0=',NULL,0,'test1','','','',0,1,'2022-04-06 06:18:46.017606','테스트1','1900-01-01',170.8,48.4,'많음',1,'채소',2327),(3,'pbkdf2_sha256$260000$XVr3FzOYAUzgzEx5cAfH7C$hgty76425r0My11EST2rhpXsLk1OfvjtgIpjmiD1HmM=',NULL,0,'test2','','','',0,1,'2022-04-06 06:19:31.411624','테스트2','1900-01-01',170.0,50.0,'보통',1,'고기',2002),(4,'pbkdf2_sha256$260000$UJuCZizfSUiIJlQxY79qBS$C5cN4TBWjUHgR60YDiBd6pUSpFsg60SUrvMbWrKwQ6I=',NULL,0,'test3','','','',0,1,'2022-04-06 06:20:09.569443','테스트3','1900-01-01',170.0,50.0,'보통',1,'고기',2002),(5,'pbkdf2_sha256$260000$X9aMEY87FlEhPLv7IpFTsv$REaryN98r1YKSV+o1ub3z7CIXXruZVzqEms8IQV3YRw=',NULL,0,'test4','','','',0,1,'2022-04-06 06:25:26.073559','김나린','2000-12-19',170.0,51.0,'많음',1,'채소',2306),(6,'pbkdf2_sha256$260000$3HnsCtX0aPpeNeTjxBQRyH$EKK75qdFf+RihoJJxlhIFlTshABng+4nLcms1GE7NsE=',NULL,0,'codms','','','',0,1,'2022-04-06 06:44:23.474811','한채은','1999-01-07',100.0,100.0,'적음',1,'일반',567),(7,'pbkdf2_sha256$260000$GF2Qdtrw765VB9pRbKMmDZ$jEaDqlRKqJ8dSa7hZ7UeC2hjkuWjywlfUg/0AzFJohg=',NULL,0,'test11','','','',0,1,'2022-04-06 16:08:10.307190','test','1999-04-15',171.0,65.2,'많음',0,'채소',2444),(8,'pbkdf2_sha256$260000$NZmZR0esFypYchPM3AsVyB$mlOixev7DRDnV3rnnfpV1cnc75l4KIMqwm4MUxsFDYg=',NULL,0,'cookie','','','',0,1,'2022-04-06 16:38:28.107384','김쿠키','2000-01-01',163.0,50.0,'많음',1,'채소',2120),(9,'pbkdf2_sha256$260000$OQbLh0C57ijO0L4dfeUSiY$nEP9j/YpY1yumQzNdZXbpiw5/iN5+Ke2VcN0PDwIga0=',NULL,0,'codms1234','','','',0,1,'2022-04-06 16:55:11.014730','채은','1999-01-07',166.0,166.0,'적음',1,'고기',1562),(10,'pbkdf2_sha256$260000$vOWskQT42uo2DCOvJ5p4aD$qx9vofaq1iAgOxeO+OyeynKQlwmskrofoLopB3XzhRg=',NULL,0,'narin','','','',0,1,'2022-04-06 22:13:59.943291','김나린','2000-01-01',170.2,50.0,'보통',1,'채소',2007);
/*!40000 ALTER TABLE `users_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-07 17:41:14
