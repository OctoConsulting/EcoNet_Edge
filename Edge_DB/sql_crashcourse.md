# a lil crashcourse on sql :)

If you're like me, then you learned SQL for a class freshman year of college, then proceeded to forget everything about SQL.

Let's jog our memory a bit :)

Build and start the PostgreSQL container with

```Powershell
# needs Docker installed :)
powershell.exe .\on_windows.ps1
```

Create a database
```SQL
/* commands should be uppercase, while names should be lowercase */
-- also comments are nice :)
CREATE DATABASE test_db
```

Create a table: (info about [data types](https://www.postgresql.org/docs/current/datatype.html))
```SQL
CREATE TABLE test_table (
    id serial primary key,
    cost money,
    process_time time
);
```

Making 
for later...

https://towardsdatascience.com/sending-data-from-a-flask-app-to-postgresql-database-889304964bf2