.. _articles3498:

信XML，得自信
=============

2011年1月19日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

XML可能是计算有史以来最NB的发明了，以至于我们以没有XML的程序是难登大堂的程序，不用XML，你都不好意思当程序员。于是，我们看到了\ `很多很雷人的用法 <http://coolshell.cn/articles/2504.html>`__\ （《信XML，得永生》），当然一些朋友当时并没有看懂，不过我不怪大家，因为我们依然深信使用XML可以让你有强大的Zhuangbility，于是我们有下面这两种相当Geiliable的用法。

一、XML中的XML
^^^^^^^^^^^^^^

这个例子是某公司的一个SOAP实现——我们的Webservice需要返回一个XML字符串，这怎么办呢？其实很容易，因为——XML是无所不能的，那怕是封装自己。

::



      <CompanyGetConnector>
        <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
          <xs:element name="InitechGetConnector">
            <xs:complexType>
              <xs:choice maxOccurs="unbounded">
                <xs:element name="employees">
                  <xs:complexType>
                    <xs:sequence>
                      <xs:element name="EmployerName" type="xs:string" minOccurs="0"/>
                      <xs:element name="Employee" type="xs:string" minOccurs="0"/>
                      <xs:element name="Firstname" type="xs:string" minOccurs="0"/>
                      <xs:element name="Prefix" type="xs:string" minOccurs="0"/>
                      <xs:element name="Lastname" type="xs:string" minOccurs="0"/>
                      <xs:element name="Org._unit" type="xs:string" minOccurs="0"/>
                      <xs:element name="Function" type="xs:string" minOccurs="0"/>
                      <xs:element name="E-mail_work" type="xs:string" minOccurs="0"/>
                      <xs:element name="Telephone_work" type="xs:string" minOccurs="0"/>
                      <xs:element name="Mobile_work" type="xs:string" minOccurs="0"/>
                      <xs:element name="Birthdate" type="xs:date" minOccurs="0"/>
                      <xs:element name="Hired_since__irt._yearsemployed_" type="xs:date" minOccurs="0"/>
                      <xs:element name="Image" type="xs:base64Binary" minOccurs="0"/>
                    </xs:sequence>
                  </xs:complexType>
                </xs:element>
              </xs:choice>
            </xs:complexType>
          </xs:element>
        </xs:schema>

        <employees>
          <EmployerName>
            My Client
          </EmployerName>
          <Employee>
            100001
          </Employee>
        </employees>
      </CompanyGetConnector>

二、一切皆为配置
^^^^^^^^^^^^^^^^

没有hard code这是一个优秀程序员在入门时就要学习的，对于Hard
Coder的东西最好写在配置文件中，这样修改这些参数就不需要修改代码而需要重新编译了。自从有了XML之后，我们的配置文件就不在使用像ini文件或是Unix下在conf文件那样的易读，我们认为，使用XML作为配置文件的格式是大势所趋，而且，我们要让我们的代码尽量的可以高度的配置，于是我们出现了下面的代码——这是一个强大的尝试，其标志着，我们完全可以以不久的未来用XML来编写一切语言的代码。

注：下面的代码最强大的应该是XML中的那个SQL。

::

     

来源：\ `文章一 <http://thedailywtf.com/Articles/All-In-The-Config.aspx>`__\ ，\ `文章二 <http://thedailywtf.com/Articles/XMLd-XML.aspx>`__

.. |image6| image:: /coolshell/static/20140922113554697000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/3498.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com