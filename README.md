# Test task for JetBrains

The description of the test task is below.

File description: 
* part1.1 -> searches for the necessary files and creates a list
* part1.2 -> goes through the list and creates tokens
* part2.1 -> creates tokens for a new file to be compared
* part2.2 -> compares files and returns "ok" for matches < 85% or "file repository and number of matches"
* JetBrains -> django app, one-page service with the ability to download a file and check it in a ready-made database
* downloaded_files -> test folder with files


## General description
You need to implement a REST API web service which will be able to index several local repositories and to answer a simple question whether or not a given file with code is similar to something inside these repositories.

### Task
### Part 1: Repository indexing mechanism

Download source code of several repositories from Github, for example intellij/community or smaller.
pygmentize -f raw /path/to/file the source code using pygments. It will produce a lot of lexical tokens.
Create an inverted index based on available Token.Names.
Save it into a file or in a database.
Preferred language is Python.

### Part 2: Checking another source code file for being a clone

Extract available Token.Names from this file.
Check whether or not there is a file in indexed repositories which has at least 85% of these Token.Names.
If such a file exists, return the path of this file, including the repository name. If not - return “OK”.
No restrictions on how this part should be implemented. It can be inside part 3 and written in Java or Kotlin or it can be inside part 1 and written in Python.

### Part 3: Create a very simple REST API web service

It should use a saved index based on available repositories from a specific folder. This index can be provided separately.
It should be able to accept source code as text and check whether it is a clone or not using an algorithm from part 2.
It should be written using Kotlin or Java.
