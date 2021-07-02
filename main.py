import time
import pymysql
import xml.etree.cElementTree as ET

# import charts

db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "root",
    "db": "INVEST",
    "charset": "utf8"
}

def ExecDB(command):
    try:
        conn = pymysql.connect(**db_settings)
        with conn.cursor() as cursor:
            cursor.execute(command)
            # 儲存變更
            conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()



def getStockList(xmlFile):
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    for child in root:

        stockId = child[1].text
        stockName = child[3].text
        stockFullName = child[2].text
        issueType = '上市'
        industryType = child[5].text
        listingDate = child[15].text
        updateDate = time.strftime("%Y%m%d", time.localtime())

        commond = f"INSERT INTO company (StockID, StockName, StockFullName, IssueType, IndustryType, ListingDate, UpdateDate) VALUE ('{stockId}', '{stockName}', '{stockFullName}', '{issueType}', '{industryType}', '{listingDate}', '{updateDate}')"
        # print(commond)
        ExecDB(commond)

def main():
    xmlFile = 'ListingCompany1.xml'
    getStockList(xmlFile)



if __name__ == '__main__':
    main()

