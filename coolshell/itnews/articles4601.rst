.. _articles4601:

关于Amazon云宕机的网贴收集
==========================

2011年4月27日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

最近，互联网上最大的事可能是Amazon的AWS宕机了，而且好几天都没有完全恢复。整个Internet都在讨论这个事，Internet很不高兴，后果可能很严重。可能是因为这个事件对中国没有影响，所以中文这边相关的文章不多，大家可以参考一下和讯网的这篇《\ `伤不起！亚马逊史前最大宕机事件的启示 <http://tech.hexun.com/2011-04-24/128998619.html>`__\ 》。

国外有人把所有和这个事件相关的贴子都收集了起来，都是一些相当不错的贴子和文章，尤其是一些经验教训的贴子，很受教，转给大家看看。这个贴子的\ `来源在这里 <http://highscalability.com/blog/2011/4/25/the-big-list-of-articles-on-the-amazon-outage.html>`__\ 。

个别公司的经历，有好有坏
^^^^^^^^^^^^^^^^^^^^^^^^

-  `How Heroku Survived the Amazon
   Outage <http://status.heroku.com/incident/151>`__ on the Heroku
   status page
-  `How SimpleGeo Stayed Up During the AWS
   Downtime <http://developers.simplegeo.com/blog/2011/04/26/how-simplegeo-stayed-up/>`__
   by Mike Malone
-  `How SmugMug survived the
   Amazonpocalypse <http://don.blogs.smugmug.com/2011/04/24/how-smugmug-survived-the-amazonpocalypse>`__
   by Don MacAskill  (`Hacker
   News <http://news.ycombinator.com/item?id=2480763>`__ discussion)
-  `How Bizo survived the Great AWS Outage of 2011 relatively
   unscathed… <http://dev.bizo.com/2011/04/how-bizo-survived-great-aws-outage-of.html>`__
   by Someone at Bizo
-  `Joe Stump’s
   explanation <http://www.focus.com/questions/information-technology/amazon-ec2-has-gone-down--what-would-prefered-hosting-be/#comment43192>`__
   of how SimpleGeo survived
-  `How Netflix Survived the
   Outage <http://www.slideshare.net/adrianco/netflix-in-the-cloud-2011>`__
-  `Why Twilio Wasn’t Affected by Today’s AWS
   Issues <http://www.twilio.com/engineering/2011/04/22/why-twilio-wasnt-affected-by-todays-aws-issues/>`__
   on Twilio Engineering’s Blog (`Hacker
   News <http://news.ycombinator.com/item?id=2472999>`__ thread)
-  `On reddit’s
   outage <http://www.reddit.com/r/announcements/comments/gva4t/on_reddits_outage/#>`__
-  `What caused the Quora problems/outage in April
   2011? <http://www.quora.com/Quora-Outage-April-21-22-2011/What-caused-the-Quora-problems-outage-in-April-2011>`__
-  `Recovering from Amazon cloud
   outage <http://tomatohater.com/2011/04/21/recovering-amazon-cloud-outage/>`__
   by Drew Engelson of PBS.

   -  PBS was affected for a while primarily because we do use
      EBS-backed RDS databases. Despite being spread across multiple
      availability-zones, we weren’t easily able to launch new resources
      ANYWHERE in the East region since everyone else was trying to do
      the same. I ended up pushing the RDS stuff out West for the time
      being.  `From
      Comment <http://don.blogs.smugmug.com/2011/04/24/how-smugmug-survived-the-amazonpocalypse/#comment-4737>`__

Amazon Web Services 讨论区
^^^^^^^^^^^^^^^^^^^^^^^^^^

有一些有经验的人共享了很多相当不错的宕机的经历。

There were also many many instances of support and help in the log.

总结
^^^^

立场：这是用户的错
^^^^^^^^^^^^^^^^^^

立场：这是Amazon的错
^^^^^^^^^^^^^^^^^^^^

教训和启示
^^^^^^^^^^

Vendor很生气
^^^^^^^^^^^^

（全文完）

.. |image6| image:: /coolshell/static/20140921221730863000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/4601.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com