#prg 14(b)
import pandas as pd  
import seaborn as sns 
import matplotlib.pyplot as plt 
df2 = pd.read_csv(r"C:/Users/karun/Downloads/10prog_4laptops - 10prog_4laptops.csv")  
sns.pairplot(df2) 
plt.show() 
