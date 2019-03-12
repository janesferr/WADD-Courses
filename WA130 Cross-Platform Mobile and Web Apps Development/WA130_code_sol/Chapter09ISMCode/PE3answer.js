// Note, some of these questions require the students to refer to www.mongodb.org 
// to create the more sophisticated queries

// All the books published before 2000 (by any author)
db.library.aggregate(
  { $unwind: "$books" },
  { $match: { "books.year": { $lt: 2000 } }}
);

// All the books published by John Grisham
db.library.find({ author: "John Grisham" }, { books: 1 })

// All the books not published by John Grisham
db.library.find({ author: { $ne: "John Grisham" }}, { books: 1 })

// All the books published between years 2000 and 2009
db.library.aggregate(
  { $unwind: "$books" },
  { $match: { "books.year": { $gte: 2000, $lte: 2009 } }}
);

// The number of books published after 2009
db.library.aggregate(
  { $unwind: "$books" },
  { $match: { "books.year": { $gt: 2009 } }},
  { $group: { _id: null, count: { $sum: 1 }}}
);