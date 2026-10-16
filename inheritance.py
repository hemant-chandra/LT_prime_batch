class Employee :
    start_time = "10AM"
    end_time = "5PM"

class Teachers(Employee) :
    def __init__(self, subject) :
        self.subject = subject

t1 = Teachers("Maths")

print(t1.subject, t1.start_time, t1.end_time)