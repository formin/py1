
1.�˰��� �� �ڵ� ����

 �˰��� ����: ������� ���� �̷� �� ����, �⿬��, �帣�� Ȯ���ϰ� ���� �������� ���� �̷��� ���� ���� ������ �� �ش� ����ڿ� ���� �̷��� ���� ������ 100 ������ ���� �մϴ�.  

 main.py: main ���� ����

  # ��ȭ ������������ sqlite �� insert
  module_using_db.iteminfoDB('../oth/item.db','../rsc/round2_itemInfo.tsv')

  # �����̷������� sqlite �� insert
  module_using_db.purchaseRecordDB('../oth/item.db','../rsc/round2_purchaseRecord.tsv')

  # �����̷� ���� �� ����� ������ ����
  module_using_db.SortUser('../oth/item.db')

  # �����̷��� ���� ��ȭ �������� ����
  module_using_db.SortPurchaseRecord('../oth/item.db')

  # �����̷��� ���� ������ �� �� ����ڰ� �������� ���� ������ ���� �� ���Ϸ� ����
  module_using_db.SortData('../oth/item.db','../predict.csv')

 module_using_db.py: �⺻ ���̺� ����

  # t1 table : ��ȭ ������ ����, COL1 ������, COL2 ����, COL3 �⿬��, COL4 �帣

  # t2 table : ��ȭ ���� ���� COL1 ������, COL2 ������

  # t3 table : ��ȭ �����̷� ���� ������ ��ŷ COL1 ������, COL2 ������

  # t4 table : ��ü ����� ����Ʈ COL1 ������

  # t5 table : ����ڰ� �������� ���� ������ �� ���� �̷��� ���� ���� 100 ���� ���� COL1 �����, COL2 ������

  # t6 table : ����ڰ� ������ ������ �帣���� �������� ���� ������ �� ���� �̷��� ���� ���� 100 ���� ���� COL1 �����, COL2 ������ COL4 �帣

  # t7 table : ����ڰ� ������ �������� �⿬�ڿ��� �������� ���� ������ �� ���� �̷��� ���� ���� 100 ���� ���� COL1 �����, COL2 ������ COL3 �⿬��

  # t8 table : ����ڰ� ������ �������� �������� �������� ���� ������ �� ���� �̷��� ���� ���� 100 ���� ���� COL1 �����, COL2 ������ COL2 ����


2.����ȯ�� �� ������ ���� 

 ����ȯ��: python 2.7

 ������: python.exe main.py

3.������

 byte_of_python.pdf
  A Byte of Python
  Swaroop C H <swaroop@swaroopch.com>
  Translated by Jeongbin Park <pjb7687@gmail.com>



