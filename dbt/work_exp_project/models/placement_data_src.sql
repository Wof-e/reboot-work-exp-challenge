{{ config(materialized='table') }}

select
    company_name,
    placement_format_desc,
    location_name as location,
    job_family,
    DATE_ADD(DATE '2023-01-01', INTERVAL (week_index-1) WEEK) as start_date,
    length_in_days,
    placement_id,
    school_year_min,
    school_year_max,
    supervisory_organisation_id,
    placement_supervisor_id,
    placement_supervisor_name,
    pd.location_id,
    week_index,
    pd.placement_format_id
from {{ source('work_ref','placement_data')}} pd
inner join {{ source('work_ref','location_metadata')}} lm
    on pd.location_id = lm.location_id
inner join {{ source('work_ref','placement_format_metadata')}} pfm
    on pd.placement_format_id = pfm.placement_format_id


