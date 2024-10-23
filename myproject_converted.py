import pandas as pd

df = pd.read_csv(r"E:\Downloads\employee_experience_survey_data (1).csv")

df

selected_columns = ['Age Bracket', 'Gender', 'Ethnicity', 'Work-Life Balance', 'Compensation Satisfaction']
df_selected = df[selected_columns]

df_selected

df['Comp_Satisfaction_Code'], comp_uniques = pd.factorize(df_selected['Compensation Satisfaction'])
df['WLB_Code'], wlb_uniques = pd.factorize(df_selected['Work-Life Balance'])


df

df_selected

selected_columns = ['Age Bracket', 'Gender', 'Ethnicity', 'Comp_Satisfaction_Code', 'WLB_Code']
df_selected = df[selected_columns]

df_selected

avg_by_age = df_selected.groupby('Age Bracket').mean(numeric_only=True)
avg_by_gender = df_selected.groupby('Gender').mean(numeric_only=True)
avg_by_ethnicity = df_selected.groupby('Ethnicity').mean(numeric_only=True)

print(df_selected.dtypes)

print("\nAverage Work-Life Balance and Compensation Satisfaction by Age Bracket:")
print(avg_by_age)
print("\nAverage Work-Life Balance and Compensation Satisfaction by Gender:")
print(avg_by_gender)
print("\nAverage Work-Life Balance and Compensation Satisfaction by Ethnicity:")
print(avg_by_ethnicity)

summary_file = 'summary_averages.xlsx'
with pd.ExcelWriter(summary_file) as writer:
    avg_by_age.to_excel(writer, sheet_name='Avg by Age Bracket')
    avg_by_gender.to_excel(writer, sheet_name='Avg by Gender')
    avg_by_ethnicity.to_excel(writer, sheet_name='Avg by Ethnicity')


print(f"\nSummary data saved to {summary_file}")



