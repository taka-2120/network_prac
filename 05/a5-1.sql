.open events.db
.mode box
DROP TABLE IF EXISTS events;
CREATE TABLE events(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, date TEXT, place TEXT);
INSERT INTO events(name, date, place) VALUES('WWDC 21','2022-06-08', 'Cupertino, California, U.S.');
INSERT INTO events(name, date, place) VALUES('Tokyo Olympics 2020','2021-07-23','Tokyo, Japan');
INSERT INTO events(name, date, place) VALUES('WWDC 22','2022-06-07', 'Cupertino, California, U.S.');
INSERT INTO events(name, date, place) VALUES('iOSDC 22','2022-09-10','Tokyo, Japan');
INSERT INTO events(name, date, place) VALUES('WWDC 23','2023-06-05','Cupertino, California, U.S.');
INSERT INTO events(name, date, place) VALUES('iOSDC 2023','2023-09-01','Tokyo, Japan');
INSERT INTO events(name, date, place) VALUES('WWDC 24','2024-06-10','Cupertino, California, U.S.');
INSERT INTO events(name, date, place) VALUES('iOSDC 2024','2024-08-22','Tokyo, Japan');
INSERT INTO events(name, date, place) VALUES('Expo 2025','2025-04-13','Osaka, Japan');
INSERT INTO events(name, date, place) VALUES('Paris Olympics 2020','2024-07-26','Paris, France');
SELECT * FROM events;
SELECT * FROM events WHERE name LIKE '%WWDC%';
SELECT * FROM events WHERE date > CURRENT_DATE;
SELECT * FROM events WHERE date < CURRENT_DATE AND name LIKE '%WWDC%';