from homework03 import Human, Student, Group, MaxStudentsExceededError 

def main():
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

    gr = Group('PD1')
    gr.add_student(st1)
    gr.add_student(st2)

    print(gr)

    # Тести
    assert str(gr.find_student('Jobs')) == str(st1), 'Test1: Студент Jobs не знайдений!'
    assert gr.find_student('Jobs2') is None, 'Test2: Студент Jobs2 не повинен існувати!'
    assert isinstance(gr.find_student('Jobs'), Student), 'Test3: Метод пошуку має повертати екземпляр Student!'

    st3 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    assert st1 == st3, 'Test4: Студенти мають бути однаковими!'
    assert st1 != st2, 'Test5: Студенти мають бути різними!'

    gr.delete_student('Taylor')
    print(gr)

    gr.delete_student('Taylor')

    try:
        for i in range(10, 12):
            st_new = Student('Female' if i % 2 == 0 else 'Male', 20 + i, f'FirstName{i}', f'LastName{i}', f'AN1{i}')
            gr.add_student(st_new)
    except MaxStudentsExceededError as e:
        print(e)

if __name__ == "__main__":
    main()