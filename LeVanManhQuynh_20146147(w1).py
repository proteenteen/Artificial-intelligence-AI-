import pandas as pd

url = 'http://winterolympicsmedals.com/medals.csv'

data=pd.read_csv(url)

# Chọn 1 nước sau đó tính tổng số huy chương vàng, bạc ,đồng từng năm trong từng mỗi môn thi đấu
# Tính tổng số huy chương qua các năm  
# Dự đoán số huy chương từng loại trong mỗi môn thi trong các năm sắp tới

# Chọn 1 nước sau đó tính tổng số huy chương vàng, bạc ,đồng từng năm trong từng mỗi môn thi đấu


NOC = data[data['NOC']=='AUT'].head(2312)
NOC.insert(8,"Total",True)

ans1 =NOC.groupby(['Year','City','Sport','Discipline','Event','Event gender'])['Medal'].value_counts().reset_index(name='Total')
print(ans1)

# Tính tổng số huy chương qua các năm 

ans2 = NOC.groupby(['Year'])['Medal'].value_counts().reset_index(name='Total')
print(ans2)

# Dự đoán số huy chương từng loại trong mỗi môn thi trong các năm sắp tới



