<H1>Проект для реализации интернет-магазина на фреймворке DJANGO.</H1>
<br></br>


Необходимо в корне проекта создать файл **.env** и внести в него свои данные для переменных по образцу из **.env.sample**.

Для наполнения БД тестовыми данными выполните команду **python manage.py fill_base** и **python manage.py fill_blog** .

Для использования почтовой рассылки и регистрации новых пользователей не забудьте заполнить в **.env**:
<br>EMAIL_HOST = ''</br>
<br>EMAIL_HOST_USER = ''</br>
<br>EMAIL_HOST_PASSWORD = ''</br>

<br></br>
<H3>!!!Примечание!!!</H3>
Необходимо в настройках вашего почтового провайдера создать т.н. App Password и ввести его в поле EMAIL_HOST_PASSWORD,
это сделано в целях безопасности.
<br>Как это сделать для: </br> 
<a name="links">[Mail.ru](https://help.mail.ru/mail/security/protection/external)<h2></h2></a>
<a name="links">[Gmail](https://www.lifewire.com/get-a-password-to-access-gmail-by-pop-imap-2-1171882)<h2></h2></a>
<a name="links">[Yandex](https://yandex.ru/support/id/authorization/app-passwords.html)<h2></h2></a>
