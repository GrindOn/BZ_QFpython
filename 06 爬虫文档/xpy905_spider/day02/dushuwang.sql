CREATE TABLE dushuwang
(
  id      VARCHAR(32) PRIMARY KEY,
  name    VARCHAR(100) UNIQUE,
  author  VARCHAR(100),
  content TEXT,
  tags    VARCHAR(100)
);