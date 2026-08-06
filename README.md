# Medicine Reminder and Tracking System

A Python-based console application that simulates the interaction between a doctor and a patient. The system allows a doctor to create a medication schedule, enables a patient to record taken medicines, and provides medication reminders.

This project was developed to demonstrate fundamental Object-Oriented Programming concepts in Python.

## Features

* Create a medication program for a patient
* Track whether medicines have been taken
* Set medication reminders
* Display reminder notifications
* Validate medicines using decorators
* Display doctor and patient information
* Track patient medication status

## Object-Oriented Programming Concepts

The project demonstrates:

* Classes and objects
* Inheritance
* Encapsulation
* Polymorphism
* Method overriding
* Decorators
* Static methods
* The `super()` function

## Project Structure

```text
Medicine-Reminder-and-Tracking-System/
├── FINAL_PROJECT.txt
├── .gitignore
├── .gitattributes
└── README.md
```

## Main Classes

### Person

The base class that contains the common `name` attribute for doctors and patients.

### Doctor

The doctor can:

* Create a medication program for a patient
* Monitor the patient's medication status
* Display specialization information

### Patient

The patient can:

* View their medication program
* Mark medicines as taken
* Set medication reminders
* Receive reminder messages

## Example Medication Program

The example application creates a program containing:

```python
medicines = [
    "Betahistine",
    "Fluoxetine",
    "Cinnarizine"
]
```

The patient can take medicines, while the doctor can check which medicines have been taken.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/ezgerdog/Medicine-Reminder-and-Tracking-System.git
```

2. Open the project folder:

```bash
cd Medicine-Reminder-and-Tracking-System
```

3. Rename `FINAL_PROJECT.txt` to `FINAL_PROJECT.py`, or run it as a Python file after changing its extension.

4. Run the application:

```bash
python FINAL_PROJECT.py
```

## Technologies

* Python
* Python Standard Library
* Object-Oriented Programming

## Possible Future Improvements

* Add separate medication times for each medicine
* Store patient data in a database
* Create a graphical user interface
* Add multiple doctors and patients
* Send real-time desktop or mobile notifications
* Add user authentication
* Create medication history reports

## Author

Developed by [Ezgi Erdoğan](https://github.com/ezgerdog)
