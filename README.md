# back-nebula

一个轻量级的实时数据处理后端服务。

### 安装

确保已安装 Python 3.7+，通过 pip 安装依赖：

```bash
pip install -r requirements.txt
```

### 使用示例

在项目中引入并启动服务：

```python
from backnebula import NebulaServer

# 初始化服务器
server = NebulaServer(host='0.0.0.0', port=8080)

# 启动服务
server.run()
```

运行测试以验证功能：

```bash
python test_backnebula.py
```

### 许可证

本项目采用 MIT 许可证。详见 LICENSE 文件。



