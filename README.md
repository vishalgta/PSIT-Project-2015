# American-Death-Probabilities
ข้อมูลที่มีอยู่ คือ ความน่าจะเป็นในการตายของคนอเมริกา
ปี ค.ศ. 1900 - 2011 อายุ 0 - 119
ชาย หญิง แยกไฟล์กัน

## ฟังชั่นที่จะทำกัน(ใส่ใน main.py)
[Tae] กราฟภาพรวม 2 กราฟ (แบบปี กับ แบบอายุ เป็นแกน x, โอกาสตายเป็นแกน y) ทั้งชายและหญิงอยู่ในกราฟเดียวกัน

แล้วดูว่าช่วงนี้ๆ 

- ทำไมตายกันเยอะจัง 
- หลังๆมาไมตายน้อยลง
- เพศไหนโอกาสตายสูงกว่ากัน
- (ถ้าทำกราฟแล้วเห็นไรมาเพิ่มเลย)

เราก็นำเสนอว่าเกิดไรขึ้น

[] กราฟแยกวัย (ทารก, เด็ก, วัยรุ่น, ผู้ใหญ่, ชรา เป็นแกน x, โอกาสตายเป็นแกน y) ทั้งชายและหญิงอยู่ในกราฟเดียวกัน

แล้วดูว่าช่วงนี้ๆ 

- วัยไหนมีโอกาสตายมากสุด
- เพศไหนโอกาสตายสูงกว่ากัน
- (ถ้าทำกราฟแล้วเห็นไรมาเพิ่มเลย)

เราก็นำเสนอว่าเกิดไรขึ้น

## data_tool.py
มีฟังชั่น load_data() ไว้โหลดข้อมูลทั้งดุ้น ออกมาเป็น dict
      select_data() เลือกข้อมูลได้   ออกมาเป็น dict

รายละเอียดอยู่ในไฟล์
