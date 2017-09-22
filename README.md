# 台糖黑客松 hacktsc 
2017/9/16  
Team: Caltrain

## 引言  
- 利用主辦單位所提供之資料（台糖2016豬隻繁殖資料），設計並實作一個**母豬生育品質預測模型**。   
- 此模型輸入為一特徵向量，特徵向量由母豬某次分娩時若干參數所集成。預測結果為其下一胎的品質等級，分別為「優」、「佳」、「普」、「劣」四等。  
- 豬隻繁殖資料包含三個子資料集：
  - 2016 全場分娩紀錄  
  - 2016 種豬主檔   
  - 2016 銷售主檔  

## 聲明 
所有程式皆為匆促趕工而成，品質差且與最新想法有所出入。目前打算先把完整想法紀錄在說明文件內，往後有機會再更新程式。  

## 方法流程
- 資料預處理
  1. 去除分娩資料中不必要的欄位，留下`母場號、母部門、母耳號、母年期、胎次、分娩活仔數、死亡仔數、斷乳仔數、斷乳窩重、初配日期、受孕日期(再配日)、分娩日期、母豬離乳日期`，最後將有缺值紀錄的刪除。  
  2. 去除種豬資料中不必要的欄位，留下`場號、部門、耳號、年期、出生日期、品種`，最後將有缺值紀錄的刪除。
  3. 將種豬資料併入分娩資料作為一新合成資料集，其中欄位亦有增減，最後保留欄位有`場次、部門、耳號、年期、胎次、分娩數量、分娩死亡數、分娩活仔數、活仔總重、母品種、公品種、母出生到配種成功、公出生到配種成功、初配種到成功、配種成功到分娩、分娩到斷乳`。
  4. 從合併後的資料集推算每筆分娩紀錄的`生育品質指數`，並進一步找出四分位數，將生育品質指數由高至低分為優、佳、普、劣四個等級作為新的資料欄位`生育品質指標`。  
    >  生育品質指數 = 斷乳窩重 - 死亡仔數*死亡仔重     
    >  PS. 資料中暗示死亡仔重皆為1
  5. 將合併資料中每筆紀錄的`生育品質指標`順移至上一胎次作為`次胎品質指標`，並移除首末胎紀錄。
  
- 模型訓練
  - SVM Model
  - Pre-defined classes: `次胎品質指標`
  - Input features: `{場次、部門、胎次、分娩數量、分娩死亡數、分娩活仔數、活仔總重、母品種、母出生到配種成功、初配種到成功、配種成功到分娩、分娩到斷乳}`
  
- 預測結果
  - Cross validation: 5次
  - training:testing = 9:1
  - Results(Accuracy):
    * 61.03%
    * 64.16%
    * 69.11%
    * 73.10%
    * 64.06%
		
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
  * feature encode 的方式也仍然很粗糙，甚至不合邏輯
  * model 還尚待改進，還沒有 Grid 過
  * 總之這就是一個很粗糙的作品...
