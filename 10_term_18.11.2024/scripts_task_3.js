// Класс работника
class Employee {
    constructor(name, position, salary) {
        this.name = name;
        this.position = position;
        this.salary = salary;
    }
}

// Класс таблицы работников
class EmpTable {
    constructor(employees) {
        this.employees = employees;
    }

    // Метод для генерации HTML таблицы
    getHtml() {
        let html = "<table border='1'><tr><th>Имя</th><th>Должность</th><th>Зарплата</th></tr>";
        for (let employee of this.employees) {
            html += `<tr><td>${employee.name}</td><td>${employee.position}</td><td>${employee.salary}</td></tr>`;
        }
        html += "</table>";
        return html;
    }
}

// Пример использования
const employees = [
    new Employee("Иван Иванов", "Менеджер", 50000),
    new Employee("Петр Петров", "Разработчик", 60000),
    new Employee("Сергей Сергеев", "Аналитик", 55000)
];

const empTable = new EmpTable(employees);
document.write(empTable.getHtml());
