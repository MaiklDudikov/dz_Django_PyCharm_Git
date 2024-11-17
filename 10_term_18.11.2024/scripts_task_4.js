// Класс стилизованной таблицы работников
class StyledEmpTable extends EmpTable {
    // Метод для получения стилей таблицы
    getStyles() {
        return `
            <style>
                table { border-collapse: collapse; width: 50%; }
                th, td { padding: 8px; text-align: left; border: 1px solid #ddd; }
                th { background-color: #f2f2f2; }
                tr:nth-child(even) { background-color: #f9f9f9; }
            </style>
        `;
    }

    // Метод для генерации HTML с включением стилей
    getHtml() {
        return this.getStyles() + super.getHtml();
    }
}

// Пример использования
const styledTable = new StyledEmpTable(employees);
document.write(styledTable.getHtml());
