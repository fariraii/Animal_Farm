# 🐄 Livestock Monitoring System

A Python program that simulates and monitors animals on a farm.  
It tracks each animal’s **location**, generates **unique IDs**, allows the farmer to **add/remove animals**, and raises **alerts** if an animal remains in the same spot for too long.  
Access is password-protected and managed via a simple console menu.

---

## ✨ Features
- 📍 Track animals with random movement on a 2D grid
- 🆔 Assign unique IDs (UUID) to each new animal
- ➕➖ Add or remove animals from records
- 🔢 Display total number of animals
- ⚠️ Detect animals stuck in the same position
- 🔑 Password protection with option to change password
- 🗂️ Data persisted in text files (`AnimalsOnFarm.txt`, `Locations.txt`, `Password.txt`)

---

## 🛠️ Tech stack
- **Language:** Python 3.x  
- **Libraries:** 
  - `random` → random movement & selection  
  - `uuid` → generate unique IDs  
  - `schedule` & `time` → simulate repeated location checks  
  - `os` → file handling

---

## 📂 Project structure
├── PythonProjectAssignment.py # main simulation with classes & menu
├── Python program assignment.py # alternate version of the program
├── AnimalsOnFarm.txt # file where animal records are stored
├── Locations.txt # file tracking animal positions
├── Password.txt # stores user password
├── Python project proposal.docx # initial project proposal
└── Python Project.docx # structured English design
---

## 🚀 Getting started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/livestock-monitoring-system.git
cd livestock-monitoring-system
2. Run the program
3. Default login
Default password: FaRm

You will be prompted to change it on first run.

📖 Usage
From the main menu:
0 - Exit
1 - Change password
2 - Add an animal to the record
3 - Remove an animal from the record
4 - Display the total number of animals
5 - Display animal locations (auto-refresh)
6 - Select a random animal
