import streamlit as st
import pandas as pd

# Page title
st.title("Salary Projection for Next 5 Years")

# Inputs: Current CTC and Average Hike %
current_ctc = st.number_input("Enter your current CTC (Annual)", value=500000.0, step=10000.0)
avg_hike = st.number_input("Enter Average Hike Percentage (%)", value=8.0, step=0.5)
current_age = st.number_input("Enter your current age", value=26, step=1)
professional_tax = st.number_input("Enter your states Professional tax", value=200, step=50)
employer_pf=st.number_input("Enter your employers PF",value=1800,steps=100)
employee_pf=st.number_input("Enter your employee PF",value=1800,steps=100)

# Convert hike to a multiplier
hike_multiplier = 1 + (avg_hike / 100)

# Create a DataFrame to store the salary progression
salary_data = {
    "Sr. No": [],
    "Salary Yearly": [],
    "Salary per month": [],
    "Year": [],
    "Hike Percentage": [],
    "Age": []
}

# Initial year and salary
year = 2024
salary_yearly = current_ctc
# Inhand_sal=(salary_yearly / 12) - professional_tax - employer_pf - employee_pf
# Calculate the salary progression for 5 years
for i in range(5):
    salary_data["Sr. No"].append(i + 1)
    salary_data["Salary Yearly"].append(round(salary_yearly, 2))
    # salary_data["Salary per month in Hand"].append(round(Inhand_sal), 2)
    salary_data["Salary per month in Hand"].append(round(((salary_yearly / 12)-professional_tax - employer_pf - employee_pf), 2))
    # salary_data["Salary per month"].append(round((salary_yearly / 12), 2))
    salary_data["Year"].append(year + i)
    salary_data["Hike Percentage"].append(round(avg_hike / 100, 2) if i != 0 else 0)
    salary_data["Age"].append(current_age + i)

    # Update salary for next year
    salary_yearly *= hike_multiplier

# Convert to DataFrame for better display
df = pd.DataFrame(salary_data)

# Display the salary progression table
st.subheader("Salary Progression Over the Next 5 Years")
st.dataframe(df)

# Optional: Download as CSV
csv = df.to_csv(index=False)
st.download_button("Download CSV", data=csv, file_name='salary_projection.csv', mime='text/csv')

st.markdown("**Project by [Gajanan Todeti](https://github.com/tgajanan)**")
