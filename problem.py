# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import enum
import uuid


class IssueType(enum):
    A = "A"
    B = "B"
    C = "C"

class Agent:
    
    def __init__(self, agent_id:str , agent_name: str, agent_expertise: IssueType, agent_issues: [], agent_solved_issue: []):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.agent_expertise= agent_expertise
        self.agent_issues = agent_issues
        self.agent_solved_issue = agent_solved_issue
        self.total_time = 0
        
    @property
    def last_pending_issue(self):
        return self.agent_issues[-1]
    @property
    def pending_issues(self):
        return self.agent_issues
        
    @property
    def completed_issue_count(self):
        return len(self.agent_solved_issue)
    @property    
    def agent_expertise(self):
        return self.agent_expertise
    
    def agent_total_time_required(self, time):
        self.total_time += time

class Priority(enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    
        
class Issue:
    
    def __init__(self, issue_id:str , issue_type: IssueType, assgined_to: None, is_resolved: bool, priority: Priority, time_required = 24):
        self.issue_id = issue_id
        self.issue_type = issue_type
        self.assgined_to = assgined_to
        self.is_resolved = is_resolved
        self.priority = priority
        self.time_required = time_required
        
    @property    
    def issue_assgined_to(self):
        return self.assgined_to
    
    @property
    def issue_type(self):
        return self.issue_type
    
    @property
    def priority(self):
        return self.priority
    
    


class CISR:
    
    def __init__(self):
        self.agents = {}
        self.issues = {}
        self.total_issue_created = 0
        
    
    def assign_the_issue(self, issue):
        if not self.agents:
            return "there must be agent to assign the issue"
        
        issue_type = issue.issue_type
        agents = self.agent[issue_type]
        agents_with_minimum_issue = agents[0]
        
        if issue.priority == Priority.HIGH:
            
            for i in range(agents):
                if agents_with_minimum_issue.agent_total_time_required > agents[i].agent_total_time_required:
                    
                    agents_with_minimum_issue = agents[i]
                    
            agents_with_minimum_issue.agent_issues.append(issue)
            issue.assigned_to = agents_with_minimum_issue
    
        return issue.assigned_to
    def mark_resolve(self, issue):
        agent = issue.assigned_to
        issue.is_resolved = True
        
    

class Display:
    
    def __init__(self):
        self.total_solved_count = 0
        self.total_pending_count = 0
    
    @classmethod
    def display_pending_count(cls):
        return cls.total_pending_count
    
    @classmethod
    def total_solved_count(cls):
        return cls.total_solved_count
        
        
        
        
def main():
    ticketing_system = CISR()
    
    numberofagents = int(input())
    
    while numberofagents >0 :
        agent_id = uuid.uuid1()
        agent_name = str(input("Agent name"))
        agent_expertise = IssueType(input ("Expertise"))
        numberofagents -= 1
        agent = Agent(agent_id= agent_id , agent_name= agent_name, agent_expertise= agent_expertise)
        
        ticketing_system.agents[agent_expertise].append(agent)
    
    issue = Issue(issue_id=uuid.uuid1() , issue_type= IssueType.A, assgined_to= None, is_resolved= False, priority= Priority.HIGH, time_required = 3)
    
    ticketing_system.issue[issue.issue_id] = issue
    
    assigned = ticketing_system.assign_the_issue(issue = issue)
    
    
    
   
    







    
    
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        