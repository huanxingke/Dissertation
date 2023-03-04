# 取消gensim的warning
import warnings
warnings.filterwarnings("ignore")

from gensim import corpora, models, similarities
import logging
import jieba
import json

# 取消jieba的日志输出
jieba.setLogLevel(logging.INFO)


class Query(object):
    def __init__(self):
        # 加载化学品数据
        with open("chemicals.json", "r") as fp:
            self.chemicals = json.load(fp)
        # 加载索引字典
        self.dictionary = corpora.Dictionary.load("chemicals.dictionary")
        # 加载模型
        self.tfidf = models.TfidfModel.load("chemicals.tfidf")
        # 加载相似度对象
        self.index = similarities.MatrixSimilarity.load("chemicals.index")

    # 搜索
    def run(self, keywords):
        # 处理
        keywords = jieba.lcut(keywords)
        # 生成搜索词袋
        keywords_corpus = self.dictionary.doc2bow(keywords)
        # 转换为TF-IDF主题向量
        keywords_vec = self.tfidf[keywords_corpus]
        # 计算相似度
        sim = self.index[self.tfidf[keywords_vec]]
        # 排序以获取相似度结果
        sim_sorted = [i for i in sorted(enumerate(sim), key=lambda item: -item[1]) if i[1] != 0]
        # 从总数据中检索
        query_results = []
        for i in sim_sorted:
            chemical_index, chemical_sim = i
            query_result = self.chemicals[chemical_index]
            query_result["similarity"] = chemical_sim
            query_results.append(query_result)
        # 返回搜索结果
        return query_results


if __name__ == '__main__':
    res = Query().run("甲烷")
    for o in res:
        print(o)