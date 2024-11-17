// Класс расширенной даты
class ExtendedDate extends Date {
    // Метод для вывода даты текстом
    getTextDate() {
        const months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"];
        return `${this.getDate()} ${months[this.getMonth()]}`;
    }

    // Метод для проверки, прошедшая дата или нет
    isFutureDate() {
        return this >= new Date();
    }

    // Метод для проверки, является ли год високосным
    isLeapYear() {
        const year = this.getFullYear();
        return (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0;
    }

    // Метод для получения следующей даты
    getNextDate() {
        const nextDay = new Date(this);
        nextDay.setDate(this.getDate() + 1);
        return nextDay;
    }
}

// Пример использования
const date = new ExtendedDate();
console.log(date.getTextDate());
console.log(date.isFutureDate());
console.log(date.isLeapYear());
console.log(date.getNextDate());
