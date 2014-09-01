.. _201012_php_best_practices:

Php最佳实践
==============================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2010/12/php_best_practices.html>`__

今天下午，我在读下面这篇文章。

虽然名字叫\ `《PHP最佳实践》 <http://www.odi.ch/prog/design/php/guide.php>`__\ ，但是它主要谈的不是编程规则，而是PHP应用程序的合理架构。

它提供了一种逻辑和数据分离的架构模式，属于\ `MVC模式 <http://www.ruanyifeng.com/blog/2007/11/mvc.html>`__\ 的一种实践。我觉得，这是很有参考价值的学习资料，类似的文章网上并不多，所以一边学习，一边就把它翻译了出来。

根据自己的理解，我总结了它的MVC模式的实现方式（详细解释见译文）：

    　　\* **视图层（View）**\ ：前端网页；

    　　\* **逻辑层（Controller）**\ ：先是页逻辑（Page
    Controller），负责处理页面请求；然后，调用业务逻辑（Business
    Controller），实现具体功能；

    　　\*
    **数据层（Model）**\ ：数据保存在数据库之中，上面有一个数据库抽象层，再上面则是一个”数据访问对象”（DAO），它生成”值对象”（Value
    Object）。业务逻辑通过DAO，操作值对象。


=======================================

**PHP最佳实践**

原载：\ `http://www.odi.ch/prog/design/php/guide.php <http://www.odi.ch/prog/design/php/guide.php>`__

译者：阮一峰

| 
| 
本文给出了PHP程序设计常见问题的解决方法，同时简单描述了PHP应用程序的架构。

**1. php.ini设置**

php.ini控制了解释器的行为，下面的一些设置保证了你的程序有最大的可移植性。

i. short\_open\_tag

设为0，即永远使用PHP的长标签形式：，不用短标签形式<?= “hello world” ?>。

ii. asp\_tags

设为0，不使用ASP标签<% echo “hello world”; %>。

iii. magic\_quotes\_gpc

建议在脚本中包含一个全局文件，负责在读取$\_GET、$\_POST、$\_COOKIE变量之前，首先检查这个设置是否打开，如果打开了，这对这些变量应用stripslashes函数。（注：该设置已经在PHP
5.3中被废除。）

iv. register\_globals

不要依赖这个设置，永远通过全局变量$\_GET、$\_POST、$\_COOKIE去读取GET、POST和COOKIE的值。为了方便起见，建议声明$PHP\_SELF
= $\_SERVER[‘PHP\_SELF’]。

v. file\_uploads

上传文件的最大大小，由下面的设置决定：

    　　\* file\_uploads必须设为1（默认值），表示允许上传。

    　　\*
    memory\_limit必须略大于post\_max\_size和upload\_max\_filesize。

    　　\*
    post\_max\_size和upload\_max\_filesize要足够大，能满足上传的需要。

**2. 配置文件（configuration file）**

你应该把与应用程序相关的所有配置，写在一个文件里。这样你就能很方便地适应开发环境的变化。配置文件通常包含以下信息：数据库参数、email地址、各类选项、debug和logging输出开关、应用程序常数。

**3. 名称空间（namespace）**

选择类和函数名的时候，必须很小心，避免出现重名。尽可能不要在类以外，放置全局性函数，类对内部的属性和方法，相当于有一层名称空间保护。如果你确实有必要声明全局性函数，那么使用一个前缀，比如dao\_factory()、
db\_getConnection()、text\_parseDate()等等。

**4. 数据库抽象层**

PHP不提供数据库操作的通用函数，每种数据库都有一套自己的函数。你不应该直接使用这些函数，否则一旦改用其他数据库（比如从MySQL
转为Oracle），你就有大麻烦了。而且，数据库抽象层通常比系统本身的数据库函数，更易用一些。

**5. “值对象”（Value Object, VO）**

值对象（VO）在形式上，就像C语言的struct结构。它是一个只包含属性、不包含任何方法（或只包含很少方法）的类。一个值对象，就对应一个实体。它的属性，通常应该与数据库的字段名保持相同。此外，还应该有一个ID属性。

    　　class Person {

    　　　　var $id, $first\_name, $last\_name, $email;

    　　}

**6. 数据访问对象（Data Access Object, DAO）**

