-- MySQL dump 10.13  Distrib 5.7.28, for macos10.14 (x86_64)
--
-- Host: localhost    Database: axf
-- ------------------------------------------------------
-- Server version	5.7.28

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

--
-- Table structure for table `auth_group`
--

--
-- Table structure for table `axf_cart`
--

DROP TABLE IF EXISTS `axf_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `axf_cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `c_goods_num` int(11) NOT NULL,
  `c_is_select` tinyint(1) NOT NULL,
  `c_goods_id` int(11) DEFAULT NULL,
  `c_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `axf_cart_c_goods_id_85ddfb56_fk_axf_goods_id` (`c_goods_id`),
  KEY `axf_cart_c_user_id_5abdebfe_fk_axf_user_id` (`c_user_id`),
  CONSTRAINT `axf_cart_c_goods_id_85ddfb56_fk_axf_goods_id` FOREIGN KEY (`c_goods_id`) REFERENCES `axf_goods` (`id`),
  CONSTRAINT `axf_cart_c_user_id_5abdebfe_fk_axf_user_id` FOREIGN KEY (`c_user_id`) REFERENCES `axf_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `axf_cart`
--

LOCK TABLES `axf_cart` WRITE;
/*!40000 ALTER TABLE `axf_cart` DISABLE KEYS */;
/*!40000 ALTER TABLE `axf_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `axf_foodtype`
--

DROP TABLE IF EXISTS `axf_foodtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `axf_foodtype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `typeid` int(11) NOT NULL,
  `typename` varchar(32) NOT NULL,
  `childtypenames` varchar(255) NOT NULL,
  `typesort` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `axf_foodtype`
--

LOCK TABLES `axf_foodtype` WRITE;
/*!40000 ALTER TABLE `axf_foodtype` DISABLE KEYS */;
/*!40000 ALTER TABLE `axf_foodtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `axf_goods`
--

DROP TABLE IF EXISTS `axf_goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `axf_goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `productid` int(11) NOT NULL,
  `productimg` varchar(255) NOT NULL,
  `productname` varchar(128) NOT NULL,
  `productlongname` varchar(255) NOT NULL,
  `isxf` tinyint(1) NOT NULL,
  `pmdesc` tinyint(1) NOT NULL,
  `specifics` varchar(64) NOT NULL,
  `price` double NOT NULL,
  `marketprice` double NOT NULL,
  `categoryid` int(11) NOT NULL,
  `childcid` int(11) NOT NULL,
  `childcidname` varchar(128) NOT NULL,
  `dealerid` int(11) NOT NULL,
  `storenums` int(11) NOT NULL,
  `productnum` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `axf_goods`
--

LOCK TABLES `axf_goods` WRITE;
/*!40000 ALTER TABLE `axf_goods` DISABLE KEYS */;
/*!40000 ALTER TABLE `axf_goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `axf_mainshow`
--

DROP TABLE IF EXISTS `axf_mainshow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `axf_mainshow` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img` varchar(255) NOT NULL,
  `name` varchar(64) NOT NULL,
  `trackid` int(11) NOT NULL,
  `categoryid` int(11) NOT NULL,
  `brandname` varchar(64) NOT NULL,
  `img1` varchar(255) NOT NULL,
  `childcid1` int(11) NOT NULL,
  `productid1` int(11) NOT NULL,
  `longname1` varchar(128) NOT NULL,
  `price1` double NOT NULL,
  `marketprice1` double NOT NULL,
  `img2` varchar(255) NOT NULL,
  `childcid2` int(11) NOT NULL,
  `productid2` int(11) NOT NULL,
  `longname2` varchar(128) NOT NULL,
  `price2` double NOT NULL,
  `marketprice2` double NOT NULL,
  `img3` varchar(255) NOT NULL,
  `childcid3` int(11) NOT NULL,
  `productid3` int(11) NOT NULL,
  `longname3` varchar(128) NOT NULL,
  `price3` double NOT NULL,
  `marketprice3` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `axf_mainshow`
--

LOCK TABLES `axf_mainshow` WRITE;
/*!40000 ALTER TABLE `axf_mainshow` DISABLE KEYS */;
/*!40000 ALTER TABLE `axf_mainshow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `axf_mustbuy`
--

DROP TABLE IF EXISTS `axf_mustbuy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `axf_mustbuy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img` varchar(255) NOT NULL,
  `name` varchar(64) NOT NULL,
  `trackid` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `axf_mustbuy`
--

LOCK TABLES `axf_mustbuy` WRITE;
/*!40000 ALTER TABLE `axf_mustbuy` DISABLE KEYS */;
/*!40000 ALTER TABLE `axf_mustbuy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `axf_nav`
--

DROP TABLE IF EXISTS `axf_nav`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `axf_nav` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img` varchar(255) NOT NULL,
  `name` varchar(64) NOT NULL,
  `trackid` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `axf_nav`
--

LOCK TABLES `axf_nav` WRITE;
/*!40000 ALTER TABLE `axf_nav` DISABLE KEYS */;
/*!40000 ALTER TABLE `axf_nav` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `axf_order`
--

DROP TABLE IF EXISTS `axf_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `axf_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `o_price` double NOT NULL,
  `o_time` datetime(6) NOT NULL,
  `o_status` int(11) NOT NULL,
  `o_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `axf_order_o_user_id_a23247bb_fk_axf_user_id` (`o_user_id`),
  CONSTRAINT `axf_order_o_user_id_a23247bb_fk_axf_user_id` FOREIGN KEY (`o_user_id`) REFERENCES `axf_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `axf_order`
--

LOCK TABLES `axf_order` WRITE;
/*!40000 ALTER TABLE `axf_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `axf_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `axf_ordergoods`
--

DROP TABLE IF EXISTS `axf_ordergoods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `axf_ordergoods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `o_goods_num` int(11) NOT NULL,
  `o_goods_id` int(11) DEFAULT NULL,
  `o_order_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `axf_ordergoods_o_goods_id_f5c54400_fk_axf_goods_id` (`o_goods_id`),
  KEY `axf_ordergoods_o_order_id_35bb0edb_fk_axf_order_id` (`o_order_id`),
  CONSTRAINT `axf_ordergoods_o_goods_id_f5c54400_fk_axf_goods_id` FOREIGN KEY (`o_goods_id`) REFERENCES `axf_goods` (`id`),
  CONSTRAINT `axf_ordergoods_o_order_id_35bb0edb_fk_axf_order_id` FOREIGN KEY (`o_order_id`) REFERENCES `axf_order` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `axf_ordergoods`
--

LOCK TABLES `axf_ordergoods` WRITE;
/*!40000 ALTER TABLE `axf_ordergoods` DISABLE KEYS */;
/*!40000 ALTER TABLE `axf_ordergoods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `axf_shop`
--

DROP TABLE IF EXISTS `axf_shop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `axf_shop` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img` varchar(255) NOT NULL,
  `name` varchar(64) NOT NULL,
  `trackid` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `axf_shop`
--

LOCK TABLES `axf_shop` WRITE;
/*!40000 ALTER TABLE `axf_shop` DISABLE KEYS */;
/*!40000 ALTER TABLE `axf_shop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `axf_user`
--

DROP TABLE IF EXISTS `axf_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `axf_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `u_username` varchar(32) NOT NULL,
  `u_password` varchar(256) NOT NULL,
  `u_email` varchar(64) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `u_username` (`u_username`),
  UNIQUE KEY `u_email` (`u_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `axf_user`
--

LOCK TABLES `axf_user` WRITE;
/*!40000 ALTER TABLE `axf_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `axf_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `axf_wheel`
--

DROP TABLE IF EXISTS `axf_wheel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `axf_wheel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img` varchar(255) NOT NULL,
  `name` varchar(64) NOT NULL,
  `trackid` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `axf_wheel`
--

LOCK TABLES `axf_wheel` WRITE;
/*!40000 ALTER TABLE `axf_wheel` DISABLE KEYS */;
/*!40000 ALTER TABLE `axf_wheel` ENABLE KEYS */;
UNLOCK TABLES;

