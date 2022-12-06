# To intialise tables into repo:
* Create a table with the suitable name of the directory from the db url - `set_pg`-> `psql`-> `CREATE DATABASE [Insert directory name]`-> `\c [database name]`-> `\q`
* Open Python intepreter `python3`in terminal and import the db as `from [directory name] import db`-> `db.create_all()`-> close interpreter with `exit()`