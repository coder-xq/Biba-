
bibas = []

#主体结构
class subject:
    def __init__(self,integrity,mode=""):
        self.integrity = integrity
        #mode有三种: low（低水标模型）,ring（环模型）,strict（严格完整性模型）
        self.mode = mode
        bibas.append(self)

    #read读操作
    def read(self,object):
        if self.mode=="ring":#环模型
           with open(object.name,'r',encoding='utf-8') as f: # ‘r’表示只读模式
                    contents = f.read() # 读取文件全部内容
                    print(contents)
        elif self.mode=="low":#低水标模型
            if self.integrity>object.integrity:
                self.integrity = object.integrity
            with open(object.name,'r',encoding='utf-8') as f: # ‘r’表示只读模式
                contents = f.read() # 读取文件全部内容
                print(contents)
            
        elif self.mode=="strict":#严格完整性模型
            if self.integrity<=object.integrity:
                with open(object.name,'r',encoding='utf-8') as f: # ‘r’表示只读模式
                    contents = f.read() # 读取文件全部内容
                    print(contents)
            else:
                print("无读权限！")
                
    #write写操作        
    def write(self,object):
        if self.integrity >= object.integrity:
            with open(object.name,'w',encoding='utf-8') as f: #  'w'表示写数据，写之前会清空文件中的原有数据！
                f.write(input("请输入要写入的内容："))
                print("write over")
        else:
            print("无写权限！")
            
    #excute执行操作        
    def excute(self,other):
        if self.integrity >= other.integrity:
            print("执行成功！")
        else:
            print("无执行权限！")
                  

#客体结构
class object:
    def __init__(self,integrity,name):
        self.integrity = integrity
        self.name=name
    


x=subject(5,"low")#主体x的完整性为5
y=subject(2,"low")#主体y的完整性为2
a=object(3,'a.txt')#客体a的完整性为3
x.read(a)
y.read(a)
print(x.integrity)
print(y.integrity)

x.write(a)
y.write(a)
x.excute(y)
y.excute(x)




#print(x.integrity)
#print(y.integrity)