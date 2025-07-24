# Proper Trench Coats – C++ & Qt Shopping Application

A modern C++ application with a Qt GUI for managing and purchasing trench coats from a virtual fashion store. The app supports both **administrator** and **user** modes, with full support for undo/redo, data validation, persistent file storage, and graphical table view of the shopping basket.

> 🎓 Developed as part of my first-year Computer Science OOP course at UBB.

---

## Features

### Administrator Mode
- Add new trench coats with attributes: `size`, `colour`, `price`, `quantity`, `photo URL`
- Update existing trench coats
- Delete trench coats from inventory
- View all trench coats
- Persistent file storage (text file using `iostream`)
- Input validation & custom exceptions
- Undo/Redo functionality for add, delete, and update operations

### User Mode
- Browse trench coats by size (or all if no size given)
- View coat details and photograph via link
- Add trench coats to shopping basket
- View basket total price
- Save shopping basket to `.csv` or `.html` format
- Basket preview in a GUI Table using `QTableView` + custom `QAbstractTableModel`

---

## Architecture

- **Layered Architecture:**
  - **Domain Layer** – Entity classes (`TrenchCoat`)
  - **Repository Layer** – File & memory repository with validation
  - **Service Layer** – Business logic, undo/redo manager
  - **UI Layer** – Qt GUI + CLI

- **Design Patterns:**
  - Command pattern (for undo/redo)
  - MVC with Qt's model/view
  - Inheritance & Polymorphism (basket format, undo commands)

---

## 🧪 Testing

- Uses custom test suite for all non-UI layers
- Unit tests for repository, service, and validator layers
- ≥ 98% test coverage (excluding UI)

---

## How to Build and Run

### Requirements
- C++17 or later
- [Qt 6](https://www.qt.io/download)
- CMake or Visual Studio
- Any modern C++ compiler (MSVC, g++, clang++)

### 💻 Build Instructions

#### 🖥️ Windows (Visual Studio)
1. Open `A8-9.sln` in Visual Studio
2. Configure to use `x64 | Debug` mode
3. Press `Ctrl + Shift + B` to build the project
4. Run the application
