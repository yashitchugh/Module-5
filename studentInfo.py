def main():

    students = {
        'Yashit': 85,
        'Parth': 92,
        'Yash': 78,
        'Rahul': 90
    }


    name = input("Enter the student's name: ")


    if name in students:
        print(f"{name}'s marks: {students[name]}")
    else:
        print(f"Student '{name}' not found in the records.")

main()
