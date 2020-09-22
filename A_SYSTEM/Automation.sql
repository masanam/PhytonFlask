-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 10, 2019 at 02:34 PM
-- Server version: 5.7.24
-- PHP Version: 7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `automation_2019`
--

-- --------------------------------------------------------

--
-- Table structure for table `bot_task`
--

DROP TABLE IF EXISTS `bot_task`;
CREATE TABLE IF NOT EXISTS `bot_task` (
  `bot_task_id` int(11) NOT NULL AUTO_INCREMENT,
  `bot_task_name` varchar(45) DEFAULT NULL,
  `task_function_count` int(11) DEFAULT NULL,
  `bot_task_type` varchar(45) DEFAULT NULL,
  `bot_task_type_id` int(11) DEFAULT NULL,
  `scene_id` int(11) DEFAULT NULL,
  `bot_task_template_id` int(11) DEFAULT NULL,
  `SN` int(10) NOT NULL,
  `run_count` int(10) NOT NULL DEFAULT '1',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`bot_task_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `bot_task_file`
--

DROP TABLE IF EXISTS `bot_task_file`;
CREATE TABLE IF NOT EXISTS `bot_task_file` (
  `bot_task_file_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `file_name` varchar(45) DEFAULT NULL,
  `file_row` varchar(45) DEFAULT NULL,
  `bot_task_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`bot_task_file_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `bot_task_group`
--

DROP TABLE IF EXISTS `bot_task_group`;
CREATE TABLE IF NOT EXISTS `bot_task_group` (
  `bot_task_group_id` int(11) NOT NULL AUTO_INCREMENT,
  `bot_task_group_template` varchar(45) DEFAULT NULL,
  `bot_task_group_name` varchar(45) DEFAULT NULL,
  `SN` int(11) DEFAULT NULL,
  `bot_task_count` varchar(45) DEFAULT NULL,
  `bot_user_id` int(11) DEFAULT NULL,
  `bot_task_group_template_id` int(11) DEFAULT NULL,
  `bot_task_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`bot_task_group_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `bot_task_group_file`
--

DROP TABLE IF EXISTS `bot_task_group_file`;
CREATE TABLE IF NOT EXISTS `bot_task_group_file` (
  `bot_task_group_file_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `file_name` varchar(45) DEFAULT NULL,
  `file_row` varchar(45) DEFAULT NULL,
  `bot_task_group_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`bot_task_group_file_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `bot_task_group_template`
--

DROP TABLE IF EXISTS `bot_task_group_template`;
CREATE TABLE IF NOT EXISTS `bot_task_group_template` (
  `bot_task_group_template_id` int(11) NOT NULL AUTO_INCREMENT,
  `bot_task_group_template_name` varchar(45) DEFAULT NULL,
  `bot_task_template_count` varchar(45) DEFAULT NULL,
  `bot_user_group` varchar(45) DEFAULT NULL,
  `cloned_create_bot_task_groups` varchar(45) DEFAULT NULL,
  `cloned_create_bot_tasks` varchar(45) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`bot_task_group_template_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `bot_task_group_template_file`
--

DROP TABLE IF EXISTS `bot_task_group_template_file`;
CREATE TABLE IF NOT EXISTS `bot_task_group_template_file` (
  `bot_task_group_template_file_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `file_name` varchar(45) DEFAULT NULL,
  `file_row` varchar(45) DEFAULT NULL,
  `bot_task_group_template_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`bot_task_group_template_file_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `bot_task_template`
--

DROP TABLE IF EXISTS `bot_task_template`;
CREATE TABLE IF NOT EXISTS `bot_task_template` (
  `bot_task_template_id` int(11) NOT NULL AUTO_INCREMENT,
  `bot_task_template_name` varchar(45) DEFAULT NULL,
  `sn_range` varchar(10) DEFAULT NULL,
  `bot_user_group_name` varchar(45) DEFAULT NULL,
  `cloned_create_bot_task_groups` varchar(45) DEFAULT NULL,
  `cloned_create_bot_tasks` varchar(45) DEFAULT NULL,
  `bot_task_group_template` varchar(45) DEFAULT NULL,
  `bot_task_group_template_id` int(11) DEFAULT NULL,
  `space` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`bot_task_template_id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `bot_task_template_file`
--

DROP TABLE IF EXISTS `bot_task_template_file`;
CREATE TABLE IF NOT EXISTS `bot_task_template_file` (
  `bot_task_template_file_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `file_name` varchar(45) DEFAULT NULL,
  `file_row` varchar(45) DEFAULT NULL,
  `bot_task_template_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`bot_task_template_file_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `bot_task_template_tf`
--

DROP TABLE IF EXISTS `bot_task_template_tf`;
CREATE TABLE IF NOT EXISTS `bot_task_template_tf` (
  `bot_task_template_tf_id` int(11) NOT NULL AUTO_INCREMENT,
  `task_function_id` int(11) DEFAULT NULL,
  `task_function` varchar(45) DEFAULT NULL,
  `scene_category_id` int(11) DEFAULT NULL,
  `scene_category` varchar(45) DEFAULT NULL,
  `scene_id` int(11) DEFAULT NULL,
  `scene` varchar(45) DEFAULT NULL,
  `task_value_type_id` int(11) DEFAULT NULL,
  `task_value_type` varchar(50) DEFAULT NULL,
  `task_value_group_id` int(11) DEFAULT NULL,
  `task_value_group` varchar(50) DEFAULT NULL,
  `task_value_count` int(11) DEFAULT NULL,
  `unique_task_value` int(11) DEFAULT NULL,
  `comment` varchar(50) DEFAULT NULL,
  `space` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`bot_task_template_tf_id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `bot_task_type`
--

DROP TABLE IF EXISTS `bot_task_type`;
CREATE TABLE IF NOT EXISTS `bot_task_type` (
  `bot_task_type_id` int(11) NOT NULL AUTO_INCREMENT,
  `bot_task_type_name` varchar(45) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`bot_task_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;


-- --------------------------------------------------------

--
-- Table structure for table `bot_task_type_file`
--

DROP TABLE IF EXISTS `bot_task_type_file`;
CREATE TABLE IF NOT EXISTS `bot_task_type_file` (
  `bot_task_type_file_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `file_name` varchar(45) DEFAULT NULL,
  `file_row` varchar(45) DEFAULT NULL,
  `bot_task_type_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`bot_task_type_file_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `bot_user`
--

DROP TABLE IF EXISTS `bot_user`;
CREATE TABLE IF NOT EXISTS `bot_user` (
  `bot_user_id` int(11) NOT NULL AUTO_INCREMENT,
  `bot_user_type` varchar(45) DEFAULT NULL,
  `first_name` varchar(45) DEFAULT NULL,
  `middle_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `DOB` varchar(45) DEFAULT NULL,
  `country` varchar(45) DEFAULT NULL,
  `state` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `mobile_phone` varchar(45) DEFAULT NULL,
  `home_phone` varchar(45) DEFAULT NULL,
  `occupation` varchar(45) DEFAULT NULL,
  `marital_status` varchar(45) DEFAULT NULL,
  `user_name` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `profile_description` varchar(45) DEFAULT NULL,
  `hobbies_and_interests` varchar(45) DEFAULT NULL,
  `data_1` varchar(45) DEFAULT NULL,
  `data_2` varchar(45) DEFAULT NULL,
  `data_3` varchar(45) DEFAULT NULL,
  `data_4` varchar(45) DEFAULT NULL,
  `data_5` varchar(45) DEFAULT NULL,
  `bot_user_group` varchar(45) DEFAULT NULL,
  `bot_user_group_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`bot_user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `bot_user_file`
--

DROP TABLE IF EXISTS `bot_user_file`;
CREATE TABLE IF NOT EXISTS `bot_user_file` (
  `bot_user_file_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `file_name` varchar(45) DEFAULT NULL,
  `file_row` varchar(45) DEFAULT NULL,
  `bot_user_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`bot_user_file_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `bot_user_group`
--

DROP TABLE IF EXISTS `bot_user_group`;
CREATE TABLE IF NOT EXISTS `bot_user_group` (
  `bot_user_group_id` int(11) NOT NULL AUTO_INCREMENT,
  `bot_user_group_name` varchar(45) DEFAULT NULL,
  `bot_user_count` int(11) DEFAULT NULL,
  `bot_user_type` varchar(45) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`bot_user_group_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `bot_user_group_file`
--

DROP TABLE IF EXISTS `bot_user_group_file`;
CREATE TABLE IF NOT EXISTS `bot_user_group_file` (
  `bot_user_group_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `file_name` varchar(45) DEFAULT NULL,
  `file_row` varchar(45) DEFAULT NULL,
  `bot_user_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`bot_user_group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
CREATE TABLE IF NOT EXISTS `log` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `log_start_date_time`  timestamp NULL DEFAULT NULL,
  `log_end_date_time`  timestamp NULL DEFAULT NULL,
  `log_description` varchar(45) DEFAULT NULL,
  `bot_task_group` varchar(45) DEFAULT NULL,
  `bot_task_group_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `scene`
--

DROP TABLE IF EXISTS `scene`;
CREATE TABLE IF NOT EXISTS `scene` (
  `scene_id` int(11) NOT NULL AUTO_INCREMENT,
  `scene_name` varchar(45) DEFAULT NULL,
  `scene_category` varchar(45) DEFAULT NULL,
  `scene_category_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`scene_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `scene_category`
--

DROP TABLE IF EXISTS `scene_category`;
CREATE TABLE IF NOT EXISTS `scene_category` (
  `scene_category_id` int(11) NOT NULL AUTO_INCREMENT,
  `scene_category_name` varchar(45) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`scene_category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `scene_category_file`
--

DROP TABLE IF EXISTS `scene_category_file`;
CREATE TABLE IF NOT EXISTS `scene_category_file` (
  `scene_category_file_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `file_name` varchar(45) DEFAULT NULL,
  `file_row` varchar(45) DEFAULT NULL,
  `scene_category_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`scene_category_file_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `scene_file`
--

DROP TABLE IF EXISTS `scene_file`;
CREATE TABLE IF NOT EXISTS `scene_file` (
  `scene_file_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `file_name` varchar(45) DEFAULT NULL,
  `file_row` varchar(45) DEFAULT NULL,
  `scene_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`scene_file_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `task_function`
--

DROP TABLE IF EXISTS `task_function`;
CREATE TABLE IF NOT EXISTS `task_function` (
  `task_function_id` int(11) NOT NULL AUTO_INCREMENT,
  `task_function_name` varchar(45) DEFAULT NULL,
  `task_function_content` varchar(45) DEFAULT NULL,
  `bot_task_bot_task_id` int(11) DEFAULT NULL,
  `task_function_category` varchar(45) DEFAULT NULL,
  `task_function_category_id` int(11) DEFAULT NULL,
  `task_value_group` varchar(45) DEFAULT NULL,
  `task_value_group_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`task_function_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;


-- --------------------------------------------------------

--
-- Table structure for table `task_function_category`
--

DROP TABLE IF EXISTS `task_function_category`;
CREATE TABLE IF NOT EXISTS `task_function_category` (
  `task_function_category_id` int(11) NOT NULL AUTO_INCREMENT,
  `task_function_category_name` varchar(45) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`task_function_category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `task_function_category_file`
--

DROP TABLE IF EXISTS `task_function_category_file`;
CREATE TABLE IF NOT EXISTS `task_function_category_file` (
  `task_function_category_file_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `file_name` varchar(45) DEFAULT NULL,
  `file_row` varchar(45) DEFAULT NULL,
  `task_function_category_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`task_function_category_file_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;


-- --------------------------------------------------------

--
-- Table structure for table `task_function_file`
--

DROP TABLE IF EXISTS `task_function_file`;
CREATE TABLE IF NOT EXISTS `task_function_file` (
  `task_function_file_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `file_name` varchar(45) DEFAULT NULL,
  `file_row` varchar(45) DEFAULT NULL,
  `task_function_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`task_function_file_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `task_value`
--

DROP TABLE IF EXISTS `task_value`;
CREATE TABLE IF NOT EXISTS `task_value` (
  `task_value_id` int(11) NOT NULL AUTO_INCREMENT,
  `task_value_name` varchar(45) DEFAULT NULL,
  `task_value_content` varchar(45) DEFAULT NULL,
  `task_value_type` varchar(45) DEFAULT NULL,
  `task_value_type_id` int(11) DEFAULT NULL,
  `task_value_group` varchar(45) DEFAULT NULL,
  `task_value_group_id` int(11) DEFAULT NULL,
  `scene_id` int(11) DEFAULT NULL,
  `scene_category_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`task_value_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `task_value_file`
--

DROP TABLE IF EXISTS `task_value_file`;
CREATE TABLE IF NOT EXISTS `task_value_file` (
  `task_value_file_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `file_name` varchar(45) DEFAULT NULL,
  `file_row` varchar(45) DEFAULT NULL,
  `task_value_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`task_value_file_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;


-- --------------------------------------------------------

--
-- Table structure for table `task_value_group`
--

DROP TABLE IF EXISTS `task_value_group`;
CREATE TABLE IF NOT EXISTS `task_value_group` (
  `task_value_group_id` int(11) NOT NULL AUTO_INCREMENT,
  `task_value_group_name` varchar(45) DEFAULT NULL,
  `task_value_count` varchar(45) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`task_value_group_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `task_value_group_file`
--

DROP TABLE IF EXISTS `task_value_group_file`;
CREATE TABLE IF NOT EXISTS `task_value_group_file` (
  `task_value_group_file_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `file_name` varchar(45) DEFAULT NULL,
  `file_row` varchar(45) DEFAULT NULL,
  `task_value_group_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`task_value_group_file_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `task_value_type`
--

DROP TABLE IF EXISTS `task_value_type`;
CREATE TABLE IF NOT EXISTS `task_value_type` (
  `task_value_type_id` int(11) NOT NULL AUTO_INCREMENT,
  `task_value_type_name` varchar(45) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`task_value_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `task_value_type_file`
--

DROP TABLE IF EXISTS `task_value_type_file`;
CREATE TABLE IF NOT EXISTS `task_value_type_file` (
  `task_value_type_file_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `file_name` varchar(45) DEFAULT NULL,
  `file_row` varchar(45) DEFAULT NULL,
  `task_value_type_id` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`task_value_type_file_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
