#pydantic schema
from enum import Enum 
class FlairEnum(str,Enum):
    bug = 'bug'
    feature = 'feature'
    question = 'question'
    docs =  'docs'