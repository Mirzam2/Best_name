# **Best_name**
**Требования к программному обеспечению**

Программа Python v 3.9.6

**Используемые внешние модули**

*Предустановленные в Python:*
- random
- math
- os
- sys
- time
- typing

*Дополнительно установленные:*
- perlin-noise
- pathlib
- pygame
- json

**Управление**

Используйте английскую раскладку клавиатуры. 
- A, D - движение влево-вправо соответственно
- W - прыжок.
- Левая кнопка мыши - удар по мобам при коротком нажатии, ломание блоков при длительном нажатии. 
- Правая кнопка мыши - постановка блоков. 
- E - открытие инвентаря. R - закрытие инвентаря. Левая кнопка мыши в окне инвентаря - выбор блока, который нужно ставить.
- 1, 2 - вкл/выкл музыку соответственно

**Объекты**

- **Подвижные объекты:**

  -  ***Главный герой***:
 Персонаж, управляемый игроком. Может ходить, прыгать, падать, ломать и ставить блоки, а так же бить и получать урон от враждебных мобов. Генерируется в центре карты. Вначале имеет 10 жизней, каждый удар моба уменьшает это число на урон моба. Если жизни закончатся показывается экран смерти.
  - ***Зобми***:
Враждебный моб, управляется псевдо-ИИ. Движется по направлению у игроку, если долго стоит на одном месте, то прыгает. Когда достигает расстояния удара бьёт по герою, при этом нанося 1 еденицу урона и отбрасывая его. У ударов есть перерыв - 100 тиков. Зомби генерируются раз в 1000 тиков, в произвольном пустом месте экрана. Начальный запас здоровья - 5. Если жизни закончатся - исчезает
- **Неподвижные объекты**:
  - ***Блоки***:
  Ячейки составляющие карту. Имеется 19 типов блоков. Каждый имеет такой набор параметров:
     - Название
     - Прочность
     - Проницаемость (возможность проходить через блок)
     - Картинка блока
     - Вероятность генерации
   
     Карта генерируеся случайным образом, но обязательно присутствие нескольких слоёв воздуха, слоя земли, а также границ мира в виде слоёв бедрока сверху, снизу, слева и справа от карты. Также в произвольных местах генерируются деревья.

**Начальный экран**

На начальном экране есть 3 кнопки:
- *New game*: при нажатии создаётся новый файл с новым пустым инвентарём, и начинается игра на этой карте.
- *Saved game*: при нажатии появляется список сохраненных карт, при нажатии на соответствующие кнопки начинается игра на выбраной сохраненной карте.
- *Exit*: при нажатии закрывается игра

**Экран смерти**

На экране смерти есть 2 кнопки:
- *Restart game*: при нажатии персонаж возраждается
- *Main meny*: при нажатии выходит на начальный экран
- *Exit*: при нажатии закрытвается игра