数据访问对象（DAO）的作用，主要是将数据库访问与其他代码相隔离。DAO应该是可以叠加（stacked）的，这样就有利于将来你再添加数据库缓存。每一个值对象的类，都应该有自己的DAO。

    | 　　class PersonDAO {
    |  　　　　var $conn;

    | 　　　　function PersonDAO(&$conn) {
    |  　　　　　　$this->conn =& $conn;
    |  　　　　}


    | 　　　　function save(&$vo) { 　　　　　　if ($v->id == 0) {
    　　　　　　　　$this->insert($vo); 　　　　　　} else {
    　　　　　　　　$this->update($vo);
    |  　　　　　　}
    |  　　　　}

    | 　　　　function get($id) { 　　　　　　#execute select statement
    　　　　　　#create new vo and call getFromResult
    |  　　　　　　#return vo
    |  　　　　}

    | 　　　　function delete(&$vo) { 　　　　　　#execute delete
    statement
    |  　　　　　　#set id on vo to 0
    |  　　　　}

    　　　　#— private functions

    | 　　　　function getFromResult(&vo, $result) {
    |  　　　　　　#fill vo from the database result set
    |  　　　　}

    | 　　　　function update(&$vo) {
    |  　　　　　　#execute update statement here
    |  　　　　}

    | 　　　　function insert(&$vo) { 　　　　　　#generate id (from
    Oracle sequence or automatically) 　　　　　　#insert record into db
    　　　　　　#set id on vo
    |  　　　　}
    |  　　}

DAO通常应该部署以下方法：

    | 　　\* save：插入或更新一条记录
    |  　　\* get：取出一条记录
    |  　　\* delete：删除一条记录

你可以根据自己的需要，添加其他DAO方法，常见的例子有isUsed()、getTop($n)、find($criteria)。

但是，所有的DAO方法都应该与数据库操作有关，不应该执行其他操作。DAO只应该对一张表进行基本的select
/ insert /
update，不应该包含业务逻辑。举例来说，PersonDAO就不应该包含向某人发送Email的代码。

你可以写一个工厂函数，根据不同的类名，返回相应的DAO。

    　　function dao\_getDAO($vo\_class) {

    　　　　$conn = db\_conn(‘default’); #get a connection from the pool

    　　　　switch ($vo\_class) {

    　　　　　　case “person”: return new PersonDAO($conn);

    　　　　　　case “newsletter”: return new NewsletterDAO($conn);

    　　　　　　…

    　　　　}

    | 　　}

**7. 自动生成代码**

99%的值对象和DAO代码，可以根据数据库模式（schema）自动生成，前提是你的表和列使用约定的方式进行命名。如果你修改数据库模式，一个自动生成代码的脚本将大大节省你的时间。

**8. 业务逻辑**

业务逻辑直接反映使用者的需要。它们处理值对象，根据业务需要修改值对象的属性，使用DAO与数据库层交互。

    | 　　class NewsletterLogic { 　　　　function NewsletterLogic() {
    |  　　　　　　…
    |  　　　　}

    | 　　　　function subscribePerson(&$person) {
    |  　　　　　　…
    |  　　　　}

    | 　　　　function unsubscribePerson(&$person) {
    |  　　　　　　…
    |  　　　　}

    | 　　　　function sendNewsletter(&$newsletter) { 　　　　　　…
    　　　　}
    |  　　}

**9. 页逻辑（控制器）**

当一个网页被请求时，页控制器（page
controller）就会运行，然后产生输出。控制器的任务，就是将HTTP请求转化成业务对象（business
object），然后调用相应的业务逻辑，最后生成一个”展示输出”的对象。

页逻辑依次执行以下步骤（请参照后面的PageController类的代码）：

    　　i. 假定页面请求之中，包含一个cmd参数。

    　　ii. 根据cmd参数的值，执行相应的动作。

    　　iii. 验证页面返回的值，生成一个值对象。

    　　iv. 针对值对象，执行业务逻辑。

    　　v. 如果有必要，可以导向另一个页面。

    　　vi. 收集必要的数据，输出结果。

