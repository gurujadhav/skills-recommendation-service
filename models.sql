CREATE DATABASE skillsdb;

USE skillsdb;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    learning_path Varchar(100),
    skills TEXT
);

CREATE TABLE resources (
    id INT AUTO_INCREMENT PRIMARY KEY,
    skill VARCHAR(100),
    link VARCHAR(255)
);


INSERT INTO resources (skill, link) VALUES
("Python", "https://docs.python.org/3/"),
("Flask", "https://flask.palletsprojects.com/"),
("Java", "https://docs.oracle.com/javase/"),
("Spring Boot", "https://spring.io/projects/spring-boot");


SELECT * FROM resourcesusers
