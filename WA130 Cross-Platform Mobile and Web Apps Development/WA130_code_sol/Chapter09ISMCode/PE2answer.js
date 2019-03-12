var mongodb = require('mongodb');

var host = '127.0.0.1';
var port = '27017'; // Default MongoDB port
var database = 'mobileappbook';
// var user = 'username';
// var password = 'password';
// var connectionString = 'mongodb://' + user + ':' + password + '@' + host + ':' + port + '/' + database;
var connectionString = 'mongodb://' + host + ':' + port + '/' + database;

var johnGrisham = {
  author: "John Grisham",
  books: [
    { title: "A Time to Kill", year: 1989 },
    { title: "The Firm", year: 1991 },
    { title: "The Pelican Brief", year: 1992 },
    { title: "The Client", year: 1993 },
    { title: "The Chamber", year: 1994 },
    { title: "The Rainmaker", year: 1995 },
    { title: "The Runaway Jury", year: 1996 },
    { title: "The Partner", year: 1997 },
    { title: "The Street Lawyer", year: 1998 },
    { title: "The Testament", year: 1999 },
    { title: "The Brethren", year: 2000 },
    { title: "A Painted House", year: 2001 },
    { title: "Skipping Christmas", year: 2001 },
    { title: "The Summons", year: 2002 },
    { title: "The King of Torts", year: 2003 },
    { title: "Bleachers†", year: 2003 },
    { title: "The Last Juror", year: 2004 },
    { title: "The Broker", year: 2005 },
    { title: "Playing for Pizza", year: 2007 },
    { title: "The Appeal", year: 2008 },
    { title: "The Associate", year: 2009 },
    { title: "The Confession", year: 2010 },
    { title: "The Litigators", year: 2011 },
    { title: "Calico Joe", year: 2012 },
    { title: "The Racketeer", year: 2012 },
    { title: "Sycamore Row", year: 2013 },
    { title: "Gray Mountain", year: 2014 }
  ]
};

mongodb.connect(connectionString, function (error, db) {
  if (error) {
    throw error;
  }

  var libraryCollection = db.collection('library');
  libraryCollection.insert(johnGrisham, function(err, result) {
    if (err) {
      console.log(err);
    } else {
      console.log(result);
      console.log("Successfully inserted John Grisham");
    }
    process.exit();
  });
});
