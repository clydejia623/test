DROP TABLE IF EXISTS `ucpaasdelay`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ucpaasdelay` (
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `timeseq` int(4) DEFAULT NULL,
  `delay` int(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28675 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

