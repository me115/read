.. _200803_imdb_database_structure:

Imdb的数据库结构
===================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2008/03/imdb_database_structure.html>`__

|mf2008031601.jpg|

`IMDB <http://www.imdb.com/>`__\ 号称是地球上最大的电影数据库，几乎所有的电影都能够在里面查到。它是我最喜欢的网站之一。

它的\ `数据库结构 <http://www.imdb.com/Licensing/structure.html>`__\ 是公开的，但是数据库不公开，必须付费才能使用。使用费非常贵，每年最少也要15000美元。

我今天下午看了它的数据库结构，如我所料，对数据格式要求很严格。这意味着用户提交数据非常麻烦，必须遵循繁琐的\ `格式规定 <http://www.imdb.com/updates/guide/>`__\ ，并且还要通过管理员审核，才能正式收入数据库。我猜想，IMDB一定雇佣了很庞大的编辑队伍。

但是，这样的好处是，它的数据高度结构化，查找起来非常方便，可以精确查询和排序每一个字段。因此，它的数据商业价值很高。

下面就是它的数据库结构。


==============

| 1. 字段名：IMDb Constant Title Code 类型： 7 Digit Number
含义：每部电影在IMDB中的唯一编号。 示例： 0068646 2. 字段名：Title
类型： Text 含义：电影名。 示例： The Godfather 3. 字段名：Year 类型： 4
digit Number 含义：电影首次公映时间。 示例：1972 4. 字段名：Plot Outline
类型： Text
|  含义：电影情节的一句话总结。
|  示例：A Mafia boss’ son, previously uninvolved in the business, takes
over when his father is critically wounded in a mob hit.

| 5. 字段名：Plot Summary 类型：Text
|  含义：情节简介。
|  示例：Don Vito Corleone is the head of a New York Mafia “family”.
Problems arise when a gangster supported by another Mafia family,
Sollozzo, announces his intentions to start selling drugs all over New
York. Don Vito hates the idea of drugs, and he is quite happy with the
gambling/protection etc. that make him money, so an attempt is made on
his life. Sollozzo then kidnaps one of Don Vitos advisors, and tries to
make him force Don Vitos son to agree to sell drugs, but the plan goes
wrong when Sollozzo finds out that Don Vito is still alive.

| 6. 字段名：Principal Cast 类型：Text 含义：主要演员，最多不超过5个。
示例：Marlon Brando Al Pacino Diane Keaton
|  Richard S. Castellano
|  Robert Duvall

| 7. 字段名：Genre 类型：Text Set
|  含义：电影的类型，可能的取值为以下几种——Action, Adventure, Animation,
Comedy, Crime, Documentary, Drama, Family, Fantasy, Film-Noir, Horror,
Musical, Mystery, Romance, Sci-Fi, Short, Thriller, War, Western。
|  示例：Crime, Drama

| 8. 字段名：MPAA Rating 类型：Text
|  含义：美国的电影分级，可能的取值为以下几种——G, PG, PG-13, R, NC-17,
X。
|  示例：USA:R

| 9. 字段名：U.S. Runtime 类型：Minutes 含义：电影长度。 示例：175 10.
字段名：Trivia 类型：Text
|  含义：电影花絮。
|  示例：The phone number Michael calls to find out news about his
father is Long Beach 4-5620.

| 11. 字段名：Goofs 类型： Text
|  含义：电影中穿帮和不合理的镜头。
|  示例：In several scenes wine bottles are shown with the DOC Italian
wine classification designation shown on the bottle. DOC designations
did not come in effect until the 1960s.

| 12. 字段名：Writer(s) 类型：Text
|  含义：编剧。
|  示例：Coppola, Francis Ford;Puzo, Mario

| 13. 字段名：Plot Keywords 类型：Text Set 含义：情节关键词。
示例：garrote;revenge;father-son-relationship 14. 字段名：IMDb Average
User Rating 类型：Number
|  含义：观众的平均打分，最高10分，最低1分。
|  示例：9.0

| 15. 字段名：Link to official site
|  类型：URL
|  含义：电影的官方网站。

| 16. 字段名：Additional Cast 类型：Text
|  含义：除主要演员外的其他演员,最多不超过10个。
|  示例：James Caan;Talia Shire;Sterling Hayden

| 17. 字段名：External Reviews Links
|  类型：URL
|  含义：外部影评文章的网址。

| 18. 字段名：Links to Trailers
|  类型：Text
|  含义：预告片的观看网址。

| 19. 字段名：Producer(s)
|  类型：Text
|  含义：制片人

| 20. 字段名：Distributor(s)
|  类型：Text Set
|  含义：发行商

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2008/03/imdb_database_structure.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com