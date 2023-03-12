#----打开数据库-----
from py2neo import Node, Relationship, Graph, NodeMatcher, RelationshipMatcher,Subgraph
graph = Graph("http://localhost:7474/", auth=("neo4j", "替换为你的密码"))


#----删除所有内容-----
graph.delete_all()
