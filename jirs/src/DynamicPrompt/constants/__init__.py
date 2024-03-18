import os
from datetime import datetime

## Login Credentils

SERVER = "https://assetmark.atlassian.net"
USERNAME = "paritosh.sharma@assetmark.com"

## Jira Export Constants
FIELDS_TO_BE_INCLUDED = ['Summary','Description','Custom field (Acceptance Criteria)']

## Commaon Constants
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR = os.path.join("artifacts", TIMESTAMP)