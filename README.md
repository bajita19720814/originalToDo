# 付箋アプリ（Windows版 ToDo アプリ）

Python（Tkinter）で作った Windows 用の ToDo アプリです。
PC 起動時に自動で立ち上がり、付箋のように画面端にタスクを表示します。

## 主な機能
- タスクの追加・削除
- SQLite によるデータ保存
- カラー設定
- UI フォルダでレイアウト管理
- 付箋で指定のタスクを常駐  
     PC起動時にアプリを起動し表示期間にある付箋をPC右上部に常駐。  
     メイン画面（タスク入力画面）は最小化してタスクバーに。  
※ タスク変更後、付箋の表示を切り替えるにはアプリを再起動する必要があります。

## ダウンロード
Releases から Setup.exe をダウンロードしてください。

## スクリーンショット
  <img width="240" alt="win_mobile" src="https://github.com/user-attachments/assets/8c251103-57db-43fb-98b2-934ac78566f9" />


## 使用技術
- Python 3.x
- Tkinter
- SQLite
- PyInstaller
- Inno Setup

## インストール方法
1. Setup.exe を実行
2. インストーラーの指示に従うだけで完了  
   ※　起動時タスク入力画面は最小化してタスクバーに表示されます。タスク入力、変更後に付箋の表示を変更するにはアプリの再起動が必要です。

## ライセンス
MIT License
