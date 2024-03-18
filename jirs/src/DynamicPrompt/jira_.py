from jiraone import LOGIN, issue_export, endpoint
from jira import JIRA
import base64
from dataclasses import dataclass


class JiraOperations:
    def __init__(self, issue_id:str, jql_query: str, token:str)-> None:
        self.jiraOptions = {'server': "https://assetmark.atlassian.net"}
        self.username = "paritosh.sharma@assetmark.com"
        self.password = token
        self.issue_id = issue_id
        self.jql_query = jql_query

    def login(self):
        LOGIN(
            user=self.username,
            password = self.password,
            url=self.jiraOptions['server']
        )
        load = LOGIN.get(endpoint.get_all_priorities())
        if load.status_code == 200:
             # some expression here
            print("Login Sucessfull !!")

    def get_jira_client(self):
        jira_client = JIRA(
            options = self.jiraOptions,
            basic_auth = (
                self.username,
                self.password
            )
        )
        return jira_client
    
    def get_result_using_jiraone(self):
        self.login()
        response = issue_export(jql = self.jql_query)
        return response

    def get_result_jira(self)->None:
        response = self.get_jira_client().issue(self.issue_id)
        return response 

    def get_token(self):
        credentials = f"{self.username}:{self.password}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        return encoded_credentials
    

@dataclass
class LoginCredentials:
    USERNAME:str
    TOKEN:str
    SERVER:str




token = ""

obj = JiraOperations(issue_id="DS-4",
                     jql_query="""project = "TMS" and (text ~ "TMS-84" or issuekey = "TMS-84")
ORDER BY created DESC""",
                     token = token)
# print(obj.get_result_jira())

print(obj.get_result_using_jiraone())









# # import the installed Jira library 
# from jira import JIRA 

# # Specify a server key. It is your domain 
# # name link. 
# jiraOptions = {'server': "https://paritosh-sharma.atlassian.net"} 

# # Get a JIRA client instance, Pass 
# # Authentication parameters 
# # and Server name. 
# # emailID = your emailID 
# # token = token you receive after registration 
# jira_ = JIRA(options = jiraOptions, 
# 			basic_auth = ("prxxxxxxh@gmail.com", 
# 						"bj9xxxxxxxxxxxxxxxxxxx5A")) 

# # While fetching details of a single issue, 
# # pass its UniqueID or Key. 
# singleIssue = jira_.issue(issue_id) 
# print('{}: {}:{}'.format(singleIssue.key, 
# 						singleIssue.fields.summary, 
# 						singleIssue.fields.reporter.displayName)) 