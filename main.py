from app_maker import AppMaker, Page


home = Page(title="Home", path="/")
page_2 = Page(title="Page 2", path="/page-2")
page_3 = Page(title="Pedro", path="/pedro")

app = AppMaker(pages=[home, page_2, page_3])
