# проект автоматизации тестирования отдельного функционала учебного сервиса по заказу самокатов https://qa-scooter.praktikum-services.ru/
1. Проект реализован с помощью фреймвойрка pytest.
2. Установить зависимости — pip install -r requirements.txt.
3. ВНИМАНИЕ: в файлах accordion.py, order.py, transitions.py указан абсолюный путь до браузера Firefox и драйвера geckodriver.Сорри, но 
без этого драйвер не инициализируется.
4. Тесты сгруппированы в файлы в дирректории tests:
accordion.py
test_click_on_how_much
test_click_on_want_some_scooters
test_click_on_how_calculate_rental_time
test_click_on_can_i_order_today
test_click_on_can_expent_reurn_earlier
test_click_on_charging_with_a_scooter
test_click_on_can_cancel_order
test_click_on_live_further_than_mkad

order.py
test_click_on_button_order_in_head
test_click_on_button_order_in_footer
test_filling_user_by_order_for_who

transitions.py
test_transition_to_main_page_click_logo
test_transition_to_yandex_page

5.Классы страниц, локаторы, методы для работы с элементами страниц находятся в директории  pages
в файлах mainpage.py, orderpage.py, yandexpage.py.

6. Команда для запуска pytest -v tests/filename.py --alluredir=allure_results
7.Отчеты о тестировании находятся в директории allure_results
8.Просмотр отчетов: allure serve allure_results 

