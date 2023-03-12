#----打开数据库-----
from py2neo import Node, Relationship, Graph, NodeMatcher, RelationshipMatcher,Subgraph
graph = Graph("http://localhost:7474/", auth=("neo4j", "替换为你的密码"))


path = r"C:\Users\DELL\data\5501-6000_input_pre_5元组.csv"

file = open(path,'r',encoding = 'utf-8').readlines()


con = list()
zh = ['病名','病症','其它','药名','诊断方案','治疗方案','包含','治疗','危险因素','辅助诊断','特征','并发','别名','作用','条件','诊断']
for j in file:
    try:
        a = j.replace("\t","").strip('\n').split(",")
        # a = [eval(i) for i in a] #引号里面有引号-两对引号
        a = [i for i in a] #只有一对引号
        
        if (a[1] not in zh) or (a[2] not in zh) or (a[3] not in zh):
            continue
        #['甲状腺功能亢', '病名', '治疗', '其它', 'HCV感染患者']
        con.append(a)
    except:
        continue
    # print(a)


for j in con:
    
    try:
        selector = NodeMatcher(graph) #创建图，实质上为句柄
        # ---创建头实体节点---
        entity1 = selector.match(j[1], name = j[0]) #检索是否存在头实体节点
        if len(list(entity1)) == 0: #不存在头实体节点，则创建头实体
            entity1_node = Node(j[1], name = j[0])
            graph.create(entity1_node) #创建头实体
        else: #存在头实体节点，跳过
            pass

        # ---创建尾实体节点---
        entity3 = selector.match(j[3], name = j[4])
        if len(list(entity3)) == 0: #不存在尾实体节点，则创建
            entity3_node = Node(j[3], name = j[4])
            graph.create(entity3_node)
        
        
        else: #存在节点，跳过
            pass

        #将两虚点建立关系
        e1_node = graph.nodes.match(j[1], name = j[0]).first()
        e2_node = graph.nodes.match(j[3], name = j[4]).first()
        e12 = Relationship(e1_node, j[2], e2_node)
        graph.create(e12)
    except:
        continue

print("ok1")
