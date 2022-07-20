from asyncio import wait_for
from os import waitid_result
from tkinter import W


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

#       // Para obter mais informações, acesse: https://go.microsoft.com/fwlink/?linkid=830387
#     "version": "0.2.0",
#     "configurations": [
#         {
#             "type": "pwa-msedge",
#             "request": "launch",
#             "name": "Open index.html",
#             at wait_for._compile (node:internal/modules/cjs/loader:1105:14)
#             at w.Module._extensions..js (node:internal/modules/cjs/loader:1159:10)
#             at while.load (node:internal/modules/cjs/loader:981:32)
#             at waitid_result.Module._load (node:internal/modules/cjs/loader:822:12)
#             at wait_for.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:77:12)
#             at WindowsError:internal/main/run_main_module:17:47
# #         
#         }
#     ]
# }
