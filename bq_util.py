from google.cloud import bigquery

gcp_project_id = 'innovation-nation-389906'
client = bigquery.Client(project=gcp_project_id)

class Student:
  def __init__(self, name, year_group, location, availability_months,interests,duration):
    self.name = name
    self.location = location
    self.availability_months = availability_months
    self.interests = interests
    self.year_group = year_group
    self.duration = duration

class Placement:
  def __init__(self, organisation, duration, location, start_date,job_family, school_year_max, school_year_min):
    self.organisation = organisation
    self.duration = duration
    self.location = location
    self.start_date = start_date
    self.job_family = job_family
    self.school_year_max = school_year_max
    self.school_year_min = school_year_min


def fetch_placements(student_filter):
    interests_str = str(student_filter.interests).replace('[','(').replace(']',')')
    months_str = str(student_filter.availability_months).replace('[','(').replace(']',')')

    sql_query = f"select * from `{gcp_project_id}.work_exp_ds.placement_data_src` where " \
                 f"school_year_min <={student_filter.year_group} and school_year_max>= {student_filter.year_group} " \
                 "and placement_format_desc = 'In Person' "\
                 f"and upper(location) like upper('%{student_filter.location}') "\
                 f"and job_family in {interests_str} "\
                 f"and length_in_days >= {student_filter.duration} and upper(FORMAT_DATE('%B', start_date)) in {months_str}"
    print(sql_query)
    query_job = client.query(sql_query)  # Make an API request.

    placement_list =[]
    for row in query_job:
        print(row)
        p = Placement(row['company_name'],row['length_in_days'],row['location'],row['start_date'],row['job_family'],
                                        row['school_year_max'],row['school_year_min'])
        placement_list.append(p)

    return placement_list



if __name__ == "__main__":
    month_list = ['MARCH','APRIL']
    interest_list = ['Legal','Infrastructure Engineering']
    filter = Student('mno',10,'London',month_list,interest_list,2)
    print(fetch_placements(filter))

