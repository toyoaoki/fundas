import pandas as pd
import numpy as np
import networkx as nx
import graphviz as gv
from typing import Union

# 何の集まり？
# DataArray
# つまり　index => dim と dim => arr
# 右辺はfunctionとしよう
# 左辺はどう名前付けしようかな indexerとかでいいな
# indexerは全てのArrayに必要だろうか
# 無くていい気がする
# ある方が良いのは計算量的な観点
# まずはなしで設計
# category(functions) と　indexerの二つの構造
# categoryにはdagのschemeがあり、rootを取る関数がある
# 二つのdataframeをmergeすることができる
# それによってcategoryとindexerもmerge
# categoryのmergeは単にcategoryの合併
# indexerが大変。mergeする列を全て計算⇒pullbackを取る
# pullbackの取り方として、backpropergation的な手法を取るべきか否か
# まずはbackで！オプションにより計算方法を変える
# とするとfunctionで数式を使用するのが難しくなる
# whereでもそう。よってfowardで計算する必要あり
# category化するときに計算すべき？  
# index => dimはfunction内では？
# 両方function内に実装した方がよさそう？
# mergeはどうなる？
# 単なるschemeの追加＋pullbackの連鎖
# pullbackが鬼門で可換図式が出てくる。この扱いをどうするか
# 一旦pullbackを取れば二つのルートは片方で良い
# pullbackの連鎖はindexerとして取り出した方がいいのか？
# 結局実装は二つに一つでindexerかequationか
# 合流する物は全てeqが成立していると仮定する方がいいのでは
# mergeのdomはrooteでいいか？
# formula funcはどうなる？
# dfを更新する形が一番楽かな？
# groupbyは？
# groupbyobj*agg ⇒　funcs

class Indexer:
    
    def __init__(self) -> None:
        pass
    
    def to_dataframe(self):
        pass
    
    def display_dataframe():
        pass
    
    def display_scheme(self):
        pass
    
    def merge(self, other, **kwargs):
        pass
    
    def where(self, cond):
        pass

    def __eq__(self, o: object) -> bool:
        pass

    def __ne__(self, o: object) -> bool:
        pass

    def __lt__(self, o: object) -> bool:
        pass

    def __gt__(self, o: object) -> bool:
        pass
    
class Function:
    
    def __init__(self, data, dom=None, cod=None, formula=None) -> None:
        pass
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass
    
    
class Category:
    
    def __init__(self, functions={}) -> None:
        self.functions = functions
    
    def add(self, function:'Function') -> 'Category':
        self[function.cod_name] = function
        return self
        
    def drop(self, function:Union[str, 'Function']) -> 'Category':
        if isinstance(function, str):
            function_name = function
        else:
            function_name = function.cod_name
        del self[function_name]
        return self
    
    def __getattr__(self, name):
        #自分に無い属性はてself.functionsからとって来る
        return getattr(self.functions, name)