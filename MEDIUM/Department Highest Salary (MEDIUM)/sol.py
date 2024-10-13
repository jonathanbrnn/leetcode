import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    dic = defaultdict(list)

    for name, sal, dpid in zip(employee["name"], employee["salary"], employee["departmentId"]):
        sal = int(sal)

        if dpid not in dic:
            dic[dpid] = [(int(sal), str(name))]
        elif sal > dic[dpid][0][0]:
            dic[dpid] = [(int(sal), str(name))]
        elif sal == dic[dpid][0][0]:
            dic[dpid].append((int(sal), str(name)))

    salaries = []
    departments = []
    employee = []
    for item, val in dic.items():
        for ind in val:
            departments.append(department.loc[department['id'] == item, 'name'].values[0])
            employee.append(ind[1])
            salaries.append(ind[0])

    return pd.DataFrame({"Department": departments, "Employee": employee, "Salary": salaries})
