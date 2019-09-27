
-- ----------------------------
-- Table structure for `lagou`
-- ----------------------------
DROP TABLE IF EXISTS `lagou`;
CREATE TABLE `lagou` (
  `positionName` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `workYear` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `salary` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `companyShortName` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `companyIdInLagou` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `education` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `jobNature` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `positionIdInLagou` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `createTimeInLagou` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `city` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `industryField` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `positionAdvantage` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `companySize` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `score` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `positionLables` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `industryLables` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `publisherId` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `financeStage` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `companyLabelList` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `district` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `businessZones` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `companyFullName` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `firstType` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `secondType` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `isSchoolJob` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `subwayline` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `stationname` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `linestaion` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `resumeProcessRate` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `createByMe` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `keyByMe` varchar(255) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
