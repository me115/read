#! /usr/bin/env python
#coding=utf-8
# author liudong@  3/27/2014
# rst 文件生成后，为了格式整洁而修剪 
import os,sys,re,traceback
from datetime import datetime
#from avlog import LOG_ERR, LOG_INFO

class Rstclip:
    
    # 遍历所有文件
    def dirAllFileInDir(self,dir):
        for filename in os.listdir(dir):
            if filename == '.' or filename == '..':
                continue
            elif os.path.isfile(filename) and filename[-4:] == '.rst':
                self.clip(dir.rstrip('/') + '/' +  filename)
            elif os.path.isdir(filename):
                self.dirAllFileInDir(dir.rstrip('/') + '/' +  filename)
                
    # 修剪单个文件
    def clip(self, filename):
        #首先重命名
        tmpfile= filename + '.tmp'
        os.rename(filename,tmpfile )
        
        f = open(tmpfile,'r')
        alllines = f.readlines()
        
        h1idx,h2idx,paperend,imgBegin =0,0,0,0
        for i,line in enumerate(alllines):
            # find h1
            if line.strip() != '' and line.strip().strip('=') == '':
                h1idx = i -1 
            # find h2
            if line.strip() != '' and line.strip().strip('-') == '':
                h2idx = i -1
            # find paper end
            if line.count('访问 `酷壳404页面') > 0:
                paperend = i -2
            # find image idx
            if line[0:3] == '.. ' and i > paperend and imgBegin == 0:
                imgBegin = i
        
        print h1idx,h2idx,paperend,imgBegin
        fw = open(filename,'w')
        for i,line in enumerate(alllines):
            if (i >= 2 and i < h2idx) or ( i >= paperend and i < imgBegin):
                continue
            #删除没有垃圾信息行
            if line.count('|好烂啊|') > 0 or line.count('平均分：') > 0 or \
                line.count('Loading …') > 0 or line.count('.. |有点差| image') > 0 or \
                line.count('.. |凑合看看|') > 0 or line.count('.. |还不错|') > 0 or \
                line.count('.. |很精彩|') > 0 or line.count('.. |Loading ...|') > 0 or \
                line.count('.. |Loading...|') > 0:
                continue
            
            if i == h2idx +1 : # 提升为h1
                line = line.replace('-','=')
            
            fw.writelines(line)
    
if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    
    rst = Rstclip()
    try:
        
        rst.dirAllFileInDir('.')
    except Exception, ex:
        exc = traceback.format_exc()
        sys.stderr.write("trace =%s \n" % exc)
        sys.stderr.write("ex=%s \n" % str(ex))
