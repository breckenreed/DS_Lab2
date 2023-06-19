## DS_Lab2



1. Встановити і налаштувати Hazelcast

> $ pip install hazelcast-python-client
> docker pull 

2. Сконфігурувати і запустити 3 ноди

Створюємо мережу Docker згідно з https://docs.hazelcast.com/hazelcast/5.3/getting-started/get-started-docker :

> docker network create hazelcast-network

Cтворюємо три контейнери Hazelcast та контейнер Hazelcast Management Center:
<img width="588" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/f0a01866-7eab-4fbe-8db6-af5b6d290301">


При додаванні нового контейнера попередні автоматично дізнаються про це:

<img width="1204" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/589f3ff6-afca-4411-9f28-35c45e4cd45d">

<img width="1173" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/816a0b0a-a5eb-4a96-9271-83fa447df5bd">




<img width="1439" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/d7f75d1f-0518-4838-902a-859b7d57bfd5">


3.Продемонструйте роботу Distributed Map
<img width="554" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/49295a9c-7ccc-4bda-8aeb-2ae5fe7b94d8">

<img width="545" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/18e5aaca-8132-4c55-afd6-af904803bac8">





6. Продемонструйте роботу Distributed map with locks. <br />

 a-1) Запускаємо nolock_map.py в одному потоці, бачимо що результат передбачувано інкрементується з кожним разом: <br />
<img width="524" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/e9c2e9f1-9a25-43d4-ad6a-1df5ba5bb0fe">

 а-2) Запускаємо nolock_map.py водночас у двох потоках, результати починають неконтрольовано змінюватися, спостерігається data race. <br />

В одному потоці бачимо одну відповідь, в іншому - іншу (друга операція була запущена під час виконання першої). <br />
 <img width="524" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/85dbbb70-a6a2-491a-a6d1-8288d98fd090"> <br />
 <img width="558" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/0ddfc17a-e1a9-4da9-bccd-3369b6de5f89"> <br />
 <img width="530" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/8b420f3d-faeb-40cf-ba38-185ded1524ad"> <br />



