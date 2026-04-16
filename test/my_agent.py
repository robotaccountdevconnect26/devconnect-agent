class MyAgent:

  def query_none(self):
    return None

  def query_list(self):
    return "I have been suceessfully deployed from a GitHub Repository!"

  def register_operations(self):
    return {
        "": ["query_none", "query_list"],
    }

agent = MyAgent()
