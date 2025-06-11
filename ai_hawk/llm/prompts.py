# Prompt templates used by llm_manager

# These strings provide default prompts for different
# sections of a resume or job application. They can be
# customized to fit your use case.

summarize_prompt_template = (
    "Summarise the following job description in a few key points:\n{text}"
)

personal_information_template = (
    "Use the following personal information to answer the question:\n"
    "{resume_section}\nQuestion: {question}"
)

self_identification_template = (
    "Refer to the self identification details to answer the question:\n"
    "{resume_section}\nQuestion: {question}"
)

legal_authorization_template = (
    "Use the legal authorization information to answer the question:\n"
    "{resume_section}\nQuestion: {question}"
)

work_preferences_template = (
    "Use the work preferences provided to answer the question:\n"
    "{resume_section}\nQuestion: {question}"
)

education_details_template = (
    "Use the education details to answer the question:\n"
    "{resume_section}\nQuestion: {question}"
)

experience_details_template = (
    "Use the experience details to answer the question:\n"
    "{resume_section}\nQuestion: {question}"
)

projects_template = (
    "Use the projects information to answer the question:\n"
    "{resume_section}\nQuestion: {question}"
)

availability_template = (
    "Use the availability information to answer the question:\n"
    "{resume_section}\nQuestion: {question}"
)

salary_expectations_template = (
    "Use the salary expectations to answer the question:\n"
    "{resume_section}\nQuestion: {question}"
)

certifications_template = (
    "Use the certification details to answer the question:\n"
    "{resume_section}\nQuestion: {question}"
)

languages_template = (
    "Use the languages listed to answer the question:\n"
    "{resume_section}\nQuestion: {question}"
)

interests_template = (
    "Use the interests listed to answer the question:\n"
    "{resume_section}\nQuestion: {question}"
)

coverletter_template = (
    "Write a short cover letter using the resume and job description:\n"
    "Resume: {resume}\nJob Description: {job_description}\nCompany: {company}"
)

determine_section_template = (
    "Identify which section of the resume can best answer the question:\n"
    "{question}"
)

numeric_question_template = (
    "Answer the numeric question using the provided resume information:\n"
    "Educations: {resume_educations}\nJobs: {resume_jobs}\nProjects: {resume_projects}\nQuestion: {question}"
)

options_template = (
    "Choose the best option that answers the question based on the resume:\n"
    "Question: {question}\nOptions: {options}"
)

resume_or_cover_letter_template = (
    "Does the phrase relate to the resume or the cover letter?\nPhrase: {phrase}"
)

is_relavant_position_template = (
    "Given the resume and job description, determine if the position is relevant\n"
    "Resume: {resume}\nJob Description: {job_description}"
)
