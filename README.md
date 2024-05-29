# GlowQuest

GlowQuest - это головоломка, в которой игроки поворачивают квадратные блоки с соединительными линиями на сетке, чтобы осветить все клетки. Игра начинается с подсвеченной верхней левой клетки, и целью является соединение всех клеток с ней.

## Описание игры

В GlowQuest вам представлена сетка квадратных блоков, каждый из которых содержит линии, которые можно поворачивать. Ваша задача - повернуть эти блоки так, чтобы каждая клетка в сетке была освещена за счёт соединения со стартовой клеткой в верхнем левом углу.

### Основные особенности
- **Три типа блоков**: вертикальные, горизонтальные и угловые блоки.
- **Гибкий размер сетки**: игроки могут выбирать размер сетки от 10x10 до 100x100 клеток в настройках.
- **Таймер**: В начале игры запускается двухминутный обратный отсчёт. Если таймер достигает нуля, игра заканчивается, и игрок получает уведомление об этом посредством диалогового окна.
- **Условие победы**: Если все клетки освещены до истечения времени, игрок побеждает и получает уведомление об этом посредством диалогового окна.
- **Анализ после игры**: После неудачной попытки игра отображает правильное расположение блоков, чтобы игрок мог учиться и улучшаться.

## Как играть

1. **Настройте сетку**: Выберите желаемый размер сетки в настройках.
2. **Начните игру**: Запускается двухминутный таймер обратного отсчёта.
3. **Поворачивайте блоки**: Нажимайте на блоки, чтобы повернуть их и соединить линии.
4. **Осветите все клетки**: Убедитесь, что все клетки освещены соединениями от стартовой клетки в верхнем левом углу.
5. **Победите или проиграйте**: Если все клетки освещены до истечения времени, вы побеждаете. Если таймер достигает нуля, игра заканчивается, и вы можете увидеть правильное решение.

## Установка

Чтобы запустить GlowQuest локально, выполните следующие шаги:

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/coldborne/glowquest.git
   cd glowquest
   ```

3. Создайте виртуальное окружение и установите зависимости:
   ```bash
   python -m venv venv
   source venv/bin/activate # На Windows используйте `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Запустите игру:
   ```bash
   main.py
   ```

### Вклад
Добро пожаловать к участию в разработке! Пожалуйста, форкните репозиторий и отправьте pull request для любых улучшений или исправлений ошибок.

### Лицензия
Этот проект лицензирован под лицензией MIT. Подробнее см. файл LICENSE.