# Calculator to determine Profit Margin

ForeignCost = float(input('Enter Foreign Cost  '))
Rate = float(input('Enter exchange rate  '))
SalePrice = float(input('Enter Sale Price  '))
Profit = float(1.05)
ImportFee = float(5)

FinalCost = ((ForeignCost * Rate) * Profit) + ImportFee
print(FinalCost)

CostPercentage = (SalePrice - FinalCost) / SalePrice
print(CostPercentage)