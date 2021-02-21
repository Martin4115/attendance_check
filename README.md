# Attendance Checking System

A self-developed program to check the attendance for large class designed for TAs.

## Working Flow
+ Generate random strings as password by program and give them to students on sites
+ Collect the passwords together with students' id in someways
+ Check the attendance by validate the password collected

## Usage of Program
+ The method in codesGen.py could generate passwords, both in pdf and txt. pdf version is for printing and distribution, and txt data is saved for later validation

## Dependency Libraries
+ pylabels
+ reportlab

## Some Notes
+ In our current program, we assume the random strings generated is distinct. The assumption holds as the probobility of generating two identical strings is negligible.
