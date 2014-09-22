.. _articles11:

PHP v5.3的新鲜玩意
==================

2009年3月2日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

PHP v5.3马上就要release了，这里让我们看看他有一些什么样的新特性。

**1）\_callStatic() magic 方法**

::

    class Foo
    {
        public static function __callStatic( $name, $args )
        {
            echo "Called method $name statically";
        } 

        public function __call( $name, $args )
        {
            echo "Called method $name";
        }
    }

::

    Foo::dog();       // outputs "Called method dog statically"
    $foo = new Foo;
    $foo->dog();      // outputs "Called method dog"

**2）\ ``动态调用函数``**

::

    class Dog
    {
        public function bark()
        {
            echo "Woof!";
        }
    } 

    $class = "Dog"
    $action = "bark";
    $x = new $class(); // instantiates the class "Dog"
    $x->$action();     // outputs "Woof!" 

**3) 标准**\ **PHP**\ **库（SPL）**

加了了少数几个容器类，比如，栈（SplStack）和固定数组（SplFixedArray）

::

    $stack = new SplStack(); 

    // push a few new items on the stack
    $stack->push("a");
    $stack->push("b");
    $stack->push("c"); 

    // see how many items are on the stack
    echo count($stack); // returns 3 

    // iterate over the items in the stack
    foreach ( $stack as $item )
        echo "[$item],";
    // the above outputs: 1

     [/c],[b],[a]  // pop an item off the stack echo $stack->pop(); // returns "c"   // now see how many items are on the stack echo count($stack); // returns 2

**4) Closures 功能**

关于Closures，这是一个把函数定义成变量的玩意。让我们看几个例子：

示例一：

::

    $string = "Hello World!";
    $closure = function() use ($string) { echo $string; };

    $closure();

| **Output:**
|  Hello World!
|  示例二 使用引用的变量

::

    $x = 1
    $closure = function() use (&$x) { ++$x; }

    echo $x . "\\n";
    $closure();
    echo $x . "\\n";
    $closure();
    echo $x . "\\n";

| **Output**: 1 2
|  3
|  示例三，返回值

::

    function getAppender($baseString)
    {
          return function($appendString) use ($baseString)
      { return $baseString .$appendString; };
    }

示例四，Reflection

::

    class Counter
    {
          private $x;

          public function __construct()
          {
               $this->x = 0;
          }

          public function increment()
          {
               $this->x++;
          }

          public function currentValue()
          {
               echo $this->x . "\\n";
          }
    }
    $class = new ReflectionClass("Counter");
    $method = $class->getMethod("currentValue");
    $closure = $method->getClosure()
    $closure();
    $class->increment();
    $closure();

| **Output**: 0
|  1
|  示例五，Reflection API

::

    $closure = function ($x, $y = 1) {};
    $m = new ReflectionMethod($closure);
    Reflection::export ($m);
    Output:
    Method [  public method __invoke ] {
      - Parameters [2] {
        Parameter #0 [  $x ]
        Parameter #1 [  $y ]
      }
    }

示例六，Uses Case

::

    $logdb = function ($string) { Logger::log("debug","database",$string);};
    $db = mysqli_connect("server","user","pass");
    $logdb("Connected to database");
    $db->query("insert into parts (part, description) values
     ("Hammer","Pounds nails");
    $logdb("Insert Hammer into to parts table");
    $db->query("insert into parts (part, description) values
           ("Drill","Puts holes in wood");
    $logdb("Insert Drill into to parts table");
    $db->query("insert into parts (part, description) values
     ("Saw","Cuts wood");
    $logdb("Insert Saw into to parts table");

更为详细的文章，请参考这里，\ `链接 <http://www.ibm.com/developerworks/opensource/library/os-php-5.3new2/index.html>`__\ 。

**5) 使用namespace**

新版的PHP会开始支持C++式的namespace，请参看示例：

示例一

::

    /* Foo.php */
    <?php
    namespace Foo;
    function bar()
    {
        echo "calling bar....";
    }
    ?> 

    /* File1.php */
    <?php
    include "./Foo.php";
    Foo/bar(); // outputs "calling bar....";
    ?> 

    /* File2.php */
    <?php
    include "./Foo.php";
    use Foo as ns;
    ns/bar(); // outputs "calling bar....";
    ?> 

    /* File3.php */
    <?php
    include "./Foo.php";
    use Foo;
    bar(); // outputs "calling bar....";
    ?>

示例二，多重namespace

::

     <?php
    namespace Foo;
    class Test {} 

    namespace Bar;
    class Test {} 

    $a = new Foo\\Test;
    $b = new Bar\\Test; 

    var_dump($a, $b); 

    Output:
    object(Foo\\Test)#1 (0) {
    }
    object(Bar\\Test)#2 (0) {
    }
    Output:
    object(Foo\\Test)#1 (0) { }
    object(Bar\\Test)#2 (0) { }

示例三，不同文件中的namespace

::

    /*定义*/
    /* global.php */
    <?php
    function hello()
    {
        echo "hello from the global scope!";
    }
    ?> 

    /* Foo.php */
    <?php
    namespace Foo;
    function hello()
    {
        echo "hello from the Foo namespace!";
    }
    ?> 

    /* Foo_Bar.php */
    <?php
    namespace Foo/Bar;
    function hello()
    {
        echo "hello from the Foo/Bar namespace!";
    }
    ?>


    /*使用 */
    <?php
    include "./global.php";
    include "./Foo.php";
    include "./Foo_Bar.php";

    use Foo; 

    hello();         // outputs "hello from the Foo namespace!"
    Bar\\hello();   // outputs "hello from the Foo/Bar namespace!"
    \\hello();       // outputs "hello from the global scope!"
    ?>

更为详细的文章，请参考这里，\ `链接 <http://www.ibm.com/developerworks/opensource/library/os-php-5.3new3/index.html>`__\ 。

**6)开始支持Achieve包**

正像JAR一样，PHP也要开始支持自己的Achieve包了，叫作，Phar。PHP提供了一整套函数来帮助开发人员创建和使用Phar，正如下面的示例所示：

**创建**\ ：

::

    $p = new Phar("/path/to/my.phar",
     CURRENT_AS_FILEINFO | KEY_AS_FILENAME, "my.phar");
    $p->startBuffering();

**创建文件存根**\ （stub）

::

    $p->setStub("");

**加入文件**\ ：

::

    $p["file.txt"] = "This is a text file";
    $p["index.php"] = file_get_contents("index.php");
    $p["big.txt"] = "This is a big text file";
    $p["big.txt"]->setCompressedBZIP2();
    //加入某目录下所有的文件
    $p->buildFromDirectory("/path/to/files","./\\.php$/");

**使用Phar**

::

    include "myphar.phar";
    include "phar://myphar.phar/file.php";

更为详细的文章，请参考这里，\ `链接 <http://www.ibm.com/developerworks/opensource/library/os-php-5.3new4/index.html>`__\ 。

.. |image| image:: /coolshell/static/20140920235230069000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/11.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com