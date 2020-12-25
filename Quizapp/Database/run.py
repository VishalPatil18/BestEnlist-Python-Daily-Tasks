import sqlite3 as db

con = db.connect("Tiango.sqlite")
cur = con.cursor()

# Questions for all topics
cur.executescript('''
INSERT INTO Cplusplus VALUES("Static variable declared in a class are also called_________ .", "instance variable", "named constant", "global variable", "class variable", "class variable"); 
INSERT INTO Cplusplus VALUES("Which of the following operator is used to release the dynamically allocated memory in CPP?", "remove", "free", "delete", "Both b and c", "delete"); 
INSERT INTO Cplusplus VALUES("Which of the following is not a false statement about new operator?", "It can’t be overloaded.", "It returns garbage value when memory allocation fails.", "It automatically computes the size of the data object.", "All of these", "It automatically computes the size of the data object."); 
INSERT INTO Cplusplus VALUES("Run time polymorphism can be achieved with______ .", "Virtual Base class", "Container class", "Virtual function", "Both a and c", "Virtual function");
INSERT INTO Cplusplus VALUES("Attempting to throw an exception that is not supported by a function call results in calling _____________ library function.", "indeterminate()", "unutilized()", "unexpected()", "unpredicted()", "unexpected()");
INSERT INTO Cplusplus VALUES("Which of the following is not a file opening mode ____ .", "ios::ate", "ios::nocreate", "ios::noreplace", "ios::truncate", "ios::truncate");
INSERT INTO Cplusplus VALUES("If the derived class is struct, then default visibility mode is _______ .", "public", "protected", "private", "struct can’t inherit class", "public");
INSERT INTO Cplusplus VALUES("An operator function is created using _____________ keyword.", "iterator", "allocator", "constructor", "operator", "operator");
INSERT INTO Cplusplus VALUES("Logical expressions produce ____________ type results.", "explicit", "garbage", "bool", "static", "bool");
INSERT INTO Cplusplus VALUES("Return type of uncaught_exception() is ________________ .", "int", "bool", "char*", "double", "bool"); 

INSERT INTO Java VALUES("Which variables are created when an object is created with the use of the keyword 'new' and destroyed when the object is destroyed?", "Local variables", "Instance variables", "Class Variables", "Static variables", "Class Variables");
INSERT INTO Java VALUES("What can be accessed or inherited without actual copy of code to each program?", "Browser", "Applet", "Package", "None of the above", "Package"); 
INSERT INTO Java VALUES("Which cookie it is valid for single session only and it is removed each time when the user closes the browser?", "Persistent cookie", "Non-persistent cookie", "All the above", "None of the above", "Non-persistent cookie"); 
INSERT INTO Java VALUES("What invokes immediately after the start() method and also any time the applet needs to repaint itself in the browser?", "stop()", "init()", "paint()", "destroy()", "paint()");
INSERT INTO Java VALUES("Which is a perfect example of runtime polymorphism?", "Method overloading", "Method overriding", "Constructor overloading", "None of the above", "Method overriding");
INSERT INTO Java VALUES("Which specification provides runtime environment in which java byte code can be executed?", "JDK", "JVM", "JRE", "None of the above", "JVM");
INSERT INTO Java VALUES("In which the access modifier means that the field can be accessed by all classes in your application?", "private", "Public", "Package", "Protected", "Public");
INSERT INTO Java VALUES("Which is a non-static method having the same name as its class?", "Field", "Method", "Constructor", "None of the above", "Constructor");
INSERT INTO Java VALUES("Hibernate is an?", "Open Source", "Lightweight", "ORM", "All mentioned above", "All mentioned above");
INSERT INTO Java VALUES("The life cycle of the thread is controlled by ?", "JVM", "JDK", "JRE", "None of the above", "JVM");

INSERT INTO Python VALUES("Which is reserved keyword in Python", "for", "catch", "switch", "let", "for"); 
INSERT INTO Python VALUES("Which of the following is not a data structure in Python", "List", "Set", "Tuple", "Array", "Array"); 
INSERT INTO Python VALUES("Suppose list1 is [1, 3, 2], What is list1 * 2 ?", "[2, 6, 4]", "[1, 3, 2, 1, 3]", "[1, 3, 2, 1, 3, 2]", "[1, 3, 2, 3, 2, 1]", "[1, 3, 2, 1, 3, 2]"); 
INSERT INTO Python VALUES("What is the output of this expression, 3*1**3?", "27", "9", "3", "1", "3"); 
INSERT INTO Python VALUES("What is the dataype of L? L = [1, 23, ‘hello’, 1].", "List", "Dict", "Array", "Tuple", "List"); 
INSERT INTO Python VALUES("What is the result of round(0.5) - round(-0.5)?", "0", "1", "2", "None of these", "0"); 
INSERT INTO Python VALUES("Which of these in not a core datatype?", "List", "Tuple", "Class", "Dict", "Class"); 
INSERT INTO Python VALUES("All keywords in Python are in", "lower case", "UPPER CASE", "Capitalized", "None of the above", "None of the above"); 
INSERT INTO Python VALUES("Which of the following statements is used to create an empty set?", "{}", "[]", "()", "set()", "set()"); 
INSERT INTO Python VALUES("Which of the following lines of code will result in an error?", "s={abs}", "s={4, ‘abc’, (1,2)}", "s={2, 2.2, 3, ‘xyz’}", "s={san}", "s={san}"); 

INSERT INTO MySQL VALUES("Which is reserved keyword in Python", "pass", "catch", "switch", "let", "pass"); 
INSERT INTO MySQL VALUES("Which of the following is not a data structure in Python", "List", "Set", "Tuple", "Array", "Array"); 
INSERT INTO MySQL VALUES("3rd question", "A", "B", "C", "D", "C"); 
INSERT INTO MySQL VALUES("4th question in Python", "A", "B", "C", "D", "D"); 

INSERT INTO JavaScript VALUES("Inside which HTML element do we put the JavaScript?", "<javascript>", "<script>", "<js>", "<scripting>", "<script>"); 
INSERT INTO JavaScript VALUES("Which built-in method calls a function for each element in the array?", "while()", "loop()", "forEach()", "None of these", "forEach()"); 
INSERT INTO JavaScript VALUES("Which of the following function of Array object represents the source code of an object?",
"toSource()", "splice()", "toString()", "unshift()", "toSource()"); 
INSERT INTO JavaScript VALUES("Which of the following is not a reserved word in JavaScript?", "interface", "throws", "short", "except", "except"); 
INSERT INTO JavaScript VALUES("Which of the following is the correct syntax to print a page using JavaScript?", "window.print();", "browser.print();", "navigator.print();", "document.print();", "window.print();"); 
INSERT INTO JavaScript VALUES("Which of the following function of Number object returns a string value version of the current number?", "toString()", "toFixed()", "toLocaleString()", "toPrecision()", "toString()"); 
INSERT INTO JavaScript VALUES("Which of the following function of String object creates a string to be displayed as bold as if it were in a <b> tag?", "anchor()", "big()", "blink()", "bold()", "bold()"); 
INSERT INTO JavaScript VALUES("Which of the following function of Array object applies a function simultaneously against two values of the array (from left-to-right) as to reduce it to a single value?", "pop()", "push()", "reduce()", "reduceRight()", "reduce()"); 
INSERT INTO JavaScript VALUES("The async attribute can be set in the following ways -", "<script async>", "<script async="async">", "<script async="">", "All of these", "All of these"); 
INSERT INTO JavaScript VALUES("Which was the first browser to support JavaScript ?", "Netscape", "Mozilla Firefox", "Google Chrome", "IE", "Netscape"); 

INSERT INTO Aptitude VALUES("Which is reserved keyword in Python", "pass", "catch", "switch", "let", "pass"); 
INSERT INTO Aptitude VALUES("Which of the following is not a data structure in Python", "List", "Set", "Tuple", "Array", "Array"); 
INSERT INTO Aptitude VALUES("3rd question", "A", "B", "C", "D", "C"); 
INSERT INTO Aptitude VALUES("4th question in Python", "A", "B", "C", "D", "D");
''')

con.commit()
cur.close()
