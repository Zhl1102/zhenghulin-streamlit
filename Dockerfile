# 声明Docker镜像使用python3.9.10
FROM python:3.9.10
#RUN apt-get update && apt-get install -y curl

# 设置镜像使用腾讯云pip源，提高安装速度
RUN pip config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple

# 开放镜像内8501端口,用于Streamlit请求访问
EXPOSE 8501

# 设置镜像的工作空间为/app，并复制项目文件进去
RUN mkdir -p /app

WORKDIR /app
ADD  . /app
RUN pip install -r requirements.txt

# 设置启动Streamlit的执行命令
CMD [ "streamlit","run","main.py"]
