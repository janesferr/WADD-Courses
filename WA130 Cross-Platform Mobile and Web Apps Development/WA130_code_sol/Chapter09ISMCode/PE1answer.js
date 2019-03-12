// See section 9.3 - Modeling a NoSQL database
db.library.insert({ author: "Pawan" });
db.library.update({ author: "Pawan" },
                  { author: "Pawan",
                    books:
                      [
                        { title: "Web mining", year: 2007 },
                        { title: "Web programming", year: 2012 }
                      ]
                  });
db.library.update({ author: "Pawan" },
                  { 
                    $push: { 
                      books: { title: "Mobile app development", year: 2015 }
                    }
                  });
db.library.insert({
  author : "Walter",
  books :
  [
    { title : "Intro programming", year : 2000 },
    { title : "Data structures", year : 2002 }
  ]
});