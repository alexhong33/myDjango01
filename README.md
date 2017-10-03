# myDjango01
Python日常项目

#### 依赖：
    * pip install django==1.8.2

#### 管理员账号

* username：abc
* password：12345

#### 启动
* python manage.py runserver


#### 忘记管理员密码

    >>> from django.contrib.auth.models import User
    >>> user = User.objects.get(pk=1)
    >>> user
    <User: you_account>
    >>> user.set_password('your_new_password')
    >>> user.save()
    >>> quit()