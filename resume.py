import streamlit as st
import pandas as pd
from PIL import Image

sidebar = st.sidebar.radio(
    "导航栏",
    ("个人简历", "试驾心得")
)

if sidebar == "个人简历":
		st.title("个人简历")
		image = Image.open('/Users/watermelon/PycharmProjects/pythonStreamlit/证件照.jpeg')
		st.image(image, width=100)
		st.write("---------------------------------")
		st.subheader("个人简介")
		personal_info = pd.DataFrame({
				'姓名': ['郑虎林'],
				'电话': ['18847339790'],
				'邮箱': ['1533938229@qq.com'],
				'Github': ['https://github.com/Zhl1102'],
				'意向职位': ['测试开发工程师']
		})
		st.table(personal_info)

		st.subheader("专业技能")
		st.write("掌握Python编程语言，熟悉RabbitMQ、MySQL(PXC)数据库，Linux操作系统及命令行基本操作，"\
						"了解Docker和K8S知识和基本操作，有良好的代码设计编写和调试代码的能力。")

		st.subheader("实习经历")
		internship = pd.DataFrame({
				'2021.11-至今|玛蒂尔德(北京)科技有限公司|测试开发': ['隶属中间件测试团队，\
				负责RabbitMQ和MySQL PXC组件', '负责页面测试，接口自动化测试，性能测试及稳定性测试。', '熟悉Docker和K8S，编写简单python脚本。']})
		st.table(internship)

		st.subheader("实践经历")
		practice = pd.DataFrame({
				'2020.7-2021.7|类似weibo的Web应用|自主开发': ['目的是将所学知识融会贯通，\
				通过分析发现Rails技术栈，可以完美实现各方面的学习。', '理解了MVC架构，学会了Linux\
				命令行操作、Vi编辑器以及Github版本工具。', '通过项目学习，总结出发现问题-分析问题-解决问题-复盘总结的学习方法。'], 
				})
		practice1 = pd.DataFrame({
				'2021.09-2021.10|Python爬虫|数据爬取': ['首先研究爬虫方案，搭建以Python和Selenium测试工具为主的环境。', \
				'抓取富途牛牛网页中财报模块的网页数据。', '将所爬取的数据写入到CSV文件中。']
		})
		st.table(practice)
		st.table(practice1)

		st.subheader("教育背景")
		edu = pd.DataFrame({
				'时间': ['2020.09-2022.07', '2017.09-2020.07'],
				'学校': ['山东科技大学泰山科技学院', '山东圣翰财贸职业学院'],
				'专业': ['计算机科学与技术', '计算机应用技术']})
		st.table(edu)

		st.subheader("自我评价")
		st.write("本人热爱计算机，具有良好的代码编程习惯，有独立思考、持续学习和解决问题的能力，\
							善于倾听和团队合作。我坚信终身学习的理念可以让我一生受益，每一次尝试都是我不断\
							完善自己的机会，对计算机强烈的兴趣驱动着我不断深入学习。")

		st.balloons()