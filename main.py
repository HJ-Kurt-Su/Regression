import pandas as pd

# from sklearn import linear_model
# from sklearn.linear_model import LinearRegression
# from statsmodels.formula.api import ols
import statsmodels.formula.api as smf


path = r"C:\Users\1907008\Documents\Presentation\HingeBRKT\bonding_brkt_20201203.csv"
df = pd.read_csv(path)

print(df.columns)
print(df.head())
# print(y)
# print(x)

model = smf.ols('ForceP ~ C(MaterialA + Adhesive)', df)
res = model.fit()

print(res.summary())

# regr=linear_model.LinearRegression()
# regr.fit(x, y)
# print(regr.coef_)
# print(regr.intercept_)
# #
# print(df.corr()['ForceP'])
# print(df.corr())


