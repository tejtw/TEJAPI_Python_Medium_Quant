import tejapi
import matplotlib.pyplot as plt

tejapi.ApiConfig.api_key = "your_api_key"

company = '2330'
price_data = tejapi.get('TWN/EWIFINQ', # tej 財務資料庫
                coid = company,
                mdate={
                    # 起始日期    
                    'gte':'2022-01-01', 
                    # 結束日期
                    'lte':'2022-12-31'}, 
                opts={'columns': ['coid','mdate','ac_3990']}, 
                paginate=True
            )

company_data = tejapi.get(
        'TWN/EWPRCD',  # 資料庫
        coid=company,  # 股票代碼
        mdate={
                    # 起始日期    
                    'gte':'2018-01-01', 
                    # 結束日期
                    'lte':'2018-12-31'}, 
        paginate=True,  
        opts={'columns': ['mdate', 'close_d']},
    )

print(price_data['ac_3990'])
print(company_data['close_d'])
close = company_data['close_d']

Price_to_Earnings_Ratio = []
quarter = [60,63,63,61]
quarter_count = 0
season_days = 0
init_day = 0

while quarter_count<4:
    season_days = quarter[quarter_count] # 每季有幾天
    print(init_day+season_days)
    for i in range(init_day, int(init_day+season_days)):
        Price_to_Earnings_Ratio.append(round(company_data['close_d'][i]/price_data['ac_3990'][quarter_count]))
    init_day = init_day + season_days
    quarter_count += 1

# print(Price_to_Earnings_Ratio)
# 設定畫出本益比倍數
x = [x for x in range(0, len(close))]
Price_to_Earnings_Ratio_30 = [ratio * 30 for ratio in Price_to_Earnings_Ratio]
Price_to_Earnings_Ratio_35 = [ratio * 35 for ratio in Price_to_Earnings_Ratio]
Price_to_Earnings_Ratio_40 = [ratio * 40 for ratio in Price_to_Earnings_Ratio]
Price_to_Earnings_Ratio_45 = [ratio * 35 for ratio in Price_to_Earnings_Ratio]
Price_to_Earnings_Ratio_50 = [ratio * 50 for ratio in Price_to_Earnings_Ratio]

# 畫出本益比
plt.plot(x, Price_to_Earnings_Ratio_30, label='Ratio=30', color='blue') 
plt.plot(x, Price_to_Earnings_Ratio_35, label='Ratio=35', color='blue') 
plt.plot(x, Price_to_Earnings_Ratio_40, label='Ratio=40', color='yellow')
plt.plot(x, Price_to_Earnings_Ratio_45, label='Ratio=45', color='brown')
plt.plot(x, Price_to_Earnings_Ratio_50, label='Ratio=50', color='purple')
plt.plot(x, close.tolist(), label='K line', color='red') # 畫出收盤價曲線

plt.title('Price_to_Earnings_Ratio')  # 設定圖形標題
plt.xlabel('Days')  # 設定X軸標籤
plt.ylabel('Ratio')  # 設定Y軸標籤
plt.legend()  # 添加圖例
plt.show()

