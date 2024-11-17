// Класс простого маркера
class Marker {
    constructor(color, inkLevel) {
        this.color = color; // Цвет маркера
        this.inkLevel = inkLevel; // Количество чернил (в процентах)
    }

    // Метод для печати строки
    print(text) {
        let printedText = '';
        for (let char of text) {
            if (this.inkLevel <= 0) break; // Останавливаем печать, если закончились чернила
            printedText += char;
            if (char !== ' ') this.inkLevel -= 0.5; // Уменьшаем количество чернил на 0,5% за каждый непустой символ
        }
        console.log(`%c${printedText}`, `color: ${this.color}`);
    }
}

// Класс заправляемого маркера, наследуется от Marker
class RefillableMarker extends Marker {
    refill(inkAmount) {
        this.inkLevel = Math.min(this.inkLevel + inkAmount, 100); // Добавляем чернила, не превышая 100%
    }
}

// Пример использования
const marker = new Marker("blue", 10);
marker.print("Здравствуйте, это тестовое сообщение..");

const refillableMarker = new RefillableMarker("red", 5);
refillableMarker.print("Тестирование заправляемого маркера.");
refillableMarker.refill(50);
refillableMarker.print("Это после заправки.");