注意：可以编写一个工具函数（utility
function），处理GET或POST值，当有的变量没有赋值时，提供一个默认值。页逻辑不包含HTML代码。

    | 　　class PageController {
    |  　　　　var $person; #$person is used by the HTML page
    |  　　　　var $errs;

    | 　　　　function PageController() { 　　　　　　$action =
    Form::getParameter(‘cmd’);
    |  　　　　　　$this->person = new Person();
    |  　　　　　　$this->errs = array();


    | 　　　　　　if ($action == ‘save’) {
    |  　　　　　　　　$this->parseForm();
    |  　　　　　　　　if (!this->validate()) return;

    　　　　　　　　NewsletterLogic::subscribe($this->person);

    | 　　　　　　　　header(‘Location: confirmation.php’);
    　　　　　　　　exit;
    |  　　　　　　}
    |  　　　　}

    | 　　　　function parseForm() { 　　　　　　$this->person->name =
    Form::getParameter(‘name’); 　　　　　　$this->person->birthdate =
    Util::parseDate(Form::getParameter(‘birthdate’);
    |  　　　　　　…
    |  　　　　}

    | 　　　　function validate() { 　　　　　　if ($this->person->name
    | 　　　　function validate() { 　　　　　　if ($this->person->name
    == ”) $this->errs[‘name’] = FORM\_MISSING;
    　　　　　　#FORM\_MISSING is a constant 　　　　　　…
    　　　　　　#FORM\_MISSING is a constant 　　　　　　…
    　　　　　　return (sizeof($this->errs) == 0);
    |  　　　　}
    |  　　}

**10. 表现层（Presentation Layer）**

最顶层的页面包含实际的HTML代码。这个页面需要的所有业务对象（business
object），由页逻辑提供。

这个页面先读取业务对象的属性，然后将它们转换成HTML格式。

    | 　　 　　　　$c =& new PageController();
    |  　　?>

    　　

    　　

    　　

    ” method=”POST”> 　　　　 　　　　person->name); ?>”> 　　　　

    Subscribe

    　　

    | 
    |  　　

    | 
    |  　　

**11. 本地化（Localization）**

本地化意味着要支持多种语言，这个比较麻烦，你无非有两种方法可以选择：

    　　A) 准备多重页面。

    　　B) HTML页面中去除特定语言相关的内容。

一般来说，A方法用得比较多，因为B方法会使得HTML页面的可读性很差。

所以，你可以先写完一种语言的页面，然后把它们进行拷贝，用某种命名法区别不同语言的版本，比如index\_fr.php表示index.php的法语版。

为了保存用户的语言选择，你有几种方法：

    　　A) 将语言设定保存在一个session变量或cookie之中；

    　　B) 从HTTP头中读取locale值；

    　　C) 把语言设定作为一个参数，追加在每个URL后面。

看上去A方法比C方法容易得多（虽然session和cookie都有过期的问题），而B方法只能作为A或C的补充。

最后不要忘了，数据库中的字段也必须进行本地化。

**12. 安装位置**

有时候你需要知道程序的根目录在哪里，但是$\_SERVER[‘DOCUMENT\_ROOT’]只是web服务器的根目录，如果你的程序安装在它的某个子目录之中，PHP没法自动知道。

你可以定义一个全局变量$ROOT，它的值就是程序的根目录，然后把它包含在每一个脚本文件中。那么，你要包含某个文件，就这样写require\_once(“$ROOT/lib/base.inc.php”);。

**13. 目录结构**

首先，每个类都应该有自己的独立文件，还必须有一套文件名的命名规则（naming
convention）。

软件的目录结构可以采用如下形式：

    　　/ 根目录。浏览器从这个页面开始访问。

    　　/lib/ 包含全局变量（base.inc.php）和配置文件（config.inc.php）。

    　　/lib/common/ 包含其他项目也可以共用的库，比如数据库抽象层。

    　　/lib/model/ 包含值对象类。

    　　/lib/dao/ 包含数据访问对象（DAO）类，以及DAO工厂函数。

    　　/lib/logic/ 包含业务逻辑类。

    　　/parts/ 包含HTML模板文件。

    　　/control/
    包含页逻辑。对于大型程序来说，这个目录下面可能还有子目录（比如admin/,
    /pub/）。

base.inc.php文件中，应该按照以下顺序添加包含文件：

    　　\* /lib/common之中经常使用的类（比如数据库层）。

    　　\* 配置文件；

    　　\* /lib/model之中所有类；

    　　\* /lib/dao的之中所有类。

至于那些存放图片、上传文件的目录，这里就省略了。

| （完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2010/12/php_best_practices.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com