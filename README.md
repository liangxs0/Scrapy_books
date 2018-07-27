# Scrapy_books
基于scrapy框架写的一个爬取"http://books.toscrapc.com/"中书的书名以及价格，将信息保存到.csv格式的文档中去。

创建工程

```python
scrapy startproject toscrape_book
```

指定工程等的爬去网页

```python
cd topscrape_book
scrapy genspider books books.topscrapy.com
```

源码中包括数据的获取和数据的处理以及piplines的开启操作，最终完成对数据的处理和插入表格的操作，代码的执行可以使用命令行执行：

```python
scrapy crawl books -o books.csv
```

也可以在工程的同级目录下创建以一个python文件调用cmdline的模块：

```python
	from scrapy import cmdlines
    cmdline.extract('scrapy crawl books -o books.csv'.spilt())
```



