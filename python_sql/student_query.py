from sql_students import session, UserHomework


def query_all_students():
    return session.query(UserHomework).all()


def query_student_by_name(name):
    return session.query(UserHomework).filter(UserHomework.student_name == name).all()


def query_students_by_homework_count(homework_count):
    return session.query(UserHomework).filter(UserHomework.homework_account == homework_count).all()


def query_students_by_age(age):
    return session.query(UserHomework).filter(UserHomework.age == age).all()


def query_latest_updates():
    return session.query(UserHomework).order_by(UserHomework.last_update_time.desc()).limit(1).all()


def main():
    while True:
        print("\nSelect an option:")
        print("1: Query all students' information")
        print("2: Query a student by name")
        print("3: Query students by homework count")
        print("4: Query students by age")
        print("5: Query the latest updated student information")
        print("0: Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            students = query_all_students()
            for student in students:
                print(student)
        elif choice == "2":
            name = input("Enter the student's name: ")
            students = query_student_by_name(name)
            for student in students:
                print(student)
        elif choice == "3":
            homework_count = int(input("Enter the minimum homework count: "))
            students = query_students_by_homework_count(homework_count)
            for student in students:
                print(student)
        elif choice == "4":
            age = int(input("Enter the student's age: "))
            students = query_students_by_age(age)
            for student in students:
                print(student)
        elif choice == "5":
            student = query_latest_updates()
            print(student)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()