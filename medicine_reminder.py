import time
from datetime import datetime, timedelta

# Decorator to log method calls (removed print for "Calling method:")
def log_method_call(func):
    def wrapper(*args, **kwargs):    # This is the wrapper function that surrounds the original function.
        result = func(*args, **kwargs)   
        return result
    return wrapper  # This effectively replaces the original function.

# Decorator to check if the medicine exists in the patient's program
def check_medicine_in_program(func):
    def wrapper(self, medicine, *args, **kwargs):
        if medicine not in self.medicine_program:  # Check if the medicine is in the patient's medicine program.
            print(f"{medicine} is not in {self.name}'s medicine program.")  # if medicine is not found.
            return  
        return func(self, medicine, *args, **kwargs)  # If the medicine exists in the program, execute the original function.
    return wrapper

# Decorator to ensure reminder is set only if the patient has a medicine program
def check_medicine_program(func):
    def wrapper(self, *args, **kwargs):
        if not self.medicine_program:
            # If the patient does not have a medicine program, print a message and stop execution.
            print(f"{self.name} has no medicine program set. Please create one first.")
            return       
        return func(self, *args, **kwargs)
    return wrapper  # Return the wrapper function to replace the original method.

class Person:  # The Person class stores attributes common to both doctors and patients.
    def __init__(self, name):
        self.name = name  # Person's name

    def __str__(self):  # The __str__ method is used here to return the name of a Person object as text.
        return f"{self.name}"

# Doctor class inherits from Person class.
class Doctor(Person):  # Represents the doctor who determines the patient's medicine program and the specialty of that doctor.
    def __init__(self, name, specialization):
        super().__init__(name)  # Calling the parent class constructor with super().
        self.specialization = specialization
        self.medicine_program = []

    @log_method_call  # Using the log decorator for method calls
    def create_medicine_program(self, patient, medicines):  # Creating a dictionary for the patient's medicine program
        patient.set_medicine_program(medicines)
        print(f"The medicine program for the patient {patient.name} prepared by Doctor {self.name}.\n")

    @log_method_call
    def track_patient(self, patient):
        print(f"\nTracking medicines for patient {patient.name}:")
        for medicine, taken in patient.medicine_program.items():
            print(f"{medicine}: {'Taken' if taken else 'Not Taken'}")

    @staticmethod
    def print_specialization_info():  # Static method example: the method does not require access to any instance or class property. It only prints information about the doctor.
        print("\nThis doctor is a specialist in audiology.")

    # Overriding __str__ method to print 'Doctor: Dr. <name>'
    def __str__(self):
        return f"\nDoctor: Dr. {self.name}"

# Patient class inherits from Person class.
class Patient(Person):  # Patient overrides the methods of the Person class. Polymorphism therefore occurs here.
    def __init__(self, name):  # Define the patient's attributes.
        super().__init__(name)  # Calling the parent class constructor with super().
        self.medicine_program = {}  # Dictionary to track medicines and their status.
        self.reminder_time = None  # Placeholder for reminder time.

    def set_medicine_program(self, medicines):
        # Creating a dictionary to store medicines with 'False' as the initial value (not taken).
        self.medicine_program = {medicine: False for medicine in medicines}

    @check_medicine_in_program  # Using the decorator to ensure the medicine is in the program before marking it as taken.
    @log_method_call  # Using the log decorator for method calls.
    def take_medicine(self, medicine):  # Marks a medicine as taken. 
        if medicine in self.medicine_program:
            self.medicine_program[medicine] = True
            print(f"{self.name} has taken {medicine}.")
        else:
            print(f"{medicine} is not in {self.name}'s medicine program.")

    @check_medicine_program  # Using the decorator to ensure the reminder can only be set if the patient has a medicine program.
    def get_reminder(self):  # Sends a reminder to the patient to take their medicine. 
        if not self.reminder_time:
            print(f"\n{self.name} does not have a reminder set.")
            return

        reminder_hour = self.reminder_time.strftime("%H:%M")
        if self.reminder_time > datetime.now():
            print(f"\nReminder: {self.name}, it's {reminder_hour} time to take your medicine!")
        else:
            print(f"Reminder: {self.name}, it was {reminder_hour}, you should have taken your medicine by now.")

    @log_method_call  # Using the log decorator for method calls
    def set_reminder(self, minutes_from_now):  # Sets a reminder for the patient.
        self.reminder_time = datetime.now() + timedelta(minutes=minutes_from_now)
        reminder_hour = self.reminder_time.strftime("%H:%M")
        print(f"\nReminder for {self.name} set for {reminder_hour}.")
        
    # Overriding __str__ method to print 'Patient: <name>'
    def __str__(self):
        return f"Patient: {self.name}"

# Function to print both Doctor and Patient details.
def print_person_info(person):
    print(person)  # Prints the correct __str__ based on whether it's a Doctor or Patient object.

# Creating Doctor and Patient objects.
doctor = Doctor("Ezgi", "Audiologist")
patient = Patient("Hilal Bizimyer")

# Doctor creates a medicine program for the patient with new medicine names.
medicines = ["Betahistine", "Fluoxetine", "Cinnarizine"]
doctor.create_medicine_program(patient, medicines)

# Patient takes some medicines.
patient.take_medicine("Betahistine")
patient.take_medicine("Fluoxetine")

# Doctor tracks the patient's medicine status.
doctor.track_patient(patient)

# Patient sets a reminder for taking medicine.
patient.set_reminder(5)  # Reminder in 5 minutes.

# Simulating time passage.
time.sleep(6)  # Wait for 6 seconds.
patient.get_reminder()

# Print both doctor and patient info.
print_person_info(doctor)  # This will now print 'Doctor: Dr. Ezgi'
print_person_info(patient)  # This will print the name of the patient as before.

# Using the Static and Class Methods.
doctor.print_specialization_info()  # Static method usage.

