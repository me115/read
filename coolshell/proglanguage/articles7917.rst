.. _articles7917:

各式各样的验证码
================

2012年7月19日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

还记得以前那篇《\ `超强验证码 <http://coolshell.cn/articles/3277.html>`__\ 》？其实这个世界变态的验证码还有很多，下面是一个列表向像展示了各种稀奇古怪的验证码。不过本文并不单单只是收集这验证码，前面的比较恶搞，后面的会向你展示什么是有accessibility验证码。

完全看不清楚的
^^^^^^^^^^^^^^

这是人类的字符吗？

|image0|

图案中的字母是什么？

|image1|

这也够奇葩的了。

|image2|

看得清但令人抓狂的
^^^^^^^^^^^^^^^^^^

|image3|\ |image4|

数学公式的
^^^^^^^^^^

如果你填对了，你是人类吗？

`
|image5| <http://coolshell.cn//wp-content/uploads/2012/07/4.jpg>`__

|image6|

智力题
^^^^^^

|image7|

|image8|

|image9|

你的审美水平正常吗？
^^^^^^^^^^^^^^^^^^^^

|image10|

你懂盲文吗？
^^^^^^^^^^^^

|image11|

ASCII图片式
^^^^^^^^^^^

|image12|

怎么验证一个人是否成年
^^^^^^^^^^^^^^^^^^^^^^

|image13|

3D验证码
^^^^^^^^

通个这个脚本自动生成的：\ `http://ocr-research.org.ua/tb/getimage.php5 <http://ocr-research.org.ua/tb/getimage.php5>`__

|http://ocr-research.org.ua/tb/getimage.php5|

reCaptcha
^^^^^^^^^

相信大家都知道reCAPTCHA下了一盘很大的棋，它让你在输验证码的时候还帮着还原书籍中那些很难被OCR识别的单词。其有两组验证码，一组是可以被电脑识别的，另一组是不能被电脑识别的（也就是让人来帮电脑识别的），如果你第一组答对了，就会被
认为是人工操作，于是你回答的第二组就会成为人肉OCR。

|image15|

它最近又将增加一项新功能：显示Google地图上的街景地址和名称。这样从地图上的街景中提取街道地址和名称以及交通标志等数据，以完善Google地图上的信息。

|image16|

Facebook的人脸识别验证码
^^^^^^^^^^^^^^^^^^^^^^^^

你觉得有创意吗?

|image17|

`微软的ASIRRA <http://research.microsoft.com/en-us/um/redmond/projects/asirra/>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|image18|

`DISTCHA <http://accessibiliteweb.com/stuff/captcha-slider.html>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

通过像iPhone/iPad开启时滑动的样式来验证。

|image19|

`MotionCAPTCHA <http://josscrowcroft.com/projects/motioncaptcha-jquery-plugin/>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

用鼠标来画个画。

|image20|

`siteHelp的DragCapCha <http://sitehelp.com.au/demos/dragcaptcha.php>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

为下面的字母排个序吧

|image21|

jQuery 验证码插件
^^^^^^^^^^^^^^^^^

`jQuery s3Capcha 插件 <http://serie3.info/s3capcha/demonstration.php>`__
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

|image22|

`Ajax Fancy Captcha <http://www.webdesignbeach.com/beachbar/ajax-fancy-captcha-jquery-plugin>`__
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

和上面那个不一样，这个需要拖动

|image23|

`wCaptcha <http://www.wozia.pt/blog/wcaptcha-a-better-captcha-alternative-jquery-captcha-plugin/>`__
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

和上面的很相似。

|image24|

`Picatcha <http://www.picatcha.com/captcha/>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

挑出所有的计算器

|image25|

`yoCaptcha <http://yocaptcha.com/>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

广告式的验证码

|image26|

W3C的建议
^^^^^^^^^

W3C的这篇文章（\ `http://www.w3.org/TR/turingtest/ <http://www.w3.org/TR/turingtest/>`__\ ）表达了传统的验证码图片的Inaccessibility的问题，而且一些验证码都很容易被破解。如：

W3C也给了一些解决方案：

-  一些逻辑题或是智力题。
-  声音输出，为了照顾残疾人。 \ `Spam-bot tests flunk the
   blind <http://news.com.com/2100-1032-1022814.html>`__
-  限制帐号的操作次数。
-  使用现有的Spam检测机制。如：酷壳（Coolshell.cn）的评论没有验证码，垃圾评论完全靠\ `Akismet <http://akismet.com/>`__ 插件过滤。

建议你移步去看看这篇文章。

（全文完）

.. |image0| image:: /coolshell/static/20140922103020605000.jpg
.. |image1| image:: /coolshell/static/20140922103020743000.jpg
.. |image2| image:: /coolshell/static/20140922103021108000.jpg
.. |image3| image:: /coolshell/static/20140922103021393000.jpg
   :target: http://coolshell.cn//wp-content/uploads/2012/07/2.jpg
.. |image4| image:: /coolshell/static/20140922103021434000.jpg
.. |image5| image:: /coolshell/static/20140922103021510000.jpg
.. |image6| image:: /coolshell/static/20140922103021554000.jpg
.. |image7| image:: /coolshell/static/20140922103021611000.jpg
.. |image8| image:: /coolshell/static/20140922103021716000.jpg
.. |image9| image:: /coolshell/static/20140922103021799000.jpg
   :target: http://coolshell.cn//wp-content/uploads/2012/07/9.jpg
.. |image10| image:: /coolshell/static/20140922103021888000.jpg
.. |image11| image:: /coolshell/static/20140922103021958000.jpg
   :target: http://coolshell.cn//wp-content/uploads/2012/07/a438_c13.jpg
.. |image12| image:: /coolshell/static/20140922103022028000.jpg
.. |image13| image:: /coolshell/static/20140922103022115000.jpg
.. |http://ocr-research.org.ua/tb/getimage.php5| image:: http://ocr-research.org.ua/tb/getimage.php5
   :target: http://ocr-research.org.ua/tb/getimage.php5
.. |image15| image:: /coolshell/static/20140922103022232000.png
.. |image16| image:: /coolshell/static/20140922103022307000.jpg
.. |image17| image:: /coolshell/static/20140922103022407000.jpg
.. |image18| image:: /coolshell/static/20140922103022492000.png
   :target: http://research.microsoft.com/en-us/um/redmond/projects/asirra/
.. |image19| image:: /coolshell/static/20140922103022636000.png
   :target: http://accessibiliteweb.com/stuff/captcha-slider.html
.. |image20| image:: /coolshell/static/20140922103022687000.png
   :target: http://josscrowcroft.com/projects/motioncaptcha-jquery-plugin/
.. |image21| image:: /coolshell/static/20140922103022746000.png
   :target: http://sitehelp.com.au/demos/dragcaptcha.php
.. |image22| image:: /coolshell/static/20140922103022824000.png
   :target: http://serie3.info/s3capcha/demonstration.php
.. |image23| image:: /coolshell/static/20140922103022881000.png
   :target: http://www.webdesignbeach.com/beachbar/ajax-fancy-captcha-jquery-plugin
.. |image24| image:: /coolshell/static/20140922103022911000.png
   :target: http://www.wozia.pt/blog/wcaptcha-a-better-captcha-alternative-jquery-captcha-plugin/
.. |image25| image:: /coolshell/static/20140922103022951000.png
   :target: http://www.picatcha.com/captcha/
.. |image26| image:: /coolshell/static/20140922103023020000.png
   :target: http://yocaptcha.com/
.. |image33| image:: /coolshell/static/20140922103026088000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/7917.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com