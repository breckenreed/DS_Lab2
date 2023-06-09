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
<img width="580" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/9a2d32b8-3aa7-4821-b5aa-665c919390f9">


