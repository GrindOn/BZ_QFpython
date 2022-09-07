CREATE TABLE t_book(
  book_id VARCHAR(32) PRIMARY KEY ,
  book_name VARCHAR(100),
  book_cover VARCHAR(200),
  book_url VARCHAR(50),
  tags VARCHAR(50),
  author VARCHAR(50),
  summary TEXT
);

CREATE TABLE t_seg(
  seg_id VARCHAR(32) PRIMARY KEY ,
  book_id VARCHAR(32),
  url VARCHAR(100),
  title VARCHAR(200)
);

CREATE TABLE t_detail_seg(
  seg_id VARCHAR(32),
  content TEXT
);