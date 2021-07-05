
class Question:
    
    def __init__(self, question):
        self._question = question
     
    def get_question(self):
         return self._question  
    def get_answer(self):
         return self._answer

    def set_answer(self,answer):
        self._answer = answer 
    def set_question(self, question):
        self._question = question   
    
    _question=str 
    _answer=False
