import streamlit as st
import pandas as pd
from PIL import Image

sidebar = st.sidebar.radio(
    "导航栏",
    ("HOMEPAGE", "个人简历", "试驾心得")
)
if sidebar == "HOMEPAGE":
		st.header("本网页用python语言调用streamlit框架制作")
		st.subheader("数字化时代")
		image  = Image.open('/Users/watermelon/PycharmProjects/pythonStreamlit/网络时代.jpeg')
		image1 = Image.open('/Users/watermelon/PycharmProjects/pythonStreamlit/网络时代1.jpeg')
		st.image(image)
		st.image(image1)

elif sidebar == "个人简历":
		st.title("求职简历")
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
				'2021.11-至今|北京凌云雀科技有限公司|软件测试工程师(实习)': ['隶属中间件测试团队，\
				负责RabbitMQ和MySQL PXC组件。', '根据需求文档编写测试用例，执行回归测试并编写测试报告。', \
				'对产品进行相关的页面测试，接口自动化测试，性能测试以及稳定性测试等。', '发现产品缺陷，与研发团队进行有效沟通，\
				对产品缺陷进行跟踪、分析、解决。']})
		st.table(internship)

		st.subheader("实践经历")
		practice = pd.DataFrame({
				'2020.7-2021.7|类似weibo的Web应用|自主开发': ['为实现此页面，选择 Rails技术栈，从前端H5，业务逻辑Ruby，\
				数据库SQL能完整贯通起来。', '理解了MVC架构，学会了Linux命令行操作、Vi编辑器以及Github版本工具。', \
				'通过项目学习，总结出发现问题-分析问题-解决问题-复盘总结的学习方法。'], 
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
elif sidebar == "试驾心得":
		st.title("理想汽车试驾感受")
		st.subheader("一、整体感受")
		st.write("1.驾驶感觉很不错，车体很平稳，提速也很快很流畅，使用的都是电机所以没有提速的顿挫感。")
		st.write("2.副驾体验是最棒的，显示屏可以看剧、刷视频、K歌，座椅按摩通风加热，体验感很惬意。")
		st.write("3.后排的感受是休息，空间很宽敞，腿部和头部的距离都很大，同样有加热和按摩，适合休息。")
		st.write("4.后备箱的空间也是相当大的，第三排座椅放倒相当于一张床，很适合野餐；放起来也有一定空间。")
		st.write("5.最满意的就是理想one是一台油电混合的车，既满足了用电省钱，还没有丢掉油车的动力。")
		st.subheader("二、期待改进")
		st.write("1.电池容量增大，增加续航能力，增加充电的速度。")
		st.write("2.理想同学的智能性也很好，但有时会卡顿。")
		st.write("3.可以给后排座椅也加上通风功能。")