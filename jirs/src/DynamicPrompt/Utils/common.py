from jiraone import LOGIN, issue_export, add_log, endpoint
from DynamicPrompt.constants import FIELDS_TO_BE_INCLUDED, ARTIFACTS_DIR
from DynamicPrompt.entity.config_entity import LoginCredentials
import pandas as pd
import os

class LoginToJira:
    def __init__(self):
        self.login_credentials = LoginCredentials()

    def Login(self)->bool:
        LOGIN(
            user=self.login_credentials.USERNAME,
            password = self.login_credentials.TOKEN,
            url=self.login_credentials.SERVER
        )
        load = LOGIN.get(endpoint.get_all_priorities())
        if load.status_code == 200:
            signal = True
            return signal
        else:
            signal = False
            return signal

class JiraOperattions:
    def __init__(self):
        self.login_status:bool = LoginToJira().Login()
    
    def get_metadata_of_story(self,story_id:str):
        self.story_id = story_id
        jql_query=f"""(issuekey = "{self.story_id}") ORDER BY created DESC"""
        if self.login_status==True:
            response = issue_export(jql = jql_query,folder=ARTIFACTS_DIR)
            #  include_fields = FIELDS_TO_BE_INCLUDED
        else:
            raise Exception("Not logged in to Jira")

class PromptOperations:
    def __init__(self,story_id) -> None:
        JiraOperattions().get_metadata_of_story(story_id=story_id)
        self.metadata_df = pd.read_csv(os.path.join(ARTIFACTS_DIR,'final_file.csv'))

    def generate_prompt(self):
        prompt = f"""
        You are an experienced functional tester and you have to write the detailed test cases for the below given user story, Also Each Test Case Should Contain Test Case Title, Test Case Steps or BDD Test Case Steps, and Expected Results.

        Title of the user story is:
        {self.metadata_df['Summary'][0]}

        Description is -
        {self.metadata_df['Description'][0]}

        The acceptance criteria is -
        {self.metadata_df['Custom field (Acceptance Criteria)'][0]}
        
        """
        return prompt
    