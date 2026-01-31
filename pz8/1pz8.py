 #Измените имя на "Jessa" во вложенном словаре
nested_student_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

nested_student_dict["class"]["student"]["name"] = "Jessa"

print(nested_student_dict)


