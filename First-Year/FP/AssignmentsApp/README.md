# Student Lab Assignment Manager – Python Application

This repository contains a console-based Python application developed as part of the Fundamentals of Programming course at UBB. 
The application manages students, lab assignments, and grades using a layered architecture and supports in-memory, text file, and binary file storage.

## 📚 Project Description
The Student Lab Assignment Manager is a menu-driven program that allows users to:
- Manage students and lab assignments (CRUD operations)
- Assign work to individuals or student groups
- Grade students and track their performance
- Generate useful statistics about assignments and grades
- This application follows clean coding principles and object-oriented design. It includes automatic data generation, flexible configuration, and full support for unit testing and custom exceptions.

## ✅ Features
Layered Architecture: Clear separation between UI, service, and data access layers using classes.
Console User Interface: Easy-to-navigate, menu-driven interface.
Entity Management: Add, remove, update, and list students and assignments.
Group Assignment: Assign tasks to individual students or entire groups intelligently.
Grading System: Assign grades with immutable grading rules.
Statistics:
- Students sorted by grade for a given assignment.
- Students late with assignments (missed deadlines).
- Top-performing students based on average grades.
Data Persistence: Works with in-memory, text file, or binary file (Pickle) repositories.
Configuration File: Easily switch between repository types via a settings.properties file.
Auto Data Generation: Uses Faker to generate 20+ entries for each entity on startup.
Unit Testing: Includes PyUnit tests for all non-UI components.
Custom Exceptions: Robust error handling with custom exception classes.
