import concurrent.futures
import logging
from random import randint
from time import sleep


def greeting(name):
   logging.debug(f'greeting for: {name}')
   sleep(randint(0, 3))
   return f"Hello {name}"


arguments = (
   "Bill",
   "Mark",
   "Sam",
   "Tom",
   "John",
)

if __name__ == '__main__':
   logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
   with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
      results = list(executor.map(greeting, arguments))

   logging.debug(results)

"""
Створюємо ThreadPoolExecutor та задаємо, що робота буде виконуватися не більше ніж 2 потоками. 
Пул можна створити в менеджері контексту, щоб бути впевненим, що всі ресурси будуть коректно повернуті до системи після завершення. 
Але це не обов'язково, можна створити пул і потім викликати у нього метод shutdown, щоб завершити всі потоки та повернути ресурси системі.
"""
#########################################
"""
ThreadPoolExecutor-0_0 greeting for: Bill
ThreadPoolExecutor-0_1 greeting for: Mark
ThreadPoolExecutor-0_1 greeting for: Sam
ThreadPoolExecutor-0_0 greeting for: Tom
ThreadPoolExecutor-0_1 greeting for: John
MainThread ['Hello Bill', 'Hello Mark', 'Hello Sam', 'Hello Tom', 'Hello John']
"""
