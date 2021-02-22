# Attendance Checking System

A self-developed program to check the attendance for large class designed for TAs.

## Working Flow
+ Generate random strings as password by program and give them to students on sites
+ Collect the passwords together with students' id in someways
+ Check the attendance by validate the password collected

## Way to Run Program

### Code generation
+ `python ./codesGen.py Number Name`
+  Number: the number of labels generates, integer, default 30
+  Name: the filename of pdf and txt file, default random 8-bit decimal

## Dependency Libraries
+ pylabels
+ reportlab

## Some Notes
+ In our current program, we assume the random strings generated is distinct. The assumption holds as the probobility of generating two identical strings is negligible.
