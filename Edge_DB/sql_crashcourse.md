# A little crashcourse on using SQL

If you're like me, then you learned SQL for a class freshman year of college, then proceeded to forget everything about SQL.

Let's jog our memory a bit :)

Create a database
```SQL
/* commands should be uppercase, while names should be lowercase */
-- also comments are nice :)
CREATE DATABASE test_db
```

Create a table
```SQL
CREATE TABLE test_table (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   .....
    columnN datatype,
    PRIMARY KEY (one or more columns)
);
```