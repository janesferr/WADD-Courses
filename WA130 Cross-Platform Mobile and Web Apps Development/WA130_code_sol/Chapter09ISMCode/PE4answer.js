// Note, some of these questions require the students to refer to www.mongodb.org 
// to create the more sophisticated queries

// All the books published before 2000 (by any author)
db.library.update(
  {},
  { $pull: { books: { year: { $lt: 2000 }}}},
  { multi: true }
);

// All the books published by John Grisham
db.library.update(
  { author: "John Grisham" },
  { author: "John Grisham", books: [] }
);

// All the books not published by John Grisham
db.library.update(
  { author: { $ne: "John Grisham" }},
  { $set: { books: [] }},
  { multi: true }
);

// All the books published between years 2000 and 2009 (by any author)
db.library.update(
  {},
  { $pull: { books: { year: { $gte: 2000, $lte: 2009 }}}},
  { multi: true }
);