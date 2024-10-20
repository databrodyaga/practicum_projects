# Определение возраста покупателей для магазина "Хлеб-соль"

## Описание проекта
Сетевой супермаркет «Хлеб-Соль» внедряет систему компьютерного зрения для обработки фотографий покупателей. Фотофиксация в прикассовой зоне поможет определять возраст клиентов, чтобы:  
- Анализировать покупки и предлагать товары, которые могут заинтересовать покупателей этой возрастной группы;  
- Контролировать добросовестность кассиров при продаже алкоголя.

Необходимо построить модель, которая по фотографии определит приблизительный возраст человека. В нашем распоряжении набор фотографий людей с указанием возраста.

Метрикой качества будет MAE.

Рекомендации:  
- Функцией потерь не обязательно должна быть MAE. Зачастую нейронные сети с функцией потерь MSE обучаются быстрее.  
- Качество на валидационной выборке улучшается, но модель при этом переобучается всё сильнее? Не спешите менять модель. Обычно нейронные сети с большим числом слоёв сильно переобучаются.

Необходимо построить и обучить свёрточную нейронную сеть на датасете с фотографиями людей. Целевое значения MAE на тестовой выборке не больше 8.  
В [статье о датасете](https://inria.hal.science/hal-01677892/document), с которым будем работать, значение MAE равно 5.4 — если получим MAE меньше 7, это будет отличный результат!

## Описание данных
Данные взяты с сайта [ChaLearn Looking at People](http://chalearnlap.cvc.uab.es/dataset/26/description/).  
В нашем распоряжении одна папка со всеми изображениями (/final_files) и CSV-файл labels.csv с двумя колонками: file_name и real_age. 
Извлечь данные из папки вам поможет метод [ImageDataGenerator](https://keras.io/preprocessing/image/) —flow_from_dataframe(dataframe, directory, ...).

Конкретные шаги анализа и прогнозирования данных приведены по тексту ноутбука.  

В данном проекте отработаны следующие аспекты темы **Компьютерное зрение**:  
- Введение в компьютерное зрение (решение простые задачи компьютерного зрения с привлечением готовых нейронных сетей и библиотеки Keras)  
- Полносвязные сети  
- Свёрточные сети