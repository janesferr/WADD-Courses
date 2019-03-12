-- All the books published before 2000 (by any author)
DELETE FROM library WHERE year < 2000;

-- All the books published by John Grisham
DELETE FROM library WHERE author = "John Grisham";

-- All the books not published by John Grisham
DELETE FROM library WHERE author != "John Grisham";

-- All the books published between years 2000 and 2009 (by any author)
DELETE FROM library WHERE year >= 2000 AND year <= 2009;