CREATE DATABASE IF NOT EXISTS `django_local`;

USE `django_local`;

DROP TABLE IF EXISTS `national_pokedex`;

CREATE TABLE
    `national_pokedex` (
        `id` SMALLINT AUTO_INCREMENT NOT NULL COMMENT 'ID',
        `name` VARCHAR(12) NOT NULL COMMENT 'Name of Pokémon',
        `created_by` VARCHAR(30) DEFAULT NULL COMMENT 'New Creator',
        `created_at` datetime DEFAULT NULL COMMENT 'Newly created date and time',
        `updated_by` VARCHAR(30) DEFAULT NULL COMMENT 'Last updater',
        `updated_at` datetime DEFAULT NULL COMMENT 'Last updated date and time',
        `is_deleted` tinyint (1) NOT NULL DEFAULT '0' COMMENT 'Delete flag',
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='National Pokédex';

LOCK TABLES `national_pokedex` WRITE;

INSERT INTO
    `national_pokedex`
VALUES
    (
        1,
        'フシギダネ',
        'オーキド博士',
        '1996-02-27',
        'オーキド博士',
        '1996-02-27',
        0
    ),
    (
        2,
        'フシギソウ',
        'オーキド博士',
        '1996-02-27',
        'オーキド博士',
        '1996-02-27',
        0
    ),
    (
        3,
        'フシギバナ',
        'オーキド博士',
        '1996-02-27',
        'オーキド博士',
        '1996-02-27',
        0
    ),
    (
        4,
        'ヒトカゲ',
        'オーキド博士',
        '1996-02-27',
        'オーキド博士',
        '1996-02-27',
        0
    ),
    (
        5,
        'リザード',
        'オーキド博士',
        '1996-02-27',
        'オーキド博士',
        '1996-02-27',
        0
    ),
    (
        6,
        'リザードン',
        'オーキド博士',
        '1996-02-27',
        'オーキド博士',
        '1996-02-27',
        0
    ),
    (
        7,
        'ゼニガメ',
        'オーキド博士',
        '1996-02-27',
        'オーキド博士',
        '1996-02-27',
        0
    ),
    (
        8,
        'カメール',
        'オーキド博士',
        '1996-02-27',
        'オーキド博士',
        '1996-02-27',
        0
    ),
    (
        9,
        'カメックス',
        'オーキド博士',
        '1996-02-27',
        'オーキド博士',
        '1996-02-27',
        0
    );

UNLOCK TABLES;
