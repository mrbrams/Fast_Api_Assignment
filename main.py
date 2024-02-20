from fastapi import FastAPI
from uuid import UUID


app = FastAPI()

# Create a FASTAPI project with the following specifications:
# A student resource. Each student will have:
# - id: int
# - name: str
# - age: int
# - sex: str
# - height: float

# Create a dict to store the student resource in memory.
students = {}

# Create a dictionary to store the student data.
student_data = {"id": 0, "name": "", "age": 0, "sex": "", "height": 0.0}


@app.get("/")
def home():
    return {"message": "Hello from the students API"}


# Get all students.
@app.get("/students")  # GET method to get a resource
def get_students():
    return students


# Get a single student using a path parameter
# The value of the path parameter item_id will be passed to your function as the argument item_id
@app.get("/students/{id}")  # GET method to get a resource
def get_student_by_id(id: str):
    student = students.get(id)
    if not student:
        return {"error": "Student not found"}

    return student


# Add a student.
@app.post("/students")  # POST method to create a new resource
def add_student(
    name: str, age: int, sex: str, height: float
):  # query parameters
    new_student = student_data.copy()
    new_student["id"] = str(UUID(int=len(students) + 1))
    new_student["name"] = name
    new_student["age"] = age
    new_student["sex"] = sex
    new_student["height"] = height

    students[new_student["id"]] = new_student

    return {"message": "Student added successfully", "data": new_student}


# Update a student.
@app.put("/students/{id}")  # PUT method to update a resource
def update_student(
    id: str, name: str, age: int, sex: str, height: float
):  # A combination of path and query parameters
    student = students.get(id)
    if not student:
        return {"error": "Student not found"}

    student["name"] = name
    student["age"] = age
    student["sex"] = sex
    student["height"] = height

    return {"message": "Student updated successfully", "data": student}


# Delete a student.
@app.delete("/students/{id}")  # DELETE method to delete a resource
def delete_student(id: str):
    student = student.get(id)
    if not student:
        return {"error": "Student not found"}

    del students[id]

    return {"message": "Student deleted successfully"}
