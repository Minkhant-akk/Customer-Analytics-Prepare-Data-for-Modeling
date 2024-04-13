import pandas as pd
ds_jobs_clean = pd.read_csv("customer_train.csv")

# Convert integer columns into int32
ds_jobs_clean[["student_id", "training_hours", "job_change"]] = ds_jobs_clean[["student_id", "training_hours", "job_change"]].astype("int32")

# Convert float column into float16
ds_jobs_clean["city_development_index"] = ds_jobs_clean["city_development_index"].astype("float16")

# Convert nominal columns into categories
ds_jobs_clean[['city', 'gender', 'major_discipline', 'company_type']] = ds_jobs_clean[['city', 'gender', 'major_discipline', 'company_type']].astype("category")

# Convert relevant_experience into an ordered category
rel_cats = pd.CategoricalDtype(['No relevant experience', 'Has relevant experience'], ordered=True)

ds_jobs_clean['relevant_experience'] = ds_jobs_clean['relevant_experience'].astype(rel_cats)

# Convert enrolled_university into an ordered category
uni_cats = pd.CategoricalDtype(['no_enrollment', 'Part time course', 'Full time course'], ordered=True)
ds_jobs_clean['enrolled_university'] = ds_jobs_clean['enrolled_university'].astype(uni_cats)

# Convert education_level into an ordered category
edu_cats = pd.CategoricalDtype(['Primary School', 'High School', 'Graduate', 'Masters', 'Phd'], ordered=True)
ds_jobs_clean['education_level'] = ds_jobs_clean['education_level'].astype(edu_cats)

# Convert experience into an ordered category
exp_strings_lst = ['<1'] + list(map(str, range(1, 21))) + ['>20']
exp_cats = pd.CategoricalDtype(exp_strings_lst, ordered=True)
ds_jobs_clean['experience'] = ds_jobs_clean['experience'].astype(exp_cats)

# Convert company_size into an ordered category
cmp_cats = pd.CategoricalDtype(['<10', '10-49', '50-99', '100-499', '500-999', '1000-4999', '5000-9999', '10000+'], ordered=True)
ds_jobs_clean['company_size'] = ds_jobs_clean['company_size'].astype(cmp_cats)

# Convert last_new_job into an ordered category
job_cats = pd.CategoricalDtype(['never', '1', '2', '3', '4', '>4'], ordered=True)
ds_jobs_clean['last_new_job'] = ds_jobs_clean['last_new_job'].astype(job_cats)

# Filter students with 10 or more years experience at companies with at least 1000 employees
ds_jobs_clean = ds_jobs_clean[(ds_jobs_clean['experience'] >= '10') & (ds_jobs_clean['company_size'] >= '1000-4999')]
ds_jobs_clean.head(100)

print(job_cats)
print(ds_jobs_clean.dtypes)
print(ds_jobs_clean)