.. _articles1313:

Erlang和Python互通
==================

2009年8月24日
`free.wang <http://coolshell.cn/articles/author/free-wang>`__

最近开发 Erlang
,对其字符串处理能力无言至极,于是决定把它和python联合起来,打造一个强力的分布式系统,等将来需要系统级开发时,我再把
C++/C组合进来.

首先参考了 Erlang
官方文档和 \ `http://blog.developers.api.sina.com.cn/?tag=\ **erlang** <http://www.zend2.com/DoIt.php?u=Oi8vd3d3LmJsb2dnZXIuY29tL2Jsb2cuZGV2ZWxvcGVycy5hcGkuc2luYS5jb20uY24vP3RhZz1lcmxhbmc%3D&b=5>`__
以及\ `http://kazmier.net/computer/port-howto/ <http://www.zend2.com/DoIt.php?u=Oi8va2F6bWllci5uZXQvY29tcHV0ZXIvcG9ydC1ob3d0by8%3D&b=5>`__
.

| 研读了将近24个小时, 才终于完全把问题解决.
 起名为town，town在英文里表示集市，也就是代表各种语言在这里的交流与互动。)
)

::

    -module(town).
    -behaviour(gen_server).

    %% API
    -export([start/0,combine/1]).

    %% gen_server callbacks
    -export([init/1, handle_call/3, handle_cast/2, handle_info/2,
    terminate/2, code_change/3]).
    -record(state, {port}).

    start() ->
      gen_server:start_link({global, ?MODULE}, ?MODULE, [], []).
    stop() ->
      gen_server:cast(?SERVER, stop).
    init([]) ->
      process_flag(trap_exit, true),
      Port = open_port({spawn, "python -u /home/freefis/Desktop/town.py"},[stream,{line, 1024}]),
      {ok, #state{port = Port}}.

    handle_call({combine,String}, _From, #state{port = Port} = State) ->
      port_command(Port,String),
      receive
        {Port,{data,{_Flag,Data}}} ->
          io:format("receiving:~p~n",[Data]),
          sleep(2000),
          {reply, Data, Port}
      end.
    handle_cast(stop, State) ->
      {stop, normal, State};
    handle_cast(_Msg, State) ->
      {noreply, State}.

    handle_info(Info, State) ->
      {noreply,State}.

    terminate(_Reason, Port) ->
      ok.

    code_change(_OldVsn, State, _Extra) ->
      {ok, State}.

    %%--------------------------------------------------------------------
    %%% Internal ---------------------------------------------------------
    combine(_String) ->
      start(),
      String = list_to_binary("combine|"++_String++"\n"),
      gen_server:call(?SERVER,{combine,String},infinity),
      stop().

这段是Python的脚本
当erlang中town:combine(“sentence1+sentence2″)执行时，会在后台启动python的脚本，处理完毕后返回给Erlang结果:sentence1sentence2，然后退出。

::

    import sys
    def handle(_string):
        if _string.startswith("combine|"):
            string = "".join( _string[8:].split(","))
            return string

    """waiting for input """
    while 1:
        # Recv. Binary Stream as Standard IN
        _stream = sys.stdin.readline()

    if not _stream: break
        # Scheme, Turn into  Formal String
        inString  = _stream.strip("\r\n")
        # handle String
        outString = handle(inString)
        # send to port as Standart OUT
        sys.stdout.write("%s\n" % (outString,))
        sys.exit(0)

.. |image6| image:: /coolshell/static/20140920235416102000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/1313.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com