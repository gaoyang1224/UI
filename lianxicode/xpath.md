1.//input[@name='']
2.and组合
3.//div/input
4.//div//input
5.儿子找父亲 ..
6.文本 //a[text()='']
7.contains,用于文本有空格的情况    //a[contains(text(),'')]      //a[contains(@class,'')]
8.索引，要加括号，从1开始    (//a[contains(text(),"体育")])[1]
9.轴  following-sibling选取当前节点之后的所有同级节点
      preceding-sibling选取当前节点之前的所有同级节点
      ancestor选取当前节点所有先辈     (//a[contains(text(),"体育")])//ancestor::td[@align='left']
10. *   //*[id='']
      
11.八大元素定位
id
name
class
xpath
css
link
partial
tagname

12.等待
强制等待，硬性等待 time.sleep
智能等待，隐形等待，只能等待元素，只要设置一次
显性等待