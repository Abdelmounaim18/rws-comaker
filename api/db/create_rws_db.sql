CREATE DATABASE IF NOT EXISTS `RWS_DB`;
CREATE TABLE IF NOT EXISTS RWS_DB.Roads
(
    `id`           INT      NOT NULL UNIQUE AUTO_INCREMENT,
    `road_name`    TEXT     NOT NULL,
    `last_updated` DATETIME NOT NULL,
    `event_count`  INT      NOT NULL,
    PRIMARY KEY (`id`),
    constraint Roads_pk
        unique (road_name) using hash,
    constraint id
        unique (id)

);
CREATE TABLE IF NOT EXISTS RWS_DB.LaneLocations
(
    `id`           INT  NOT NULL UNIQUE AUTO_INCREMENT,
    `road_name`    TEXT  NOT NULL,
    `km`           TEXT  NOT NULL,
    `lane`         TEXT  NOT NULL,
    `carriage_way` TEXT NOT NULL,
    `uuid`         TEXT NOT NULL,
    PRIMARY KEY (`id`)

);
CREATE TABLE IF NOT EXISTS RWS_DB.Events
(
    `id`         INT      NOT NULL UNIQUE AUTO_INCREMENT,
    `road_name`  TEXT     NOT NULL,
    `avg_speed`  TEXT     NOT NULL,
    `flow_count` TEXT     NOT NULL,
    `ts_event`   TEXT     NOT NULL,
    `uuid`       TEXT     NOT NULL,
    PRIMARY KEY (`id`)

);


