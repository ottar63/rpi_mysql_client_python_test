create database if not exists docker_test;

create user if not exists 'docker_test'@'%'  identified by 'docker_password';

grant all privileges on  docker_test.*  to 'docker_test'@'%';

use docker_test;
CREATE TABLE IF NOT EXISTS `visits` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `host` varchar(255) COLLATE utf8_bin NOT NULL,
    `ip_address` varchar(255) COLLATE utf8_bin NOT NULL,
    `date_time`  datetime,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;
