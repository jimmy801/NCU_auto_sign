# NCU_auto_sign
## Introduction
中央大學工讀生自動簽到程式，可以使用參數設置簽到時間(時長)、簽到頁 ID、帳號和密碼
## Environment
- ununtu 16.04
- python 3.6
- also has [Dockerfile](https://github.com/jimmy801/NCU_auto_sign/blob/master/dockerfile/Dockerfile)
## 使用方式
下載專案
```bash= !
$ git clone https://github.com/jimmy801/NCU_auto_sign.git
```
移至專案路徑
```bash= !
$ cd NCU_auto_sign
```
安裝必須套件
```bash= !
$ pip install -r requirment.txt
```
執行程式
```bash= !
$ python crawler.py [ARGS(-t, -wid, -a, -p)]
```
[ARGS] 介紹
- `-t`, `--time`: 簽到時長(hr)，預設為 `4`
- `-wid`, `--work_id`: 簽到頁 ID，預設為空，可以修改程式碼來設置預設值<br>
    請至[中央大學人事系統簽到退作業](https://cis.ncu.edu.tw/HumanSys/student/stdSignIn)中表格點選 `新增簽到` 按鍵後的網址應為 https://cis.ncu.edu.tw/HumanSys/student/stdSignIn/create?ParttimeUsuallyId=XXXX ，XXX 即簽到頁 ID<br>
    ![](https://i.imgur.com/xID5JPk.png)
- `-a`, `--account`: 使用者帳號，預設為空，可以修改程式碼來設置預設值
- `-pwd`, `--password`: 使用者密碼，預設為空，可以修改程式碼來設置預設值

