## DS_Lab2

1. Встановити і налаштувати Hazelcast

> $ pip install hazelcast-python-client
> docker pull 

2. Сконфігурувати і запустити 3 ноди

Створюємо мережу Docker згідно з https://docs.hazelcast.com/hazelcast/5.3/getting-started/get-started-docker :

> docker network create hazelcast-network

Cтворюємо три контейнери Hazelcast та контейнер Hazelcast Management Center:
<img width="588" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/f0a01866-7eab-4fbe-8db6-af5b6d290301">


При додаванні нового контейнера попередні автоматично дізнаються про це: <br />

<img width="1204" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/589f3ff6-afca-4411-9f28-35c45e4cd45d"> <br />

<img width="1173" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/816a0b0a-a5eb-4a96-9271-83fa447df5bd"> <br />




<img width="1439" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/d7f75d1f-0518-4838-902a-859b7d57bfd5"> <br />


3.Продемонструйте роботу Distributed Map <br />
<img width="572" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/4179e295-8752-49e0-8932-05738b156a33"> <br />

<img width="545" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/18e5aaca-8132-4c55-afd6-af904803bac8"> <br />

Дані нестрого розподілені на 3 частини у трьох кластерах:  <br />
<img width="1433" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/20e8b578-95b6-46ba-b658-02847bdf7432"> <br />

4.Подивитись як зміниться розподіл якщо відключити:
При вимкненні однієї ноди бачимо, що дані розподіляються по двом нодам, що залишилися: <br />
<img width="1208" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/da5152e7-7b8f-44e1-90cb-75173903da30"> <br />
<img width="486" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/85381077-e6a0-4e0f-b9e9-0b18e7c6051f"> <br />
За допомогою скрипту checker.py бачимо, що втрат даних немає. <br />

Аналогічно, коли дві ноди вимкнені: <br />
<img width="1207" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/6c1d27b8-1e29-4aab-bd68-9410138bf2d3"> <br />
<img width="528" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/27992a89-08be-45da-a683-8c4e4fca9e53"> <br />

5. Заміна backup-count <br />
  Дістаємо конфіг файл із контейнера за допомогою cat /opt/hazelcast/config/hazelcast-docker.xml та міняємо backup-counts на <br />

а) 0 <br />
<img width="989" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/d6617529-eb3b-4906-a65a-e1a4887e0e3e">

При зміні backup-count на 0 у всіх мемберах кластеру, запис карти за допомогою distributed-map.py відбувся набагато швидше і зайняв всього 20 секунд порівняно із записом із backup-count 1 (котрий тривав 40-50 хвилин)
<img width="1237" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/e52277d5-9f42-4211-bab8-ca10c3f14feb">

Втім, дані втрачаються при вимкненні нод:
<img width="1238" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/493f6d53-4a5b-4d54-a036-c37424986f1c">
<img width="1240" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/92d7a939-f4f2-412f-978f-8519bab59186">

б) 2 <br />
<img width="869" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/635e7577-6d54-4ec0-85f1-7a0f608aaa7c"> <br />

Зменшили кількість ітерацій до 100 щоб уникнути довгого завантаження даних: <br />
<img width="1229" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/c80255a8-4f0e-4d54-b105-b7bc12e361c8"> <br />

backup memory має вдвічі більший розмір за entry memory: <br />
<img width="1223" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/794a1ac6-02be-4192-ba2d-f1b6ddeeb1e3"> <br />

При вимкненні одної ноди реагує подібно до backup-counts=1:
<img width="1227" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/cb9693ae-f7ee-44e6-a4ea-bc8501d5e612"> <br />

Двох нод: 
<img width="1249" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/ef69a068-9dd0-4def-875d-eec4eb13f3e8"> <br />

7. Продемонструйте роботу Distributed map with locks. <br />

 a-1) Запускаємо nolock_map.py в одному потоці, бачимо що результат передбачувано інкрементується з кожним разом: <br />
<img width="524" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/e9c2e9f1-9a25-43d4-ad6a-1df5ba5bb0fe"> <br />

 а-2) Запускаємо nolock_map.py (назва файлу мінялася в процесі виконання роботи) водночас у двох терміналах, результати починають неконтрольовано змінюватися, спостерігається data race. <br />
<img width="666" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/efc2e8a5-c3c7-48a6-9ecf-19141a8e0311"> <br />


 б) Optimistic locking:  <br />
  При одночасному запуску двох opt_lock у нас виводиться один стійкий результат: <br />

<img width="617" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/1f6bd3a6-1c11-407a-b8c6-56feeec84bfc"> <br />

  

 в) Pessimistic locking:
 Бачимо стабільний реузультат, хоч і продуктивність на порядок менша. Різниця в 1 присутня через те, що в одному з потоків спрацьовує функція ```put_if_absent(key, 1)``` <br />

<img width="640" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/8ef21760-251f-40bc-aab1-c79ea79bde63"> <br />
<img width="579" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/280f3311-ee1e-410c-8a14-e050a4f724f9"> <br />


7. Налаштуйте Bounded queue <br />

Встановлюємо максимальну величину черги у розмірі "13": <br />
<img width="299" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/4919db98-bb26-47b9-a1ef-60251f0eff8e"> <br />

Якщо одночасно запустити в одному терміналі запис, а в інший - читання, то бачимо, що при затримках sleep по 0.5 сума кількості елементів черги не перевищує 8 <br />
<img width="1248" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/a99544a3-d898-49fc-ac5f-867b2b72ddab"> <br />

<img width="473" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/6008900d-dd6b-4162-ba6f-6545a080e235"> <br />
<img width="520" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/3603902a-d6da-4141-9dce-738c473d40aa"> <br />


А) з однієї ноди (клієнта) йде запис, а на двох інших читання: <br />

Якщо затримка читання є близькою до затримки запису, то читання з двох клієнтів призведе до того, що агрегована сума черги не буде зростати, адже читання відбуватиметься швидше за запис, а іноді - навіть швидше за вивід дебагу процесу запису принтом: <br />

<img width="1263" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/61950202-2612-4820-827f-aadcff10c476"> <br />
<img width="722" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/4864cc51-5332-47ed-bb4e-658aa2ac41f7"> <br />

Б) перевірте яка буде поведінка на запис якщо відсутнє читання, і черга заповнена <br />

Запис припиняється на досягненні max-size 13: <br />
<img width="617" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/067c00ad-3fa9-4577-8c2e-7dfecf0da1fd"> <br />
<img width="376" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/4f743083-e2aa-43df-9740-73486e8b4d27"> <br />
Черга не приймає елементів на запис від жодних клієнтів до звільнення в ній місця <br />

В) як будуть вичитуватись значення з черги якщо є декілька читачів  <br />
Перший читач має затримку 2 секунди, другий 6 секунд. Отже, за замовчуванням, більшу частину черги зчитує клієнт із меншою затримкою <br />

<img width="610" alt="image" src="https://github.com/breckenreed/DS_Lab2/assets/62158298/cc1a0222-18ef-4d94-a3b1-71634d202913"> <br />
