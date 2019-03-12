-- Based on library example in section 9.3

CREATE DATABASE IF NOT EXISTS mobileappbook;
USE mobileappbook;

CREATE TABLE library (
    author VARCHAR(25) NOT NULL,
    title VARCHAR(25) NOT NULL,
    year INTEGER NOT NULL
);

INSERT INTO library (author, title, year)
VALUES
  ("Pawan", "Web Mining", 2007),
  ("Pawan", "Web Programming", 2012),
  ("Pawan", "Mobile app development", 2015);

INSERT INTO library (author, title, year)
VALUES
  ("Walter", "Intro programming", 2000),
  ("Walter", "Data structures", 2002);