import numpy as np
import matplotlib.pyplot as plt

class EmployeeManagementSystem:
    def __init__(self):
        self.codes = np.array([])
        self.names = np.array([])
        self.salary = np.array([])
        self.desigs = np.array([])
        self.addresses = np.array([])
        self.performances = np.array([])
        self.attendances = np.array([])

    def add_employee(self, code, name, salary, designation, address):
        self.codes = np.append(self.codes, code)
        self.names = np.append(self.names, name)
        self.salary = np.append(self.salary, salary)
        self.desigs = np.append(self.desigs, designation)
        self.addresses = np.append(self.addresses, address)
        self.performances = np.append(self.performances, 0)  # Default performance
        self.attendances = np.append(self.attendances, 0)  # Default attendance

    def update_salary(self, code, new_salary):
        index = np.where(self.codes == code)[0]
        if index.size > 0:
            self.salary[index[0]] = new_salary
        else:
            print("Employee code not found.")

   
    def update_desig(self, code, new_designation):
        index = np.where(self.codes == code)[0]
        if index.size > 0:
            self.designations[index[0]] = new_designation
        else:
            print("Employee code not found.")

    def update_address(self, code, new_address):
        index = np.where(self.codes == code)[0]
        if index.size > 0:
            self.addresses[index[0]] = new_address
        else:
            print("Employee code not found.")

    def update_performance(self, code, new_performance):
        index = np.where(self.codes == code)[0]
        if index.size > 0:
            self.performances[index[0]] = new_performance
        else:
            print("Employee code not found.")

    def record_attendance(self, code, attendance):
        index = np.where(self.codes == code)[0]
        if index.size > 0:
            self.attendances[index[0]] += attendance
        else:
            print("Employee code not found.")

    def calculate_stats(self):
        average_salary = np.mean(self.salary)
        max_salary = np.max(self.salary)
        min_salary = np.min(self.salary)

        highest_paying_index = np.argmax(self.salary)
        lowest_paying_index = np.argmin(self.salary)

        print(f"Average Salary: {average_salary:.2f}")
        print(f"Max Salary: {max_salary:.2f} ({self.names[highest_paying_index]})")
        print(f"Min Salary: {min_salary:.2f} ({self.names[lowest_paying_index]})")

    def plot_performance(self):
        plt.scatter(self.codes, self.performances, color='blue')
        plt.title("Employee Performance")
        plt.xlabel("Employee Codes")
        plt.ylabel("Performance")
        plt.xticks(rotation=45)
        plt.grid()
        plt.show()


if __name__ == "__main__":
    ems = EmployeeManagementSystem()
    ems.add_employee(101, "Aditi", 70000, "Manager", "134 Manu App Delhi")
    ems.add_employee(102, "Ayush", 50000, "Developer", "Forest Apt Indirapuram")
    ems.add_employee(103, "Sneha", 30000, "Intern", "Kedar Shah Mohalla Indore")
    ems.add_employee(104, "Yash", 20000, "Intern", "Kedar Shah Mohalla Indore")
    ems.add_employee(105, "Harsh", 15000, "Intern", "Kedar Shah Mohalla Indore")

    ems.update_salary(102, 55000)
    ems.update_performance(101, 85)   
    ems.update_performance(102, 90)
    ems.update_performance(103, 75)
   
    ems.record_attendance(101, 20)
    ems.record_attendance(102, 22)
    ems.record_attendance(103, 18)

   
    ems.calculate_stats()

  
    ems.plot_performance()
