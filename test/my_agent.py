cat <<EOF > test/my_agent.py
class MyAgent:

  def query_none(self):
    return None

  def query_list(self):
    return [1, 2, 3]

  def register_operations(self):
    return {
        "": ["query_none", "query_list"],
    }

agent = MyAgent()
EOF
