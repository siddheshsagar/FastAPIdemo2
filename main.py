from fastapi import FastAPI,Path
from typing import Optional
# we use pydantic module to post a request to API. We create class which refer to a pydentic model.
from pydantic import BaseModel  # for declaring & defining the post requests 

app = FastAPI() # FastAPI instance

students = {
    1: {
        'name':'siddhesh',
        'id':52,
        'age':21
    },
    2: {
        'name':'pratik',
        'id':10,
        'age':20
    },
    3: {
        'name':'sahil',
        'id':23,
        'age':27
    }
}

# get methods
@app.get("/")
def index():
    return {"data":{"name":"Siddhesh}",
                    "paths":["/about","/blog","/getByName","/getByPathParameter"]}}
  
# query parameters have been used here  
@app.get("/getByName")
def getByName(name:str):  # name:str=None OR name:Optional[str]=None -> refers to not required field
    for ids in students:
        if students[ids]['name'] == name:
            return students[ids]
    return {"data":"not found"}

# path parameters i.e. 'student_id' have been used here 
@app.get("/getByPathParameter/{student_id}")
def getByPathParameter(student_id:int):
    return students[student_id]

@app.get("/about")
def about(id,published=True, limit:Optional[int]=1):
    return f"db{id} limit is {limit} and it is {published}"



class Student(BaseModel):
    name: str
    id: int
    age: int

# post method
@app.post("/create-student/{stud_id}")
def create_student(stud_id:int, student:Student):
    if stud_id in students:
        return {"error":"student exists"}
    students[stud_id] = student
    return students[stud_id]
     
    
    
class UpdateStudnt(BaseModel):
    name: Optional[str] = None
    id: Optional[int] = None
    age: Optional[int] = None

# Update method
@app.put("/update-student/{student_id}")
def updateStudent(student_id:int, student:UpdateStudnt):
    if student_id not in students:
        return {"error":"student does not exists"}
    if student.name != None:
        students[student_id]['name'] = student.name
    if student.id != None:
        students[student_id]['id'] = student.id
    if student.age != None:
        students[student_id]['age'] = student.age
    return students[student_id]


# delete method
@app.delete("/delete-student/{student_id}")
def deleteStudent(student_id:int):
    if student_id not in students:
        return {"error":"student does not exists"}
    del students[student_id]
    return {"messsage": "student successfully deleted \]"}
