### Программа для одновременного постинга сообщений  в VK,Telegram и Facebook




#### Описание:

Программа-планировщик использует Google Sheets API для работы с таблицами и API VK,Telegram и Facebook для отправки сообщений( или сообщений с изображеними)на стену в группы указаных соц сервисов.



#### Установка

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей: 

```
pip3 install -r requirements.txt
```


#### Перед первым запуском необходимо выполнить ряд обязательных условий :
Создайте  файл .env в дирректории с приложением 

ID таблицы необходимо указать в  файле .env
```
SHEET_ID = 'id вашей таблицы'
```


<b>1) По ссылке ниже включите API и получите credentials.json продублируйте дав новое имя client_secrets.json
 (необходимо для работы PyDrive)</b>

 https://developers.google.com/sheets/api/quickstart/python









<b>2) Получите "ключ доступа пользователя" ,создайте группу и альбом в данной группе VK </b>

Для этого необходимо перейти по ссылке :

https://vk.com/dev

Cоздав приложение и скопировать его "ID приложения"(понадобится нам в следующем шаге)

Перейти по ссылке:

https://vk.com/dev/implicit_flow_user

получить access_token

Значение токена и Ваш логин в VK необходимо указать в  файле .env

```
VK_LOGIN='user@mail.com'
VK_TOKEN='533bacf01e11f55b536a565b57531ad114461ae8736d6506a3'

```
Создать группу и альбом в соответствующей группе

Необходимо добавить в группу минимум одного участника

В конфигурационном файле приложения .env указать ID группы и ID альбома группы
```
GROUP_ID=
ALBUM_ID=
```

<b>3) Создать Telegram канал и Telegram бота,получить токен: </b>

Создать бота можно написав сообщение боту BotFather
при успешном создании в ответе будет token

```Use this token to access the HTTP API:
7078612782:AAkljKLJFD89SDS3SDBrJtnies
```
Создав канал в информации о канале будет его ID 

https://t.me/dl_test


где dl_test (@dl_test) - ID канала


В  файле  .env указать ID канала и токен

```

TELEGRAM_CHANNEL_ID='@dl_test'
TELEGRAM_TOKEN='7078612782:AAkljKLJFD89SDS3SDBrJtnies'
```
<b>4) Создать группу и получить токен Facebook </b>

Получить токен проще с помощью браузерного интерфейса к API Facebook.
инструкция :

https://developers.facebook.com/docs/graph-api/explorer/

узнать ID группы можно перейдя в созданную группу
```
https://www.facebook.com/groups/123332145271
```
где '123332145271' -ID группы

Необходимо добавить в группу минимум одного участника

В  файле .env указать Токен и ID группы

```
FACEBOOK_TOKEN='EAAID786y3kjhlfsdfsdfsdf4ffdsfoijf4098jfn87hujkdfWTsZD'
FACEBOOK_GROUP_ID='123332145271'

```

#### Работа с программой:
Программа настроена на работу с таблицей аналогичной:

https://docs.google.com/spreadsheets/d/17r4QRW_m0clut772bRnUL-U1-JiazImiZMm43SkgS9Q

Программа анализирует аналогичным образом созданную таблицу и согласно текущего дня недели и времени запускает разрешенные  в столбцах(Соцсети) свои модули Соцсетей с последующей публикацией информации.
При успешном запуске и постинге,программа отмечает значением "ДА" в разделе "Опубликовано?"
статьи загружаются из ссылок указанных в  разделе "Статья" изображения ,соответственно  из "Картинки"
Перед публикацией  автоматически запускается браузер, установленный по умолчанию в системе с просьбой дать разрешение на запись в таблицу.
Программа запускается в бесконечном цикле с интервалом в 5 минут.
```
$python3 main.py
Окно или вкладка откроются в текущем сеансе браузера.
Authentication successful.
1 cells updated.
```


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.

2019 Dark_Dmake

