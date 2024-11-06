import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    salaries_per_department = defaultdict(list)

    for name, salary, departmentId in zip(employee["name"], employee["salary"], employee["departmentId"]):
        salaries_per_department[departmentId].append((name, salary))

    department_names = {row["id"]: row["name"] for _, row in department.iterrows()}

    departments = []
    employees = []
    salaries = []

    for dept_id, emp_salaries in salaries_per_department.items():
        emp_salaries.sort(key=lambda x: x[1], reverse=True)
        curr_department = department_names[dept_id]

        unique_salaries = set()

        for name, salary in emp_salaries:
            if len(unique_salaries) < 3 or salary == min(unique_salaries):
                departments.append(curr_department)
                employees.append(name)
                salaries.append(salary)

                unique_salaries.add(salary)

            if len(unique_salaries) == 3 and salary != min(unique_salaries):
                break

    return pd.DataFrame({"Department": departments, "Employee": employees, "Salary": salaries})
