# ReTCP
通过TCP握手欺骗，来绕过SNI RST导致维基百科、Pixiv等站点无法访问的工具。

此方案 非域前置 不破坏SNI，无需证书，不对HTTPS进行任何损坏，支持所有站点。 

目前为demo 版本，需自行先行解决DNS污染，运行时对全局TCP握手流量都会进行注入。

## 使用
### 如果已经安装了Python 3.*或更高版本

1. 先安装依赖：pydivert

```
pip install pydivert
```

2. 对于Windows系统，需 [ 管理员权限 ] 使用通过如下命令启动：

```
python ./retcp.py
```


## 实现原理
本方案为论文 https://geneva.cs.umd.edu/papers/geneva_ccs19.pdf 中 TCB Desynchronization 绕过策略的Python代码实现。

本方案适用网站更宽广，能够直接绕过所有对于TCP req的RST规则，所以也无需修改破坏SNI即可与目标服务器直连。
