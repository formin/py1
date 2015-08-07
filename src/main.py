#coding=utf-8 ~

import module_using_db
import datetime

stype = raw_input("Enter an [S]study mode or [E]excute mode : ")

if stype.upper() == "S":

    start = datetime.datetime.now()
    print start

    """
    print 'Create iteminfoDB start Please wait.'
    module_using_db.iteminfoDB('../oth/item.db','../rsc/round2_itemInfo.tsv')
    print 'Create iteminfoDB end'

    print 'Create purchaseRecordDB start Please wait.'
    module_using_db.purchaseRecordDB('../oth/item.db','../rsc/round2_purchaseRecord.tsv')
    print 'Create purchaseRecordDB end'

    print 'Sort User start Please wait.'
    module_using_db.SortUser('../oth/item.db')
    print 'Sort User end'

    print 'Sort PurchaseRecord1 start Please wait.'
    module_using_db.SortPurchaseRecord1('../oth/item.db')
    print 'Sort PurchaseRecord1 end'

    print 'Sort PurchaseRecord2 start Please wait.'
    module_using_db.SortPurchaseRecord2('../oth/item.db')
    print 'Sort PurchaseRecord2 end'

    print 'Sort PurchaseRecord3 start Please wait.'
    module_using_db.SortPurchaseRecord3('../oth/item.db')
    print 'Sort PurchaseRecord3 end'

    print 'Sort PurchaseRecord4 start Please wait.'
    module_using_db.SortPurchaseRecord4('../oth/item.db')
    print 'Sort PurchaseRecord4 end'
    """

    print 'Sort PurchaseRecord5 start Please wait.'
    module_using_db.SortPurchaseRecord5('../oth/item.db')
    print 'Sort PurchaseRecord5 end'

    print 'Sort PurchaseRecord6 start Please wait.'
    module_using_db.SortPurchaseRecord6('../oth/item.db')
    print 'Sort PurchaseRecord6 end'


    end = datetime.datetime.now()
    print end
    print end-start

elif stype.upper() == "E":

    start = datetime.datetime.now()
    print start

    print 'Excute Data start Please wait.'
    module_using_db.ExcuteData('../oth/item.db','../predict.csv')
    print 'Excute Data end'

    end = datetime.datetime.now()
    print end
    print end-start
