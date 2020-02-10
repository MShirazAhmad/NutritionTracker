print(Mass, Date)
import pandas as pd

global AccountInfo
AccountInfo = pd.DataFrame({"Gender": ["Male"],
                       "Name": ["Shiraz Ahmad"],
                       "Age": [25], "Height": [5], "Mass": [53], "Activity": [1]})

AccountInfo=AccountInfo.astype(str)
def BMR(Gender, Name, Age, Height, Mass, Activity):
    if Gender == "Male":
        BMR = 66 + (6.3 * Mass) + (12.9 * Height) - (6.8 * Age)
    if Gender == "Female":
        BMR = 655 + (4.3 * Mass) + (4.7 * Height) - (4.7 * Age)
    return BMR

A=BMR(AccountInfo["Name"].loc[0], int(AccountInfo["Age"].loc[0]), int(AccountInfo["Height"].loc[0]), int(AccountInfo["MassAccountInfo"].loc[0]), int(AccountInfo["Activity"].loc[0])):
