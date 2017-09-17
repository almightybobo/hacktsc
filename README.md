2017/9/16 台糖黑客松 hacktsc 組別: Caltrain

# 目標
* 台糖2016豬隻族譜(繁殖)資料
  - 找出優良種豬，利用雜交優勢培育
  - 生的多，養的好，死的少（少死多賣售價高）
  - 可用利用品種和基因型進行分析，但基因型資料僅部門80有且亦不齊全

# 聲明
* 所有程式都是在很匆促的狀況下趕出來
  - 不確定有沒有蟲
  - 品質都很差，很多都是硬幹出來的，連自己看了都很痛苦
  - 不過都是可以 work 的，但也只是能 work 而已
  - 本人和協作者都當菸酒生，以後有心情再來改進呵呵

# 檔案路徑介紹
  * data => 存放原始資料以及中間處理的資料
    - raw_utf8 => 存放主辦單位所給的原始資料
      - birth.csv => 分娩資料
      - identification.csv => 種豬主檔
      - sales.csv => 銷售主檔
    - about_place_in_merge => 統計各個豬廠的狀況，含平均每胎總數、平均每胎存活數、平均每胎死亡數
    - birth_pruned.csv => 初步取出分娩資料中有用的欄位
    - identification_pruned.csv => 初步取出種豬主檔內有用的欄位
    - merge.csv => 將 birth_prined.csv 和 identification_pruned.csv 做結合，並觀察缺值決定最終要使用的 feature
    - sales_each_dept_type40.csv =>
    - sales_each_dept_type41.csv =>
    - sales_each_dept_type70.csv =>
  * graph => 程式產生的統計圖表
    - 1.png => 各豬場豬隻總數
    - 2.png => 各品種豬隻總數
    - sales_each_dept
      - sales_each_dept_type40.png
      - sales_each_dept_type41.png
      - sales_each_dept_type70.png
  * src => 程式檔
    - preprocess => data 預處理使用的程式
      - birth_pruning.py => 輸入：分娩原始資料 輸出：birth_pruned.csv
      - identification_pruning.py => 輸入：種豬主檔原始資料 輸出：identification_pruned.csv
      - merge.py => 輸入：birth_pruned.csv & identification_pruned.csv 輸出：merge.csv
    - statistic => 統計資料使用的程式
      - merge_stat.py => 輸入：merge.csv 輸出：about_place_in_merge
      - sales_stat.py =>
    - ML => 進行 machine learning 所需程式，使用的 model 為 SVM
      - svm.py => 將 merge.csv 的欄位轉換成數值化的 feature，並分出 class(用活小豬重量分成四個 label) 來進行 training 以及 evaluation
# 待改進部分
  * label 的設計，現在只是很粗糙的分類，直接用 regression 出來的結果很差
  * feature 量不足，現在能從 data 裡分析出的 feature 很少
  * model 還尚待改進，還沒有 Grid 過
  * 總之這就是一個很粗糙的作品...
