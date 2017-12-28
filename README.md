# Learning Python with PyCharm
Learn Python programming with PyCharm, the cross-platform IDE that "takes care of the routine." 
Explore PyCharm's first-rate text editing tools. 
Learn how to improve your code quality with Lens Mode and Intentions, refactor and debug code, and perform unit testing with the PyCharm test runner. 
Then dive into working with SQL databases. Lastly, learn how to integrate Python with web projects that include HTML and JavaScript.

### Topics include:
- Adding functions<br/>
- Refactoring code<br/>
- Calling packages<br/>
- Debugging code<br/>
- Creating databases<br/>
- Working with in-line SQL<br/>
- Creating web projects with PyCharm<br/>

### Src: https://www.lynda.com/Python-tutorials/Learning-Python-PyCharm/590828-2.html

### NOTE: due to following error use 'html.parser' instead of 'html5lib'<br/>
```
Traceback (most recent call last):
  File "C:/Users/superadmin/PycharmProjects/Learning_Python_With_PyCharm/PageSpider/page_spider.py", line 28, in <module>
    main(database=database_file, url_list_file=input_file)
  File "C:/Users/superadmin/PycharmProjects/Learning_Python_With_PyCharm/PageSpider/page_spider.py", line 17, in main
    words = url_utilities.scrape_page(page_content)
  File "C:\Users\superadmin\PycharmProjects\Learning_Python_With_PyCharm\PageSpider\utilities\url_utilities.py", line 40, in scrape_page
    chicken_noodle = BeautifulSoup(page_contents, "html5lib")
  File "C:\Users\superadmin\venv\PageSpider\lib\site-packages\bs4\__init__.py", line 165, in __init__
    % ",".join(features))
bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: html5lib. Do you need to install a parser library?
```
