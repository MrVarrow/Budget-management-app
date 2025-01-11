-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: budgetappdatabase
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `userquestionnaire`
--

DROP TABLE IF EXISTS `userquestionnaire`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userquestionnaire` (
  `username` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `full_name` varchar(255) DEFAULT NULL,
  `gender` enum('Male','Female','Non-binary','Prefer not to say') DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `education_level` enum('High School','Bachelor''s Degree','Master''s Degree','Doctorate') DEFAULT NULL,
  `marital_status` enum('Married','Single','Divorced','Widowed') DEFAULT NULL,
  `health_condition` enum('Excellent','Good','Fair','Poor') DEFAULT NULL,
  `city_size` enum('Big City','Small City','Town','Rural Area') DEFAULT NULL,
  `salary_range` enum('$0 - $2,000','$2,001 - $5,000','$5,001 - $10,000','$10,001 and above') DEFAULT NULL,
  `credit_card` enum('Yes','No') DEFAULT NULL,
  `consumer_credits` enum('Yes','No') DEFAULT NULL,
  `house_credit` enum('Yes','No') DEFAULT NULL,
  `financial_satisfaction` enum('Very Satisfied','Satisfied','Neutral','Dissatisfied') DEFAULT NULL,
  `travel_abroad_frequency` enum('Never','Once a year','Several times a year','Monthly') DEFAULT NULL,
  `travel_within_country_frequency` enum('Never','Once a year','Several times a year','Monthly') DEFAULT NULL,
  `online_shopping_frequency` enum('Never','Rarely (once a month)','Often (once a week)','Very Often (multiple times a week)') DEFAULT NULL,
  `social_media_frequency` enum('Never','A few times a week','Daily','Multiple times a day') DEFAULT NULL,
  `alcohol_consumption_frequency` enum('Never','Occasionally (social events)','Regularly (a few times a week)','Daily') DEFAULT NULL,
  `smoking_frequency` enum('Never','Occasionally (social events)','Regularly (a few times a week)','Daily') DEFAULT NULL,
  `yearly_savings_goal` varchar(255) DEFAULT NULL,
  `monthly_income_goal` varchar(255) DEFAULT NULL,
  `app_discovery_source` text,
  `improvement_suggestions` text,
  `most_used_functionality` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-11 11:13:31
