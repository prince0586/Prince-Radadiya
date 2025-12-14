class Memory:
    def __init__(self):
        self.logs = []
        self.knowledge_base = {}

    def add_log(self, message):
        self.logs.append(message)

    def store_finding(self, topic, content):
        self.knowledge_base[topic] = content

    def get_context(self):
        context = "Current Knowledge:\n"
        for topic, content in self.knowledge_base.items():
            context += f"- {topic}: {content[:200]}... \n"
        return context

    def get_full_report(self):
        return self.knowledge_base