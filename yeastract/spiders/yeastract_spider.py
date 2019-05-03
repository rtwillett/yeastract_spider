from scrapy import Spider, Request
from yeastract.items import YeastractItem
import pandas as pd


url_stub = "http://www.yeastract.com/view.php?existing=go&orfname="


class Yeastract_Spider(Spider):
    name = "yeastract"
    allowed_urls = ["http://www.yeastract.com"]

    df_genes = pd.read_csv("labels_BP.csv", usecols = ["genes"])
    all_genes = df_genes["genes"].tolist()

    start_urls = [url_stub + i for i in all_genes]


    def parse(self, response):

        proteinname = response.xpath('//td[@property="yontology:proteinName_"]/text()').extract_first()
        description = response.xpath('//td[@property="yontology:description_"]/text()').extract_first()

        # Joining list with : demarcators
        go_BioProc = response.xpath('//table[@summary="main content"]//table/tr[1]//a/text()').extract()
        go_BioProc = (":").join(go_BioProc)

        # Joining list with : demarcators
        go_MolFunc = response.xpath('//table[@summary="main content"]//table/tr[2]//a/text()').extract()
        go_MolFunc = (":").join(go_MolFunc)

        # Joining list with : demarcators
        go_CellComp = response.xpath('//table[@summary="main content"]//table/tr[3]//a/text()').extract()
        go_CellComp = (":").join(go_CellComp)

        print(proteinname)
        print("="*55)
        print(description)
        print("="*55)
        print(go_BioProc)
        print("="*55)
        print(go_MolFunc)
        print("="*55)
        print(go_CellComp)
        print("="*55)
        print("FINISHED")

        item = YeastractItem()

        item["proteinname"] = proteinname
        item["description"] = description
        item["go_BioProc"] = go_BioProc
        item["go_MolFunc"] = go_MolFunc
        item["go_CellComp"] = go_CellComp
        print('item: ', item)
        yield item
