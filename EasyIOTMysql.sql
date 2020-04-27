/*
Navicat MySQL Data Transfer

Source Server         : 阿里云数据库
Source Server Version : 50729
Source Host           : 101.37.86.133:3306
Source Database       : IntelligentAgriculture

Target Server Type    : MYSQL
Target Server Version : 50729
File Encoding         : 65001

Date: 2020-04-28 02:48:33
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for Account
-- ----------------------------
DROP TABLE IF EXISTS `Account`;
CREATE TABLE `Account` (
  `account_number` varchar(255) COLLATE utf8_bin NOT NULL,
  `account_username` varchar(255) COLLATE utf8_bin NOT NULL,
  `account_password` varchar(255) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`account_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
